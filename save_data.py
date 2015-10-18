#! /usr/bin/python

import sys
import os
import json
import requests

#i would want company name, description, product description,  angel co page, company web page, founders urls, emplyees urls
#example: {u'hidden': True, u'abilities': {u'intro': {u'has': False, u'can': False}}, u'id': 863219}
TOKEN='e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6'

for line in sys.stdin.readlines():
    #print(line)
    #users = json.loads(line)
    print(line)
    try:
        user = json.loads(line)
        userid = user["id"]

        if not os.path.isfile("all_investors/" + str(user["id"])):
            #print(userid)
            r = requests.get('https://api.angel.co/1/users/%s/roles?&access_token=%s' % (str(userid), TOKEN)).json()
            if ("success" in r) and (r["success"] == False):
                print(r)
                continue

            user["mined_roles"] = r
            inv = open("all_investors/" + str(user["id"]), "w")
            inv.write(json.dumps(user))
            inv.close()

    except RuntimeError as e:
        print("skipping user %s" % e.strerror)
        next


#https://api.angel.co/1/users/1279157/roles?access_token=e0a8a70151e32cb2741c89218ea744526ad043af0afd9bf6
"""
{u'image': u'https://d1qb2nb5cznatu.cloudfront.net/users/191364-medium_jpg?1405523894', u'locations': [{u'angellist_url': u'https://angel.co/italy', u'tag_type': u'LocationTag', u'display_name': u'Italy', u'id': 2127, u'name': u'italy'}, {u'angellist_url': u'https://angel.co/barcelona', u'tag_type': u'LocationTag', u'display_name': u'Barcelona', u'id': 1853, u'name': u'barcelona'}], u'resume_url': u'https://www.linkedin.com/in/carlucciluca', u'id': 191364, u'angellist_url': u'https://angel.co/luca-bidaway-com', u'what_ive_built': u"I'm good", u'criteria': u'', u'follower_count': 684, u'skills': [{u'display_name': u'Strategy', u'name': u'strategy', u'level': 4.0, u'angellist_url': u'https://angel.co/strategy', u'id': 15552, u'tag_type': u'SkillTag'}, {u'display_name': u'Business Development', u'name': u'business development', u'level': 4.0, u'angellist_url': u'https://angel.co/business-development-1', u'id': 15525, u'tag_type': u'SkillTag'}, {u'display_name': u'Corporate Finance', u'name': u'corporate finance', u'level': 3.0, u'angellist_url': u'https://angel.co/corporate-finance', u'id': 36258, u'tag_type': u'SkillTag'}, {u'display_name': u'Entrepreneurship', u'name': u'entrepreneurship', u'level': 3.0, u'angellist_url': u'https://angel.co/entrepreneurship', u'id': 15745, u'tag_type': u'SkillTag'}, {u'display_name': u'Project Management', u'name': u'project management', u'level': 3.0, u'angellist_url': u'https://angel.co/project-management-1', u'id': 24003, u'tag_type': u'SkillTag'}], u'bio': u'Founder of @bidaway \u2022 Strong business and financial background (WTO, Cimolai Group, EDPR) \u2022 IESE MBA 2012', u'blog_url': u'', u'twitter_url': u'https://twitter.com/Gehnibo', u'facebook_url': u'', u'what_i_do': u'I have worked throughout Europe as diplomat at the WTO and as corporate financial manager leading teams and working on large projects before managing a holiday resort. As CEO at BidAway, I am in charge of product development and general management (legal, external relations, business development).', u'aboutme_url': u'', u'investor': True, u'name': u'Luca Carlucci', u'roles': [{u'angellist_url': u'https://angel.co/entrepreneur-1', u'tag_type': u'RoleTag', u'display_name': u'Entrepreneur', u'id': 14725, u'name': u'entrepreneur'}, {u'angellist_url': u'https://angel.co/product_manager', u'tag_type': u'RoleTag', u'display_name': u'Product Manager', u'id': 80487, u'name': u'product_manager'}], u'dribbble_url': u'', u'linkedin_url': u'http://www.linkedin.com/in/carlucciluca', u'github_url': u'', u'behance_url': u'', u'online_bio_url': u'http://www.bidaway.com/'}
"""

