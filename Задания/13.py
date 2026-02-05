'''from ipaddress import*
net=ip_network('10.100.202.34/255.255.240.0',0)
for ip in net:
    if bin(int(ip))[2:].count('1')%5==0:
        print (ip)
        break'''
##########################################################