#! /usr/bin/python

import requests

#  /tags/:id/startups

# 1. Get a list of healhcare startups and save to the database
# 2. Enrich the database with startup's details
#http://api.angel.co/1/users/155?

#r = requests.get('https://api.angel.co/1tags/health-care/startups?access_token=e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6')
r = requests.get('https://api.angel.co/1/search?query=health-care&type=Startup&page=2&access_token=e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6').json()
#https://api.angel.co/1/tags/269/startups?access_token=e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6
print(r)
"""
print(r.text)
print(r.content)
print(r.headers)
print(dir(r))
"""
"""
Redirect URI http://angelrob.herokuapp.com/callback
Main URI http://angelrob.herokuapp.com
Client ID af88132a9056cda095cf4d8ccd2fea4704bea38c1b69a136
Your Token e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6
"""
"""
[{"id":13,"pic":"/images/icons/market.png","url":"https://angel.co/health-care","name":"Health Care","type":"MarketTag"},{"id":1103,"pic":"/images/icons/market.png","url":"https://angel.co/health-and-wellness","name":"Health and Wellness","type":"MarketTag"},{"id":175,"pic":"/images/icons/market.png","url":"https://angel.co/health-care-information-technology","name":"Health Care Information Technology","type":"MarketTag"},{"id":418,"pic":"/images/icons/market.png","url":"https://angel.co/personal-health","name":"Personal Health","type":"MarketTag"},{"id":1258,"pic":"/images/icons/market.png","url":"https://angel.co/mobile-health","name":"Mobile Health","type":"MarketTag"},{"id":107,"pic":"/images/icons/market.png","url":"https://angel.co/fitness","name":"Fitness","type":"MarketTag"},{"id":9826,"pic":"/images/icons/market.png","url":"https://angel.co/healthcare-services","name":"Healthcare Services","type":"MarketTag"},{"id":151649,"pic":"/images/icons/market.png","url":"https://angel.co/digital-health-3","name":"Digital Health","type":"MarketTag"},{"id":10783,"pic":"/images/icons/market.png","url":"https://angel.co/health-and-insurance","name":"Health and Insurance","type":"MarketTag"},{"id":2594,"pic":"/images/icons/market.png","url":"https://angel.co/senior-health","name":"Senior Health","type":"MarketTag"},{"id":157621,"pic":"/images/icons/market.png","url":"https://angel.co/mental-health-3","name":"Mental Health","type":"MarketTag"},{"id":111311,"pic":"/images/icons/market.png","url":"https://angel.co/electronic-health-records-1","name":"Electronic Health Records","type":"MarketTag"},{"id":8550,"pic":"/images/icons/market.png","url":"https://angel.co/mobile-emergency-health","name":"Mobile Emergency&Health","type":"MarketTag"},{"id":155631,"pic":"/images/icons/market.png","url":"https://angel.co/health-and-safety","name":"Health And Safety","type":"MarketTag"},{"id":152515,"pic":"/images/icons/market.png","url":"https://angel.co/health-care-services-2","name":"Health Care Services","type":"MarketTag"},{"id":154783,"pic":"/images/icons/market.png","url":"https://angel.co/healthy-eating","name":"Healthy Eating","type":"MarketTag"},{"id":154030,"pic":"/images/icons/market.png","url":"https://angel.co/brain-health","name":"Brain Health","type":"MarketTag"},{"id":154571,"pic":"/images/icons/market.png","url":"https://angel.co/health-foods","name":"Health Foods","type":"MarketTag"},{"id":158190,"pic":"/images/icons/market.png","url":"https://angel.co/ambulatory-and-acute-healthcare","name":"Ambulatory And Acute Healthcare ","type":"MarketTag"},{"id":154033,"pic":"/images/icons/market.png","url":"https://angel.co/quantified-health","name":"Quantified Health","type":"MarketTag"}]
"""
