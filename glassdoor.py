import requests
import json
import socket
import api_keys

ipaddr = socket.gethostbyname(socket.gethostname() #getting my ip addr
uagent = 'Mozilla/5.0' #arbitrary user agent 
query = 'glasses' #random query hardcoded for now

urlparams = {'t.p': api_keys.GLASSDOOR_ID, 't.k': api_keys.GLASSDOOR_KEY, 'userip': ipaddr, 'useragent': uagent , 'format': 'json', 'v': '1', 'action': 'employers', 'q': query, }


q = requests.get("http://api.glassdoor.com/api/api.htm", params=urlparams)
print(q.url)

#q.json()
#above command getting an exception when run
