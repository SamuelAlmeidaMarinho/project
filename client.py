import grpc
import camera_pb2
import camera_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = camera_pb2_grpc.imageStreamStub(channel)
request = camera_pb2.subscribeRequest()
response = stub.getImage(request)

out_file = open("out-file", "wb")
out_file.write(response.imageData)
out_file.close()