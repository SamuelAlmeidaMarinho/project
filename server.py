#! /usr/bin/python

import camera_pb2
import requests

def getImage():
    width = '1280'
    height = '720'
    hostname = '10.10.0.24'
    url = 'http://'+hostname+'/axis-cgi/jpg/image.cgi?resolution='+width+'x'+height
    image = requests.get(url).content
    file=open("capture.jpg",'wb')
    file.write(image)
    file.close()

getImage()

'''
image = camera_pb2.image()

in_file = open('capture.jpg', 'rb')
image.content = in_file.read()
in_file.close()

out_file = open("out-file", "wb")
out_file.write(image.content)
out_file.close()
'''