# Fetch Synthetic Monitor

A simple python program to check the health of a set of HTTP endpoints. 

## Sample Input File
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

## Output
```
fetch.com has 33% availability percentage
www.fetchrewards.com has 100% availability percentage
fetch.com has 67% availability percentage
www.fetchrewards.com has 50% availability percentage
```

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

# TO DO
- Add TDD unit tests
- Improve logging 
- CICD githab actions to build and deploy
- Improve Dockerfile
- Dependabot
- Auto pylint + flake8
