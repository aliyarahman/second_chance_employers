import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import csv

import api_keys #a python file where api keys are stored.
#in .gitignore so the keys aren't public.

#this API returns xml

base_url = "http://api.us.jobs/?key="+api_keys.USA_JOBS_KEY


#they won't let me do a super broad search so I'm going to loop
#through keywords




job_ids = []
job_fields = ["employer_name",
    "employer_phone",
    "employer_email",
    "employer_hq_address",
    "employer_hq_in_dc",
    "employer_home_url",
    "employer_employment_url",
    "employer_notes",
    "employer_box_present",
    "employer_crime_type_asked",
    "employer_years_specified",
    "Accounting",
    "Administrative",
    "Banking",
    "Construction",
    "Business",
    "Creative",
    "Customer Support",
    "Editorial",
    "Education",
    "Engineering",
    "Hospitality",
    "Human Resources",
    "Software",
    "Maintenance",
    "Legal",
    "Logistics",
    "Manufacturing",
    "Marketing",
    "Medical",
    "Other",
    "Project",
    "Government",
    "Non-profit",
    "Sales",
    "Security",
    "position_title",
    "position_phone",
    "position_location",
    "job_posted",
    "collateral_sanction_applies",
    "which_collateral_sanction"]


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



with open("positions.csv","a") as positions:
    writer = csv.DictWriter(positions,fieldnames = job_fields)
    writer.writeheader()
    i = 0
    for j in job_ids:
        if i % 100 == 0:
            print i
        i += 1
        job_dict = {}
        r = requests.get("%s&jvid=%s" % (base_url, j))
        soup = BeautifulSoup(r.text)
        job_dict["employer_name"] = soup.job.company.text
        job_dict["position_title"] = soup.job.company.text
        job_dict["position_location"] = soup.job.location.text
        job_dict["job_posted"] = soup.job.url.text
        description = soup.job.description.text

        if "Accounting".lower() in description.lower():
            job_dict["Accounting"]="y"
        if "Finance".lower() in description.lower():
            job_dict["Accounting"]="y"
        if "Insurance".lower() in description.lower():
            job_dict["Accounting"]="y"
        if "Administrative".lower() in description.lower():
            job_dict["Administrative"]="y"
        if "Clerical".lower() in description.lower():
            job_dict["Administrative"]="y"
        if "Banking".lower() in description.lower():
            job_dict["Banking"]="y"
        if "Real Estate".lower() in description.lower():
            job_dict["Banking"]="y"
        if "Mortgage".lower() in description.lower():
            job_dict["Banking"]="y"
        if "Building".lower() in description.lower():
            job_dict["Construction"]="y"
        if "Construction".lower() in description.lower():
            job_dict["Construction"]="y"
        if "Business".lower() in description.lower():
            job_dict["Business"]="y"
        if "Strategic Management".lower() in description.lower():
            job_dict["Business"]="y"
        if "Customer Support".lower() in description.lower():
            job_dict["Customer Support"]="y"
        if "Client Care".lower() in description.lower():
            job_dict["Customer Support"]="y"
        if "Editorial".lower() in description.lower():
            job_dict["Editorial"]="y"
        if "Education".lower() in description.lower():
            job_dict["Education"]="y"
        if "Training".lower() in description.lower():
            job_dict["Education"]="y"
        if "Engineer".lower() in description.lower():
            job_dict["Engineering"]="y"
        if "Food Services".lower() in description.lower():
            job_dict["Hospitality"]="y"
        if "Hospitality".lower() in description.lower():
            job_dict["Hospitality"]="y"
        if "Human Resources".lower() in description.lower():
            job_dict["Human Resources"]="y"
        if "Technology".lower() in description.lower():
            job_dict["Software"]="y"
        if "Software Development".lower() in description.lower():
            job_dict["Software"]="y"
        if "Installation".lower() in description.lower():
            job_dict["Maintenance"]="y"
        if "Maintenance".lower() in description.lower():
            job_dict["Maintenance"]="y"
        if "Repair".lower() in description.lower():
            job_dict["Maintenance"]="y"
        if "Legal".lower() in description.lower():
            job_dict["Legal"]="y"
        if "Logistics".lower() in description.lower():
            job_dict["Logistics"]="y"
        if "Transportation".lower() in description.lower():
            job_dict["Logistics"]="y"
        if "Manufacturing".lower() in description.lower():
            job_dict["Manufacturing"]="y"
        if "Production".lower() in description.lower():
            job_dict["Manufacturing"]="y"
        if "Operations".lower() in description.lower():
            job_dict["Manufacturing"]="y"
        if "Marketing".lower() in description.lower():
            job_dict["Marketing"]="y"
        if "Medical".lower() in description.lower():
            job_dict["Medical"]="y"
        if "Health".lower() in description.lower():
            job_dict["Medical"]="y"
        if "Project Manage".lower() in description.lower():
            job_dict["Project"]="y"
        if "Program Manage".lower() in description.lower():
            job_dict["Project"]="y"
        if "Government".lower() in description.lower():
            job_dict["Government"]="y"
        if "Public Service".lower() in description.lower():
            job_dict["Government"]="y"
        if "Non-profit".lower() in description.lower():
            job_dict["Non-profit"]="y"
        if "Sales".lower() in description.lower():
            job_dict["Sales"]="y"
        if "Retail".lower() in description.lower():
            job_dict["Sales"]="y"
        if "Business Development".lower() in description.lower():
            job_dict["Sales"]="y"
        if "Security".lower() in description.lower():
            job_dict["Security"]="y"
        if "Protective Services".lower() in description.lower():
            job_dict["Security"]="y"

        if "criminal" in description.lower() or "background check" in description.lower():
            #put this in notes
            job_dict["employer_notes"] = "background check"

        writer.writerow(job_dict)