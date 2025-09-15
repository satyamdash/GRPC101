import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    # Connect to Go server
    channel = grpc.insecure_channel("localhost:8080")
    stub = greeter_pb2_grpc.GreeterStub(channel)

    # Make request
    response = stub.SayHello(greeter_pb2.HelloRequest(name="Hey"))
    print("Greeting:", response.name)

    response = stub.SayNamaste(greeter_pb2.HelloRequest(name="Hey"))
    print("Greeting:", response.name)

if __name__ == "__main__":
    run()
