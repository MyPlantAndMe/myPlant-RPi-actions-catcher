#!/bin/env python2.7
import socket
import json
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 3100))

def write(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def readJson(bytes):
    return json.loads(bytes.decode('utf8'))

def receiveJson():
    return readJson(sock.recv(4096))

def dispatch(sensor, duration):
    if (sensor in ['lights', 'fan', 'water']):
        write(sensor, duration)
    else:
        print 'Invalid sensor name: ' + sensor

def main():
    response = receiveJson()
    duration = response.get('duration')
    sensor = response.get('sensor')
    dispatch(sensor, duration)

while True:
    main()
