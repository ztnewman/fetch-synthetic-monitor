# Fetch Synthetic Monitor

A simple python program to check the health of a set of HTTP endpoints. 

## Sample input file
```
- headers:
user-agent: fetch-synthetic-monitor
method: GET
name: fetch index page
url: https://fetch.com/
- headers:
user-agent: fetch-synthetic-monitor
method: GET
name: fetch careers page
url: https://fetch.com/careers
- body: '{"foo":"bar"}'
headers:
content-type: application/json
user-agent: fetch-synthetic-monitor
method: POST
name: fetch some fake post endpoint
url: https://fetch.com/some/post/endpoint
- name: fetch rewards index page
url: https://www.fetchrewards.com/
```

## Schema 
● name (string, required) — A free-text name to describe the HTTP endpoint.
● url (string, required) — The URL of the HTTP endpoint.
○ You may assume that the URL is always a valid HTTP or HTTPS address.
● method (string, optional) — The HTTP method of the endpoint.
○ If this field is present, you may assume it’s a valid HTTP method (e.g. GET, POST,
etc.).
○ If this field is omitted, the default is GET.
● headers (dictionary, optional) — The HTTP headers to include in the request.
○ If this field is present, you may assume that the keys and values of this dictionary
are strings that are valid HTTP header names and values.
○ If this field is omitted, no headers need to be added to or modified in the HTTP
request.
● body (string, optional) — The HTTP body to include in the request.
○ If this field is present, you should assume it's a valid JSON-encoded string. You
do not need to account for non-JSON request bodies.
○ If this field is omitted, no body is sent in the request.

● UP — The HTTP response code is 2xx (any 200–299 response code) and the response
latency is less than 500 ms.
● DOWN — The endpoint is not UP.

## Output
fetch.com has 33% availability percentage
www.fetchrewards.com has 100% availability percentage
fetch.com has 67% availability percentage
www.fetchrewards.com has 50% availability percentage

## Install

### Source

Clone the repository:

```bash
git clone https://github.com/ztnewman/fetch-synthetic-monitor.git && cd fetch-synthetic-monitor
```

Create a virtual environment (recommended):
```
python -m venv env
source env/bin/activate
pip install -r requiements.txt
```

Run:
```
python fetch-synthetic-monitor.py -c endpoints.yaml
```

## Docker

Build the container:
```
docker build -t fetch-synthetic-monitor .
```

Run:
```
docker run -it fetch-synthetic-monitor endpoints.yaml
```

# Argumentss
```
-v verbose
-l latency
-t seconds
-l latency
```

# Testing

# Security

# CICD

# Helm 

# TO DO
- Make object oriented class for clean up and reproduce
- Add tests for tdd
- Improve logging 
- Arguments for seconds, latency, headers
- Add githab actions to build and deploy
- Improve Dockerfile to reduce layers
- Security scan container
- Dependabot
- Lint flake8
