#! /usr/bin/python

import sys
import json

#i would want company name, description, product description,  angel co page, company web page, founders urls, emplyees urls
#example: {u'hidden': True, u'abilities': {u'intro': {u'has': False, u'can': False}}, u'id': 863219}
"""
{u'community_profile': False, u'abilities': {u'intro': {u'has': False, u'can': False}}, u'crunchbase_url': None, u'video_url': None, u'company_url': u'http://www.harleyscosmeticclinic.co.in', u'company_type': [], u'locations': [{u'angellist_url': u'https://angel.co/mumbai', u'tag_type': u'LocationTag', u'display_name': u'Mumbai', u'id': 22939, u'name': u'mumbai'}], u'screenshots': [], u'id': 863198, u'angellist_url': u'https://angel.co/harleys-clinic', u'quality': 1, u'follower_count': 1, u'hidden': False, u'logo_url': u'https://d1qb2nb5cznatu.cloudfront.net/startups/i/863198-76e851a9d7582242bedc7887d18e47c7-medium_jpg.jpg?buster=1444032995', u'markets': [{u'angellist_url': u'https://angel.co/cosmetic-surgery-1', u'tag_type': u'MarketTag', u'display_name': u'Cosmetic Surgery', u'id': 92439, u'name': u'cosmetic surgery'}], u'status': None, u'product_desc': u"We specialize only in cosmetic surgeries at Harley Street. Our sole purpose is to offer you the highest quality of services. Cosmetic surgery is a full-time job. We say this because you would expect specialization of procedures which result in greater proficiency, expertise and ability. No matter what procedure you're interested in, you can be sure that we have the expertise, and the talent to give you the beautiful, natural-looking results you want.", u'twitter_url': None, u'high_concept': u'Best Cosmetic Surgeon in Mumbai', u'facebook_url': None, u'updated_at': u'2015-10-05T08:16:40Z', u'thumb_url': u'https://d1qb2nb5cznatu.cloudfront.net/startups/i/863198-76e851a9d7582242bedc7887d18e47c7-thumb_jpg.jpg?buster=1444032995', u'company_size': None, u'name': u'Harleys Clinic', u'created_at': u'2015-10-05T08:16:40Z', u'linkedin_url': None, u'blog_url': None}
"""

for line in sys.stdin.readlines():
    print(line)
    try:
        startups = json.loads(line)
        for startup in startups["startups"]:
            print(startup)  
        print("loaded...strtp")
    except:
       print("skipping startup") 
