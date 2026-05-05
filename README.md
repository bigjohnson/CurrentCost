# CurrentCost to linux host with influxdb and grafana

![CurrentCost](img/currentcost.jpg)

## Serial data RJ45 pinout
```
RJ45 pin 4 (gnd) to DB9 pin 5 (gnd) on my cable RED wire
RJ45 pin 7 (unit Rx) to DB9 pin 2 (Tx) on my cable GREEN wire
RJ45 pin 8 (unit Tx) to DB9 pin 3 (Rx) on my cable YELLOW wire
```
## Serial setup
```
Baudrate 57600 bps
Data bits 8
Parity none
Stop bits 1
No flow control
```
## Xml output
```
<msg><src>CC128-v1.44</src><dsb>00014</dsb><time>14:27:25</time><tmpr>24.6</tmpr><sensor>0</sensor><id>00077</id><type>1</type><ch1><watts>00749</watts></ch1></msg>
```
## run ./currentcost.py

real data on https://grafana.panu.it/d/adjqgcl/currencost?orgId=1&from=now-6h&to=now&timezone=browser&refresh=10s

