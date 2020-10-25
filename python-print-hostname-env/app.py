#!venv/bin/python
import socket
import os
import datetime

print("HOST: " + socket.gethostname())
print("CONFIG: " + str(os.environ.get('PYTHON_HOSTNAME_ENV_VERSION')))
print("TIME: ", datetime.datetime.now().strftime("%H:%M:%S"))
