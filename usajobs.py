import requests
import api_keys
from bs4 import BeautifulSoup

import api_keys

#this API returns xml

base_url = "http://api.us.jobs/?key="+api_keys.USA_JOBS_KEY


#they won't let me do a super broad search so I'm going to loop
#through keywords

#todo find keywords
keywords = ["sales"]


job_ids = []
for k in keywords:
	r = requests.get("%s&kw=%s" % (base_url, k))
	#todo: deal with pagination

	soup = BeautifulSoup(r.text)
	jobs = soup.find_all("job")
	for j in jobs:
		job_ids.append(j.jvid.text)


#todo: go through all of the job ids and look at the description





