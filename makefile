generate:
	protoc --proto_path=. proto/greeter.proto --go_out=. --go-grpc_out=. 
