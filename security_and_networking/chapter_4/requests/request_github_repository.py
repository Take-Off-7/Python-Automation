import requests

response = requests.get('https://api.github.com/users/Take-Off-7')

print(response.url)
print(response.text)
