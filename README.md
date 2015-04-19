Catch actions from myplantandme-server's TCP server and write (not append) a duration (in seconds) into a file.

Uses Python 2.7.

# Run

```
# myplantandme-server should be running
screen -S tcp-client -d -m python2.7 client.py

# run file readers
screen -S reader-lights -d -m python2.7 reader_lights.py
screen -S reader-fan -d -m python2.7 reader_fan.py
screen -S reader-water -d -m python2.7 reader_water.py
```

# Results of tcp client.py
- file `lights`
- file `fan`
- file `water`

Exemple of content:
`1800`
