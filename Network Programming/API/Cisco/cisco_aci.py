import requests
import json
from itertools import count

#################### LOGIN ####################
url = "https://10.10.20.14"
auth_url = url + "/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "C1sco12345"
        }
    }
}

headers = {"content-type": "application/json"}

response = requests.post(
    auth_url,
    data=json.dumps(payload),
    headers=headers,
    verify=False
).json()

# print(json.dumps(response, indent=2, sort_keys=True))

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookies = {'APIC-cookie': token}

query_url = url + "/api/class/fvAp.json"

headers = {'cache-control': 'no-cache'}

get_response = requests.get(
    query_url,
    headers=headers,
    cookies=cookies,
    verify=False
).json()

# print(json.dumps(get_response, indent=2, sort_keys=True))

for item in get_response["imdata"]:
    name = item["fvAp"]["attributes"]["name"]
    print(f"Name: {name}")

