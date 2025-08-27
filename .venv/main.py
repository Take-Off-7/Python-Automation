import grpc
import network_pb2
import network_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = network_pb2_grpc.InterfaceServiceStub(channel)

response = stub.GetInterfaces(network_pb2.InterfaceRequest(name="GigabitEthernet1"))
print(f"Status: {response.status}, MTU: {response.mtu}")
