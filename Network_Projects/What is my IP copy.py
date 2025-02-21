import requests

# Fetch IP information
result = requests.get('https://ipinfo.io/json').text

# Keyword to search for
_matchip = '"ip":'
_matchcity = '"city":'


# Split the result into lines and search for the match
for line in result.splitlines():
    if _matchip in line:  # Check if the line contains the keyword
        print(line)
    if _matchcity in line: # Check if the line contains the keyword City
        print(line.replace(",",""))