import django
django.setup()
from app.models import *
from django.contrib.auth.models import User
import csv
import argparse



#to import employers and positions from a csv
#give the file as a command-line argument --positions path/to/file.csv


#if you get a django settings error, run the following in the shell:
#export DJANGO_SETTINGS_MODULE=second_chance.settings





parser = argparse.ArgumentParser()
parser.add_argument("--positions", dest="positions_csv",
                    help="csv of available positions")
args = parser.parse_args()



industries = ["Accounting / Finance / Insurance","Administrative / Clerical","Banking / Real Estate / Mortgage Professionals","Building Construction / Skilled Trades", "Business / Strategic Management","Creative / Design","Customer Support / Client Care","Editorial / Writing","Education / Training","Engineering","Food Services / Hospitality","Human Resources","IT / Software Development","Installation / Maintenance / Repair","Legal","Logistics / Transportation","Manufacturing / Production / Operations","Marketing / Product","Medical / Health","Other","Project / Program Management","Government/ Public Service","Non-profit/ Community","Sales / Retail / Business Development","Security / Protective Services"]

csv_industry_titles = ["Accounting","Administrative","Banking","Construction","Business","Creative","Customer Support","Editorial","Education","Engineering","Hospitality","Human Resources","Software","Maintenance","Legal","Logistics","Manufacturing","Marketing","Medical","Other","Project","Government","Non-profit","Sales","Security"]


for industry in industries:
    industry_set = Industry.objects.filter(name = industry)
    if len(industry_set) == 0:
        print industry
        i = Industry(name = industry)
        i.save()


if args.positions_csv is not None:
    #make dictionary of csv headers to industry objects to make them easier to add/find later
    industry_dict = {}
    for industry in csv_industry_titles:
        industry_dict[industry] = Industry.objects.filter(name__contains = industry).first()
    with open(args.positions_csv,'r') as positions_file:
        positions = csv.DictReader(positions_file)
        for p in positions:
            matching_employers = Employer.objects.filter(name = p["employer_name"][:100])
            if len(matching_employers) == 0:

                employer_dict = {"name" : p["employer_name"][:100],
                    "phone" : p["employer_phone"],
                    "email" : p["employer_email"],
                    "hq_address" : p["employer_hq_address"],
                    "hq_in_dc" : p["employer_hq_in_dc"],
                    "home_url" : p["employer_home_url"],
                    "employment_url" : p["employer_employment_url"],
                    "notes" : p["employer_notes"],
                    "box_present" : p["employer_box_present"],
                    "crime_type_asked" : p["employer_crime_type_asked"],
                    "years_specified_by_box" : p["employer_years_specified"]}
                non_null_dict = {}

                for k in employer_dict: #this loop removes blanks from the csv
                    if employer_dict[k] != "":
                        non_null_dict[k] = employer_dict[k]
                
                e = Employer(**non_null_dict)
                print p["employer_name"]
                e.save()
            else:
                e = matching_employers.first()
            for industry in csv_industry_titles:
                if p[industry] == "y":
                    e.industries.add(industry_dict[industry])
                    e.save()


            matching_positions = Position.objects.filter(title = p["position_title"][:100], employer = e)
            if len(matching_positions) == 0:
                position_dict = {"title" : p["position_title"][:100],
                        "phone" : p["position_phone"],
                        "worksite_location" : p["position_location"],
                        "job_posted" : p["job_posted"],
                        "collateral_sanction_applies" : p["collateral_sanction_applies"],
                        "which_collateral_sanction_applies" : p["which_collateral_sanction"]}
                non_null_pos_dict = {}

                for k in position_dict: #this loop removes blanks from the csv
                    if position_dict[k] != "":
                        non_null_pos_dict[k] = position_dict[k]

                p = Position(employer = e,**non_null_pos_dict)

                p.save()




else:
    print("no file of positions given, so no positions or employers populated")