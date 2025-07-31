import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = input("Enter username:") # postman
password = getpass() # password

response = requests.get(
    'https://postman-echo.com/basic-auth',
    auth=HTTPBasicAuth(username,password)
)

print('Response.status_code:' + str(response.status_code))
if response.status_code == 200:
    print('Login successful :' + response.text)
