import requests
import json
from pprint import pprint

url='https://sbx-nxos-mgmt.cisco.com/ins'
switchuser='admin'
switchpassword='Admin_1234!'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,
                         data=json.dumps(payload), 
                         headers=myheaders,
                         auth=(switchuser,switchpassword),
                         verify=False
                         ).json()
pprint(response)
