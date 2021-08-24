import nmap
import os

nmapScan = nmap.PortScanner()

print('#'*45)
print("    Python Network Mapper - made by Nem")
print('#'*45)

print('-'*45)
scan_ip = input("Input the IP you want to scan: ")
print('-'*45)
scan = nmapScan.scan(scan_ip)
print(scan)

input("\nPress enter to exit.")
