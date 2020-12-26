import socket
from IPy import IP
import pandas as pd
# ipaddress = input('[+] enter target to scan: ')
# port = 22

def scanPort(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print(f'[+] Port {port} is Open')
    except:
        print(f'[-] Port {port} is closed') 

append = []
def commonPorts(ipaddress):
    df = pd.read_csv('common-port-numbers.csv')
    for port,protocol in zip(list(df.number), list(df.assignment)):
        with open(ipaddress) as ipadd:
            for ip in ipadd:
                try:
                    sock = socket.socket()
                    sock.settimeout(0.5)
                    sock.connect((ip, port))
                    append.append({'IPAddress': ip, 'Protocole': protocol, 'Port': port, 'State': 'opened'})
                    # print(f'[+] IP address {ip} with the Protocole {protocol} and Port number {port} is Opened')
                except:
                    append.append({'IPAddress': ip, 'Protocole': protocol, 'Port': port, 'State': 'closed'})
                    # print(f'[-] IP address {ip} with the Protocole {protocol} and Port number {port} is closed')  
    OutPut = pd.DataFrame(append)
    OutPut.to_html('PortsStates.html')
    OutPut.to_csv('PortsStates.csv')


commonPorts('ipAddresses.txt')                