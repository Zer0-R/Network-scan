
# Network Scan
## Utility: 
Displays the machines connected to the network on which you are connected

## Use:
Python 2.7.13

module scapy (for version 1.x)

## Target:
multiplatform

## Version 1.x: 
Use the ICMP protocol to send "Echo Reply" messages in Python 2.7.13

### Usage:
```
Zer0ScanV1.py HOST
```

### Example 1
input: 
```
Zer0ScanV1.py 192.168.0.0/24 -t 0.5
```
output:
```
Send pings from 192.168.0.0 to 192.168.0.255...

Result:
192.168.0.39
192.168.0.254

Zer0Scan 1.2 done: 256 IP addresses (2 hosts up) scanned
```
### Example 2
input:
```
Zer0ScanV1.py 192.168.0.10-40
```
output:
```
Send pings from 192.168.0.10 to 192.168.0.40...

Result:
192.168.0.39

Zer0Scan 1.2 done: 31 IP addresses (1 hosts up) scanned
```
### Example 3
input:
```
Zer0ScanV1.py 192.168.0.200-192.168.1.200,192.168.0.50
```
output:
```
Send pings from 192.168.0.200 to 192.168.1.200...

Result:
192.168.0.254

Send ping to 192.168.0.50...

Result:

Zer0Scan 1.2 done: 258 IP addresses (1 hosts up) scanned
```

## Version 2.x: 
Trying to connect to a socket at a remote address in Python 3.6.2

### Usage:
```
Zer0ScanV2.py HOST
```

### Example 1
input: 
```
Zer0ScanV2.py 192.168.0.0/24 -p 21
```
output:
```
Send pings from 192.168.0.0 to 192.168.0.255...

Result:
192.168.0.5: DESKTOP-DVLFVVE
192.168.0.39
192.168.0.254: FREEBOX

Zer0Scan 2.0 done: 256 IP addresses (2 hosts up) scanned
```
### Example 2
input:
```
Zer0ScanV2.py 192.168.0.10-40
```
output:
```
Send pings from 192.168.0.10 to 192.168.0.40...

Result:
192.168.0.39

Zer0Scan 2.0 done: 31 IP addresses (1 hosts up) scanned
```
### Example 3
input:
```
Zer0ScanV2.py 192.168.0.200-192.168.1.200,192.168.0.50
```
output:
```
Send pings from 192.168.0.200 to 192.168.1.200...

Result:
192.168.0.254: FREEBOX

Send ping to 192.168.0.50...

Result:

Zer0Scan 2.0 done: 258 IP addresses (1 hosts up) scanned
```
