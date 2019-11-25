After cloning, install requirements:
### 'pip install -r requirements.txt'
This will install Resdec needed packages.
There is a bug which prevents starting services when there is not a log/debug.log file. Create it manually so services can be started
### 'python .\manage.py runserver 0.0.0.0:5000'
Starts thebackend server at port 5000
