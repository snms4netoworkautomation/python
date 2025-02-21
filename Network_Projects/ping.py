from ping3 import ping

iplist = ["youtube.com","google.com","4.4.4.4"]

for i in iplist:
    respone = ping(i,timeout=2)
    print(i,respone*1000)
    