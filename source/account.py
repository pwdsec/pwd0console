# File: account.py
# Author: pwd0kernel
# Date: 4/20/2021
# Description: can do stuff on your account

import requests
import warnings
from bs4 import BeautifulSoup


class Account():

    # this will change your account bio
    # since the one on the website is currently broken
    def ChangeBio(PHPSESSID, COOKIES, BIO):
        try:
            bio = requests.post("https://lynx.rip/dashboard/home/profile/", data={'bio': BIO}, verify=False, cookies=dict(
            PHPSESSID=PHPSESSID, avatar=COOKIES["avatar"], username=COOKIES["username"], did=COOKIES["did"]))
            if bio.status_code == 200:
                print("Bio as been updated to:", BIO)
            else:
                print("There was an error updating bio.")
            pass
        except Exception:
            print("There was an exception trying to change your bio.")
