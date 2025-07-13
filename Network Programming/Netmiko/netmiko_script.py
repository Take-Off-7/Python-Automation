from netmiko import ConnectHandler
import getpass

credentials = {
    "username": "developer", 
    "password": getpass.getpass("Password:")
}

devices = [
    {"device_type": "cisco_ios", "host": "10.10.20.48"},
    {"device_type": "cisco_ios", "host": "10.10.20.35"}
]

for device in devices:
    device = {**credentials, **device}

    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip int brief')
    print(output)

    output = net_connect.send_config_set(['do show arp'])
    print(output)
