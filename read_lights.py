#!/bin/env pyhton2.7
from subprocess import call
import time

filename = 'lights'
call(['gpio', 'mode', '27', 'out'])

def enable():
    print 'enable'
    call(['gpio', 'write', '27', '1'])

def disable():
    print 'disable'
    call(['gpio', 'write', '27', '0'])

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
