import subprocess
import pandas as pd
def scan_ips(ips):
    df = pd.read_csv(ips)
    for i in list(df['ip']):
        subprocess.run(["nmap", i])

# scan_ips('ipAddresses.txt')

def scan_ip_ports(interval,ips, output):
    df = pd.read_csv(ips)
    for i in list(df['ip']):
        subprocess.run(["nmap", "-p", interval, i])
    if 'closed' in output:
        for i in list(output):
            print(i)
# scan_ip_ports("1-23", 'ipAddresses.txt', 'portscan.txt')

def connect_remotely(output, port, state, service, ip, usrname):
    doc = open(str(output)).read()
    if (port in doc) and (state in doc) and (service in doc):
        print(f'the port {str(port)}, and its state is {str(state)}')
        if state == 'open' and service == 'ftp':            
            subprocess.run(["ftp", ip])
        if state == 'open' and service == 'ssh':
            subprocess.run(["ssh",str(usrname)+ '@' + str(ip)])
        if state == 'open' and service == 'telnet':
            subprocess.run(["telnet", ip])

# connect_remotely('portscan.txt', '23', 'open', 'telnet', '192.168.137.136', '')

def files_transaction(folder, usrname, ip, path):
    subprocess.run(["scp", str(folder) + '/*' + str(usrname) + '@' + str(ip) + ':' + str(path)])
# files_transaction('filetransactions', 'ubuntu', '192.168.137.128', '/home/ubuntu/Documents/')



def host_discovery():
    print(ok)