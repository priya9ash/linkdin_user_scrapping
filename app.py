from linkedin_api import Linkedin
import json

api=Linkedin("ashwin.berlin111@gmail.com","Ashwin5@p")
profile=input("enter name")
res=api.get_profile(profile)
for key,value in res.items():
    print(f"{key}:{value}")
