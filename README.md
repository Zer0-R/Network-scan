# Network-scan
## Utility: Displays the machines connected to the network on which you are connected.
## Checked: Kali Linux and Windows 10
## Language used: Python 2.7.13
## Library used: scapy and threading

### Usage
```
Zer0Scan.py HOST
-t --timeout: how much time to wait after the last packet has been send (default: 15).
```

### Example 1
input: 
```
Zer0Scan.py 192.168.0.0/24
```
output:
```
Send pings from 192.168.0.0 to 192.168.0.255...

Result:
192.168.0.39
192.168.0.254

Zer0Scan done: 256 IP addresses (2 hosts up) scanned
```
### Example 2
input:
```
Zer0Scan.py 192.168.0.10-40 -t 5
```
output:
```
Send pings from 192.168.0.10 to 192.168.0.40...

Result:
192.168.0.39

Zer0Scan done: 31 IP addresses (1 hosts up) scanned
```
### Example 3
input:
```
Zer0Scan.py 192.168.0.200-192.168.1.200,192.168.0.50
```
output:
```
Send pings from 192.168.0.200 to 192.168.1.200...

Result:
192.168.0.254

Send ping to 192.168.0.50...

Result:

Zer0Scan done: 258 IP addresses (1 hosts up) scanned
```
