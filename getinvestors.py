#! /usr/bin/python

import requests
#import pymongo
import json
import os

#  /tags/:id/startups

# 1. Get a list of healhcare startups and save to the database
# 2. Enrich the database with startup's details
#http://api.angel.co/1/users/155?

TOKEN='e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6'

"""
Redirect URI http://angelrob.herokuapp.com/callback
Main URI http://angelrob.herokuapp.com
Client ID af88132a9056cda095cf4d8ccd2fea4704bea38c1b69a136
Your Token e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6
"""
health_tags =  [{"id":13,"pic":"/images/icons/market.png","url":"https://angel.co/health-care","name":"Health Care","type":"MarketTag"},{"id":1103,"pic":"/images/icons/market.png","url":"https://angel.co/health-and-wellness","name":"Health and Wellness","type":"MarketTag"},{"id":175,"pic":"/images/icons/market.png","url":"https://angel.co/health-care-information-technology","name":"Health Care Information Technology","type":"MarketTag"},{"id":418,"pic":"/images/icons/market.png","url":"https://angel.co/personal-health","name":"Personal Health","type":"MarketTag"},{"id":1258,"pic":"/images/icons/market.png","url":"https://angel.co/mobile-health","name":"Mobile Health","type":"MarketTag"},{"id":107,"pic":"/images/icons/market.png","url":"https://angel.co/fitness","name":"Fitness","type":"MarketTag"},{"id":9826,"pic":"/images/icons/market.png","url":"https://angel.co/healthcare-services","name":"Healthcare Services","type":"MarketTag"},{"id":151649,"pic":"/images/icons/market.png","url":"https://angel.co/digital-health-3","name":"Digital Health","type":"MarketTag"},{"id":10783,"pic":"/images/icons/market.png","url":"https://angel.co/health-and-insurance","name":"Health and Insurance","type":"MarketTag"},{"id":2594,"pic":"/images/icons/market.png","url":"https://angel.co/senior-health","name":"Senior Health","type":"MarketTag"},{"id":157621,"pic":"/images/icons/market.png","url":"https://angel.co/mental-health-3","name":"Mental Health","type":"MarketTag"},{"id":111311,"pic":"/images/icons/market.png","url":"https://angel.co/electronic-health-records-1","name":"Electronic Health Records","type":"MarketTag"},{"id":8550,"pic":"/images/icons/market.png","url":"https://angel.co/mobile-emergency-health","name":"Mobile Emergency&Health","type":"MarketTag"},{"id":155631,"pic":"/images/icons/market.png","url":"https://angel.co/health-and-safety","name":"Health And Safety","type":"MarketTag"},{"id":152515,"pic":"/images/icons/market.png","url":"https://angel.co/health-care-services-2","name":"Health Care Services","type":"MarketTag"},{"id":154783,"pic":"/images/icons/market.png","url":"https://angel.co/healthy-eating","name":"Healthy Eating","type":"MarketTag"},{"id":154030,"pic":"/images/icons/market.png","url":"https://angel.co/brain-health","name":"Brain Health","type":"MarketTag"},{"id":154571,"pic":"/images/icons/market.png","url":"https://angel.co/health-foods","name":"Health Foods","type":"MarketTag"},{"id":158190,"pic":"/images/icons/market.png","url":"https://angel.co/ambulatory-and-acute-healthcare","name":"Ambulatory And Acute Healthcare ","type":"MarketTag"},{"id":154033,"pic":"/images/icons/market.png","url":"https://angel.co/quantified-health","name":"Quantified Health","type":"MarketTag"}]

#https://api.angel.co/1/tags/1/users?iinclude_details=investor&investors=by_activity&page=2&access_token=e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6


for tag in range(2,10000):
    print(tag)
    r = requests.get('https://api.angel.co/1/tags/%s/users?&access_token=%s' % (str(tag), TOKEN)).json()
    #print(r["success"])
    if ("success" in r) and (r["success"] == False):
        print(r)
        print("Passing\n")
        continue
    print(json.dumps(r))
    last_page = r["last_page"]
    if not os.path.isdir("user-" + str(tag)):
        os.mkdir("user-" + str(tag))
    for page in range(1, last_page):
        print(page)
        if not os.path.isfile("user-" + str(tag) + "/" + str(page)):
            r = requests.get('https://api.angel.co/1/tags/%s/users?&page=%s&access_token=%s' % (tag, page, TOKEN)).json()
            f = open("user-" + str(tag) + "/" + str(page), "w")
            f.write(json.dumps(r))
            f.write("\n")
            f.close()
        else:
           print("File exists, skipping!")


