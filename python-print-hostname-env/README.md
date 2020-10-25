# Simple app for printing hostname, environment variables and configuration

## Run on local machine 

```bash
source venv/bin/activate          
./app.py
```

## Build Docker image

```bash
docker build -t python-print-hostname-env .
docker run -it --rm --name python-print-hostname-env python-print-hostname-env
docker tag python-print-hostname-env:latest python-print-hostname-env:1.0
docker tag python-print-hostname-env:1.0 sebaczech/python-print-hostname-env:1.0   
docker push sebaczech/python-print-hostname-env:1.0
```
