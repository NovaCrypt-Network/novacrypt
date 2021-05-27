from .models import Member
from mee6_py_api import API
import asyncio
import logging
import time
import sys
from django.db.models import F
import time

def get_xp():
    # lookup user by id and send them a message
    users = Member.objects.all()
    logger = logging.getLogger('main')
    logger.debug("Running XP Task")
    print("starting")
    mee6API = API('702020759803134023')
   


    for Profile in users:
        time.sleep(3)
        print("doing " + Profile.user.username)
        try:
            if (Profile.discordid):
                try:
                    print("Getting XP")
                    discordid = int(Profile.discordid)
                    xp = asyncio.run(mee6API.levels.get_user_xp(discordid))
                    Profile.xp = xp
                    Profile.save()
                    print(Profile.xp)
                    print("Done!")
                except ValueError:
                    print("Invalid ID")
                except: 
                    e = sys.exc_info()[0]
                    print(e)
                    pass
            else:
                print("No ID")

        except: 
            pass

