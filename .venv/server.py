import grpc
from concurrent import futures
import network_pb2
import network_pb2_grpc

class InterfaceServiceServicer(network_pb2_grpc.InterfaceServiceServicer):
    def GetInterfaces(self, request, context):
        return network_pb2.InterfaceReply(status="up", mtu=1500)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_pb2_grpc.add_InterfaceServiceServicer_to_server(InterfaceServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
