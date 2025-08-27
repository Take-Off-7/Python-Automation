from network_pb2 import Router

# Create a Router object
r = Router(id=1, hostname="switch1", domain="example.com")

# Add an interface
iface = r.interface.add()   # matches 'repeated Interface interface = 4;'
iface.name = "GigabitEthernet0/1"
iface.description = "Uplink router"
iface.status = "shutdown"

# Add another interface
iface2 = r.interface.add()
iface2.name = "GigabitEthernet0/2"
iface2.description = "Downlink router"
iface2.status = "up"

# Print object (human-readable text format)
print("Router object:\n", r)

# Serialize to binary
binary_data = r.SerializeToString()
print("\nSerialized binary:\n", binary_data)

# Deserialize back
new_r = Router()
new_r.ParseFromString(binary_data)
print("\nDeserialized object:\n", new_r)
