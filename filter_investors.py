#! /usr/bin/python

import sys
import json

#i would want company name, description, product description,  angel co page, company web page, founders urls, emplyees urls
#example: {u'hidden': True, u'abilities': {u'intro': {u'has': False, u'can': False}}, u'id': 863219}
"""
{u'community_profile': False, u'abilities': {u'intro': {u'has': False, u'can': False}}, u'crunchbase_url': None, u'video_url': None, u'company_url': u'http://www.harleyscosmeticclinic.co.in', u'company_type': [], u'locations': [{u'angellist_url': u'https://angel.co/mumbai', u'tag_type': u'LocationTag', u'display_name': u'Mumbai', u'id': 22939, u'name': u'mumbai'}], u'screenshots': [], u'id': 863198, u'angellist_url': u'https://angel.co/harleys-clinic', u'quality': 1, u'follower_count': 1, u'hidden': False, u'logo_url': u'https://d1qb2nb5cznatu.cloudfront.net/startups/i/863198-76e851a9d7582242bedc7887d18e47c7-medium_jpg.jpg?buster=1444032995', u'markets': [{u'angellist_url': u'https://angel.co/cosmetic-surgery-1', u'tag_type': u'MarketTag', u'display_name': u'Cosmetic Surgery', u'id': 92439, u'name': u'cosmetic surgery'}], u'status': None, u'product_desc': u"We specialize only in cosmetic surgeries at Harley Street. Our sole purpose is to offer you the highest quality of services. Cosmetic surgery is a full-time job. We say this because you would expect specialization of procedures which result in greater proficiency, expertise and ability. No matter what procedure you're interested in, you can be sure that we have the expertise, and the talent to give you the beautiful, natural-looking results you want.", u'twitter_url': None, u'high_concept': u'Best Cosmetic Surgeon in Mumbai', u'facebook_url': None, u'updated_at': u'2015-10-05T08:16:40Z', u'thumb_url': u'https://d1qb2nb5cznatu.cloudfront.net/startups/i/863198-76e851a9d7582242bedc7887d18e47c7-thumb_jpg.jpg?buster=1444032995', u'company_size': None, u'name': u'Harleys Clinic', u'created_at': u'2015-10-05T08:16:40Z', u'linkedin_url': None, u'blog_url': None}
"""

fields = ["name", "high_concept", "company_url", "linkedin_url", "twitter_url" ]
for line in sys.stdin.readlines():
    #print(line)
    #users = json.loads(line)
    #print(line)
    try:
        users = json.loads(line)
        for user in users["users"]:
            if user["investor"] == True:
                #print(user["name"])
                print(json.dumps(user))
            """
            #print(user)
            datum = []
            for field in fields:
                if field in user and user[field] is not None:
                    f = user[field]
                    f = f.replace('\n', ' ')
                    datum.append(user[field])
                else:
                    datum.append("")
            if "company_type" in user:
                company_type = user["company_type"]
                #print company_type
                if (company_type):
                    datum.append(company_type[0]["name"])
            #datum = [ unicode(user[field]) for field in fields if field in user ]
            #print(datum)
            print(";".join(datum))
            #print("\n")
            """
    except:
        #print("skipping user %s" % e.strerror)
        next


"""
{u'image': u'https://d1qb2nb5cznatu.cloudfront.net/users/191364-medium_jpg?1405523894', u'locations': [{u'angellist_url': u'https://angel.co/italy', u'tag_type': u'LocationTag', u'display_name': u'Italy', u'id': 2127, u'name': u'italy'}, {u'angellist_url': u'https://angel.co/barcelona', u'tag_type': u'LocationTag', u'display_name': u'Barcelona', u'id': 1853, u'name': u'barcelona'}], u'resume_url': u'https://www.linkedin.com/in/carlucciluca', u'id': 191364, u'angellist_url': u'https://angel.co/luca-bidaway-com', u'what_ive_built': u"I'm good", u'criteria': u'', u'follower_count': 684, u'skills': [{u'display_name': u'Strategy', u'name': u'strategy', u'level': 4.0, u'angellist_url': u'https://angel.co/strategy', u'id': 15552, u'tag_type': u'SkillTag'}, {u'display_name': u'Business Development', u'name': u'business development', u'level': 4.0, u'angellist_url': u'https://angel.co/business-development-1', u'id': 15525, u'tag_type': u'SkillTag'}, {u'display_name': u'Corporate Finance', u'name': u'corporate finance', u'level': 3.0, u'angellist_url': u'https://angel.co/corporate-finance', u'id': 36258, u'tag_type': u'SkillTag'}, {u'display_name': u'Entrepreneurship', u'name': u'entrepreneurship', u'level': 3.0, u'angellist_url': u'https://angel.co/entrepreneurship', u'id': 15745, u'tag_type': u'SkillTag'}, {u'display_name': u'Project Management', u'name': u'project management', u'level': 3.0, u'angellist_url': u'https://angel.co/project-management-1', u'id': 24003, u'tag_type': u'SkillTag'}], u'bio': u'Founder of @bidaway \u2022 Strong business and financial background (WTO, Cimolai Group, EDPR) \u2022 IESE MBA 2012', u'blog_url': u'', u'twitter_url': u'https://twitter.com/Gehnibo', u'facebook_url': u'', u'what_i_do': u'I have worked throughout Europe as diplomat at the WTO and as corporate financial manager leading teams and working on large projects before managing a holiday resort. As CEO at BidAway, I am in charge of product development and general management (legal, external relations, business development).', u'aboutme_url': u'', u'investor': True, u'name': u'Luca Carlucci', u'roles': [{u'angellist_url': u'https://angel.co/entrepreneur-1', u'tag_type': u'RoleTag', u'display_name': u'Entrepreneur', u'id': 14725, u'name': u'entrepreneur'}, {u'angellist_url': u'https://angel.co/product_manager', u'tag_type': u'RoleTag', u'display_name': u'Product Manager', u'id': 80487, u'name': u'product_manager'}], u'dribbble_url': u'', u'linkedin_url': u'http://www.linkedin.com/in/carlucciluca', u'github_url': u'', u'behance_url': u'', u'online_bio_url': u'http://www.bidaway.com/'}
"""

