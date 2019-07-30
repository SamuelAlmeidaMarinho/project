#! /usr/bin/python

import grpc
import camera_pb2
import camera_pb2_grpc
import requests

import time
from concurrent import futures

def getImageAxis():
    width = '1280'
    height = '720'
    hostname = '10.10.0.24'
    url = 'http://'+hostname+'/axis-cgi/jpg/image.cgi?resolution='+width+'x'+height
    image = requests.get(url).content
    return image

class imageStreamServicer(camera_pb2_grpc.imageStreamServicer):
    def getImage(self, request, context):
        response = camera_pb2.image()
        response.width = 1280
        response.height = 720
        response.imageData = getImageAxis()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
camera_pb2_grpc.add_imageStreamServicer_to_server(imageStreamServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

'''
image = camera_pb2.image()

in_file = open('capture.jpg', 'rb')
image.content = in_file.read()
in_file.close()

out_file = open("out-file", "wb")
out_file.write(image.content)
out_file.close()
'''