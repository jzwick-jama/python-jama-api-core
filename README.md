# python-jama-api-core
A module for Python3 that can be used to send test API calls based on the .env variables set up before starting the script


Setup:
=====

1. Copy .env.example as .env and fill out the variables. No quotes are needed.
2. Run the following commands

python3 -m pip install virtualenv 
# if you don't have it already

python3 -m virtualenv .venv

source .venv/bin/activate

python3 -m pip install python-dotenv py-jama-rest-client


3. Now you should be ready to run with "python3 main.py" and the results will output to console. You can also assign to a variable, the Jama module will convert the return as an iteratable custom object with hashtables inside. 

See https://pypi.org/project/py-jama-rest-client/ for more examples of put, patch and other calls
