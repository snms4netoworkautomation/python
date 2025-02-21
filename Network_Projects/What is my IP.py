import requests

# Fetch IP information
result = requests.get('https://ipinfo.io/json').text
# Keyword to search for
_matchip = '"ip":'
_matchcity = '"city":'

for line in result.splitlines():
    if _matchcity in line or _matchip in line:
        a = (line.removesuffix(','))
        b = (line.removeprefix('"'))
        #print(a,"\n", b)
        c = []
        c.append(a)
        #print(c)
        t =tuple(c)
        print(t)
