#!/bin/env pyhton2.7
from subprocess import call
import time

filename = 'lights'

def enable():
    print 'enable'
    call(['gpio', '1'])

def disable():
    print 'disable'
    call(['gpio', '0'])

def wait(seconds):
    print 'wait ' + seconds + ' seconds'
    time.sleep(duration)

def main():
    with open(filename, 'r') as f:
        data = f.read()

    duration = int(data)
    enable()
    wait(duration)
    disable()

while True:
    main()
