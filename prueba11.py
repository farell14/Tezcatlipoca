import nmap
state=None
nmScan = nmap.PortScanner()
nmScan.scan('192.168.33.0/24', '0-1023')
for port in nmScan['192.168.33.0/24']['tcp']:
    thisDict = nmScan['192.168.33.0/24']['tcp'][port]
    print ('Port ' + str(port) + ': ' + thisDict['product'] + ', v' + thisDict['version'])
state=nmScan['192.168.33.0'].state()
print(state)