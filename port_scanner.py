import socket,sys,argparse,textwrap


default_list = [15,17,18,18,19,19,21,22,23,25,80,81,123,389,443,636,989,990,1433,1499,2022,2122,2222,2375,2376,2380,2480,2483,2484,2638,3000,3001,3020,3306,3389,3389,3500,3999,4000,4100,4200,4243,4244,4444,4500,4505,4506,5000,5001,5004,5005,5037,5432,5500,5601,5666,5667,5672,5800,5900,5984,5999,6000,6082,6379,6653,6660,6661,6662,6663,6664,6665,6666,6667,6668,6669,6888,6888,7474,7777,8000,8001,8002,8005,8008,8080,8089,8081,8123,8139,8140,8172,8222,8333,8443,8889,8983,8999,9000,9001,9006,9042,9050,9051,9092,9200,9500,9800,9999,10050,10051,11211,11214,11215,15672,18091,18092,27017,27018,27019,28015,29015,33848,35357]


def scan(port,ip_address):
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    number = conn.connect_ex((ip_address,int(port)))
    if number == 0:
        print(f"Open: {port}")
    else:
        pass    

def main():
    parser = argparse.ArgumentParser(description="This is a full tcp port scanner",epilog=textwrap.dedent('''
    Note: Don't type giberish or it will just quit
    Usage: {sys.argv[0]} <ip> <port or port-range(optional)>
    Example:{sys.argv[0]} -ip www.website.com -d
    Example:{sys.argv[0]} -ip 192.168.0.2 -d
    Example:{sys.argv[0]} -ip 192.168.0.2 -p 1-100
    Example:{sys.argv[0]} -ip 192.168.0.2 -p 1,4,10,44,80,100,443
    Example:{sys.argv[0]} -ip 192.168.0.2 -p 80
    '''),formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-ip','--ip_address',help="IP adddress of the machine")
    parser.add_argument('-p','--ports',help="Port,range of ports to scan")
    parser.add_argument('-d','--default',help="Scan default list of ports",action="store_true")
    options = parser.parse_args()
    ports = options.ports

    if not options.ip_address and (not ports or not options.default):
        print(f"Use:{sys.argv[0]} -h for usage")
        sys.exit(0)
      

    try:
        if ports:
            if '-' in options.ports:
                low_port = int((ports.split('-'))[0])
                high_port = int((ports.split('-'))[1])
                for port in range(low_port,high_port):
                    scan(port,options.ip_address)
                
            elif ',' in sys.argv[2]:
                port_list = sys.argv[2].split(',')
                for port in port_list:
                    scan(int(port,options.ip_address))

            else:
                scan(ports,options.ip_address)


        elif options.default:
            print("[*]Scanning ports from default list")
            for port in default_list:
                scan(port,options.ip_address)
    except Exception as e:
        print(f"[-]Error: {e}")               

    
main()
     



