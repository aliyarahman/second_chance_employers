import requests
import api_keys
from bs4 import BeautifulSoup
from collections import defaultdict

import api_keys

#this API returns xml

base_url = "http://api.us.jobs/?key="+api_keys.USA_JOBS_KEY


#they won't let me do a super broad search so I'm going to loop
#through keywords




job_ids = []

recordcount = 1
start = 11500 #should be zero, set to something higher for faster debugging
while recordcount > 0:

    r = requests.get("%s&zc1=DC&rd1=100&rs=%d&re=%d" % (base_url, start, start+500))
    #todo: deal with pagination

    soup = BeautifulSoup(r.text)
    jobs = soup.find_all("job")

    for j in jobs:
        print j.company.text
        job_ids.append(j.jvid.text)

    recordcount = int(soup.recordcount.text)
    start += 500


company_status = {}
company_description = defaultdict(list)
#todo: go through all of the job ids and look at the description
for j in job_ids:
    r = requests.get("%s&jvid=%s" % (base_url, j))
    soup = BeautifulSoup(r.text)
    company = soup.job.company.text
    description = soup.job.description.text
    if "felon" in description or "convict" in description or "criminal" in description:
        company_status[company] = "Bad"
    else:
        company_status[company] = "Not mentioned"

    company_description[company].append(description)






