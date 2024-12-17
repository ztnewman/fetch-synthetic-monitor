import logging
import argparse
import asyncio
import time
from urllib.parse import urlparse
import aiohttp
import yaml


class FetchMonitor:
    """ Fetch Monitor Class"""

    def __init__(self, config_file, interval, max_latency):
        self.config_file = config_file
        self.interval = interval
        self.max_latency = max_latency
        self.endpoints = self._load_config()
        self.availability = {}
        self._initialize_availability()

    def _load_config(self):
        """
        Get the endpoints from config file
        """

        with open(self.config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _initialize_availability(self):
        """
        Create dict of domain and their endpoint status
        """

        for endpoint in self.endpoints:
            domain = urlparse(endpoint['url']).netloc
            if domain not in self.availability:
                self.availability[domain] = []

    async def check_endpoint(self, session, endpoint):
        """
        Make an HTTP call to the endpoint and determine status
        """

        start_time = time.time()
        try:
            method = endpoint.get('method', 'GET')
            headers = endpoint.get('headers', {})
            body = endpoint.get('body', None)
            domain = urlparse(endpoint['url']).netloc
            async with session.request(method, endpoint['url'], headers=headers, data=body, timeout=5) as response:
                # Calculate latency as milliseconds from current time minus start time in ms
                latency = (time.time() - start_time) * 1000
                logging.debug("[DEBUG] Request: %s - %s - %s - %i", method, endpoint['url'], response.status, latency)
                result = "UP" if ((response.status < 300) and (latency < self.max_latency)) else "DOWN"
                logging.debug("[DEBUG] Endpoint '%s' %s has HTTP response code %s and response latency %i => %s",
                              domain, endpoint['name'].split(' ', 1)[1], response.status, round(latency), result)
                logging.debug("")
                return 200 <= response.status < 300 and latency < self.max_latency

        except aiohttp.ClientError as e:
            raise SystemExit(e) from e

    async def run_checks(self):
        """
        Asynchronously check each endpoint and calculate availability
        """

        async with aiohttp.ClientSession() as session:
            tasks = [
                self.check_endpoint(session, endpoint)
                for endpoint in self.endpoints
            ]
            results = await asyncio.gather(*tasks)

            domain_results = {}
            for endpoint, is_up in zip(self.endpoints, results):
                domain = urlparse(endpoint['url']).netloc
                if domain not in domain_results:
                    domain_results[domain] = []
                domain_results[domain].append(is_up)

            self.calculate_availability(domain_results)

    def calculate_availability(self, domain_results):
        """
        Calculate the availability percentage for each domain
        """

        for domain, results in domain_results.items():
            up_total = sum(results)
            availability_pct = (up_total / len(results)) * 100
            logging.info("%s has %.0f%% availability percentage", domain, availability_pct)
        logging.info("")

    async def monitor(self):
        """
        Check endpoints and pause for the interval specified until interupted 
        """

        while True:
            await self.run_checks()
            await asyncio.sleep(self.interval)


def main():
    """ Parse arguments and create a FetchMonitor """

    parser = argparse.ArgumentParser(description='HTTP Endpoint Health Monitor')
    parser.add_argument('config', help='YAML config file path')
    parser.add_argument('-l', '--latency', help='latency max in ms', type=int, default=500)
    parser.add_argument('-s', '--seconds', help='seconds between each test cycle', type=int, default=15)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger('asyncio').setLevel(logging.WARNING)
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    fetch = FetchMonitor(args.config, args.seconds, args.latency)

    try:
        asyncio.run(fetch.monitor())
    except KeyboardInterrupt:
        logging.info("Monitoring stopped")


if __name__ == "__main__":
    main()
