# File: auth.py
# Author: pwd0kernel
# Date: 4/20/2021
# Description: authentification on lynx website

import requests
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")

class LoginHandler():
    
    # this function will send a request to lynx
    # with the PHPSESSID cookie, and it will return
    # all the other cookies so we grab them for lather uses
    def Login(PHPSESSID):
        try:
            login_session = requests.Session()
            login_request = login_session.get("https://lynx.rip/dashboard/home/", cookies=dict(PHPSESSID=PHPSESSID), verify=False)
            
            if login_request.status_code == 200:
                # do stuff with
                return login_session.cookies.get_dict()
            else:
                print("There was an error reaching the dashboard. Request code:", str(login_request.status_code))
                pass
        except Exception:
            print("There was an exception trying to login.")
            pass

    # this will get the user information like
    # the username, bio, role. so then we can use
    # it on the app itself and it returns it
    # so we can use it in the main script [pwd0console.py]
    def Get_User_data(PHPSESSID, COOKIES):
        try:
            userinfo = {}

            user_data = requests.get("https://lynx.rip/dashboard/home/profile/", verify=False, cookies=dict(PHPSESSID=PHPSESSID, avatar=COOKIES["avatar"], username=COOKIES["username"], did=COOKIES["did"]))
            if user_data.status_code == 200:
                get_userdata = BeautifulSoup(user_data.text, "html.parser")
                for username in get_userdata.find_all("a", {"class": "text-light text-hover-primary font-size-h5 font-weight-bold mr-3"}):
                    userinfo["username"] = username.text
                for bio in get_userdata.find_all("span", {"style": "outline: 0px solid transparent;"}):
                    userinfo["bio"] = bio.text
                for role in get_userdata.find_all("span", {"class": "label label-inline label-light-warning font-weight-bold"}):
                    userinfo["role"] = role.text
                return userinfo
            else:
                print("there was an error reaching the profile. Request code:", str(user_data.status_code))
        except Exception:
            print("There was an exception trying to get the username.")