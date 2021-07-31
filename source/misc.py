# File: malicious.py
# Author: pwd0kernel
# Date: 4/20/2021
# Description: Miscellaneous commands

import requests
import warnings
import wget
from bs4 import BeautifulSoup

class Miscellaneous():
    
    def DownloadLynx():
        try:
            print("Downloading Lynx.zip...")
            wget.download("https://lynx.rip/downloads/Lynx.zip", "Lynx.zip")
            print("Downloaded. it should be in the same directory.")
        except Exception:
            print("There was an error downloading lynx.zip.")

    
    def DownloadLynxBackend():
        try:
            print("Downloading lynx_backend.zip...")
            wget.download("https://lynx.rip/backend/downloads/Release.lynx", "lynx_backend.zip")
            print("Downloaded. it should be in the same directory.")
        except Exception:
            print("There was an error downloading lynx_backend.zip")

    def DownloadLynxDll():
        try:
            print("Downloading lynx.dll...")
            wget.download("http://lynx.rip/backend/downloads/L09dahjd034.dll", "lynx.dll")
            print("Downloaded. it should be in the same directory.")
        except Exception:
            print("There was an error downloading lynx.dll")

    def GetAllUsersnames(PHPSESSID, COOKIES):
        try:
            users_grabbed = []

            print("Getting all users names")
            user_requests = requests.get("https://lynx.rip/dashboard/home/userlist/", cookies=dict(
            PHPSESSID=PHPSESSID, avatar=COOKIES["avatar"], username=COOKIES["username"], did=COOKIES["did"]))

            users = BeautifulSoup(user_requests.text, "html.parser")

            for i in users.find_all("div", {"class": "font-weight-bold font-size-h5 text-light"}):
                users_grabbed.append(i.text)
            print(users_grabbed)
        except Exception:
            print("There was an error while grabbing users")

    def GetAllCloudScriptsCode():
        try:
            code_list = []

            cloudcodes = requests.get("https://lynx.rip/dashboard/home/cloudscripts/storage/")
            cloud_code = BeautifulSoup(cloudcodes.text, "html.parser")
            if cloudcodes.status_code == 200:
                for i in cloud_code.find_all("li"):
                    if "src" in i.text:
                        code_list.append(i.text)
                    else:
                        pass
            else:
                print("There was an error while getting cloud codes, code: " + str(cloudcodes.status_code))
        except Exception:
            print("There was an error while getting all cloud scripts code")

    def SaveCookies(COOKIES):
        try:
            cookies_file = open("saved_cookies.txt" , "w")
            cookies_file.write(str(COOKIES))
            cookies_file.close()
        except Exception:
            print("There was an error while saving your cookies")
    
    def GetDiscord(PHPSESSID):
        try:
            print("getting the discord")
            discordRequest = requests.get("https://lynx.rip/dashboard/home/", cookies=dict(PHPSESSID=PHPSESSID))
            discord = BeautifulSoup(discordRequest.text, "html.parser")
            if discordRequest.status_code == 200:
                for discord_link in discord.find_all("a", href=True):
                    if "discord" in discord_link:
                        print("Discord: ", discord_link["href"])
                    else:
                        pass
            else:
                print("There was an error while getting the discord")
        except Exception:
            print("There was an error while getting the discord")
    
    def GetUpdateVersions(PHPSESSID):
        try:
            update_versions = requests.get("https://lynx.rip/dashboard/home/", cookies=dict(PHPSESSID=PHPSESSID))
            versions = BeautifulSoup(update_versions.text, "html.parser")
            if update_versions.status_code == 200:
                for i in versions.find_all("a", {"class": "text-muted font-weight-bold font-size-lg mb-1"}):
                    if "Version" in i.text:
                        print(i.text)
                    else:
                        pass
            else:
                print("There was an error while getting the versions.")
        except Exception:
            print("There was an error an error while getting the versions.")

    
    def GetPlannedFunctons():
        try:
            planned_requests = requests.get("https://lynx.rip/dashboard/home/", cookies=dict(PHPSESSID=PHPSESSID))
        except Exception:
            print("There was an error while getting the planned functions.")
