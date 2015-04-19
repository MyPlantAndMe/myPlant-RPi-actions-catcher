#!/bin/env pyhton2.7
from subprocess import call
import time

filename = 'lights'

def enable():
    print 'enable'
    with open('/dev/pi-blaster', 'w') as outfile:
        call(['echo', '25=1'], stdout=outfile)

def disable():
    print 'disable'
    with open('/dev/pi-blaster', 'w') as outfile:
        call(['echo', '25=0'], stdout=outfile)

def wait(seconds):
    print 'wait ' + str(seconds) + ' seconds'
    time.sleep(seconds)

def main():
    with open(filename, 'r') as f:
        data = f.read()

    if (data):
        duration = int(data)
        enable()
        wait(duration)
        disable()

while True:
    main()
