# Simple API for printing hostname, environment variables and time

## Run on local machine 

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./app.py
```

## Build Docker image

```bash
docker build -t python-flask-api-hostname-env-time .
docker run -it --rm -p 127.0.0.1:5080:5000 --name python-flask-api-hostname-env-time python-flask-api-hostname-env-time
docker tag python-flask-api-hostname-env-time:latest python-flask-api-hostname-env-time:1.0
docker tag python-flask-api-hostname-env-time:1.0 sebaczech/python-flask-api-hostname-env-time:1.0   
docker push sebaczech/python-flask-api-hostname-env-time:1.0
```
