#!/bin/env pyhton2.7
from subprocess import call
import time

filename = 'lights'

def enable():
    print 'enable'
    call(['ls', '-l'])

def disable():
    print 'disable'
    call(['ls', '-c'])

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
