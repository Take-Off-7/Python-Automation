import requests
from pprint import pprint
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

########## List Organizations ########## 

url = "https://dashboard.meraki.com/api/v1/organizations/"
headers = {
    'X-Cisco-Meraki-API-Key': 'f4c9deb8ea1546aa6c00db8400728096a6003279',
    'Content-Type': 'application/json'
}
response = requests.get(url, headers=headers, verify=False)
# pprint(response.json())

if response.status_code == 200:
    organizations = response.json()
    for org in organizations:
        print(f"Organization Name: {org['name']}, ID: {org['id']}")
else:
    print(f"Error {response.status_code}: {response.text}")

orgId = organizations[0]['id']


########## List Networks in Organization ########## 

net_url = url + orgId + '/networks'
response = requests.get(net_url, headers=headers, verify=False)

if response.status_code == 200:
    networks = response.json()
    for net in networks:
        print(f"Network Name: {net['name']}, ID: {net['id']}")
else:
    print(f"Error {response.status_code}: {response.text}")

netId = networks[0]['id']


########## List Devices in Network ########## 

dev_url = "https://dashboard.meraki.com/api/v1/networks/{netId}/devices"
response = requests.get(net_url, headers=headers, verify=False)

if response.status_code == 200:
    devices = response.json()
    for dev in devices:
        print(f"Devices: {dev['productTypes']}")
else:
    print(f"Error {response.status_code}: {response.text}")
