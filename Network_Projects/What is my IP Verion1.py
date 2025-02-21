file =open(r'C:\Users\rajatx\Documents\python\ip.txt',"a+")
file.seek(0)
content = file.read()
_ipaddress = content.split("ipAddress")[1].splitlines()
_ipaddress = _ipaddress[0]
print(type(_ipaddress))
#print(_ipaddress)
_ipaddress =_ipaddress.split('"')[2]
print(_ipaddress)
# _ipaddress =_ipaddress.split('value="')[1][0:13]
# print(_ipaddress)
