'''
Scheduling:
is an in-process scheduler for periodic jobs that uses the builder pattern
for configuration. it lets you run functions periodically at pre-determined 
interals
'''
# pip install schedule

from instapy import InstaPy 
from instapy import smart_run
from instapy import set_workspace
import schedule
import time

# user credentials
userName = ''
userPass = ''

# actions 
'''
like posts based on hashtags
session.like_by_tags(['nature', 'summer'], amount=10)

# like tags and interact with user 
session.set_user_interact(amount=3, randomize=True, percentage=100, media="Photo")
session.like_by_tags('nature', 'summer', amount=10, interact=True)

'''

# path to workspace
#C:\Users\user\Desktop\DDK\instagram-image-scraper\insta-scrape\Include
set_workspace(path='./insta-scrape/Include'

def job():
    session = InstaPy(username=userName, password=userPass)
    with smart_run(session):
	session.set_do_comment(enabled=True, percentage=20)
	session.set_comment(['Well DONE!'])
	session.set_do_follow(enabled=True, percentage=5, times=2)
	session.like_by_tags(['nature'], amount=10, media='Photo')
    
schedule.every().day.at("5.30").do(job)
# at noone
#schedule.every().day("16.30").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)

print('done!')




































