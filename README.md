## Fetch Synthetic Monitor

A simple python program to check the health of a set of HTTP endpoints. 

---

## Background


## Install

Clone the repository:
```bash
git clone https://github.com/ztnewman/fetch-synthetic-monitor.git && cd fetch-synthetic-monitor
```

Create a virtual environment:
```bash
python -m venv env
source env/bin/activate
pip install -r requiements.txt
```

### Docker Image

Build the container:
```bash
docker build -t fetch-synthetic-monitor .
```

## Usage

Run the python script:
```bash
python fetch-synthetic-monitor.py -c endpoints.yaml
```

Run the docker image:
```bash
docker run -it fetch-synthetic-monitor endpoints.yaml
```

### TO DO
- Add TDD unit tests
- Improve logging 
- CICD githab actions to build and deploy
- Improve Dockerfile
- Dependabot
- Auto pylint + flake8

### License

[MIT © Richard McRichface.](../LICENSE)
## 
