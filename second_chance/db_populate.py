import django
django.setup()
from app.models import *
from django.contrib.auth.models import User


industries = ["Accounting / Finance / Insurance","Administrative / Clerical","Banking / Real Estate / Mortgage Professionals","Building Construction / Skilled Trades", "Business / Strategic Management","Creative / Design","Customer Support / Client Care","Editorial / Writing","Education / Training","Engineering","Food Services / Hospitality","Human Resources","IT / Software Development","Installation / Maintenance / Repair","Legal","Logistics / Transportation","Manufacturing / Production / Operations","Marketing / Product","Medical / Health","Other","Project / Program Management","Government/ Public Service","Non-profit/ Community","Sales / Retail / Business Development","Security / Protective Services"]


for industry in industries:
	print industry
	i = Industry(name = industry)
	i.save()

