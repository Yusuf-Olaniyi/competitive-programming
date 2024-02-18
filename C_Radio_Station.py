n,m = map(int,input().split())

ip_name = {}
while n > 0:
    name,ip = map(str,input().split())

    ip_name[ip] = name
    n -= 1

ip_command = {}

while m > 0:
    command,ip =  map(str,input().split())
    ip = ip.replace(';','')
    print(f'{command} {ip}; #{ip_name[ip]}')
    
    m -= 1


        
