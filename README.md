Catch actions from myplantandme-server's TCP server and write (not append) a duration (in seconds) into a file.

Uses Python 2.7.

# Run

```
# create fifo's (we cannot include them into git)
mkfifo lights fan water

# myplantandme-server should be running
screen -S tcp-client -d -m python2.7 client.py

# run file readers
screen -S reader-lights -d -m python2.7 reader_lights.py
screen -S reader-fan -d -m python2.7 reader_fan.py
screen -S reader-water -d -m python2.7 reader_water.py
```

The TCP client `client.py`
- write a duration (seconds) into fifo `lights`
- write a duration (seconds)  into fifo `fan`
- wirite a duration (seconds) into fifo `water`

A reader read (and block until a content) each a fifo, run a command to enable the device, wait the given number of seconds then run a command to disable the device.
