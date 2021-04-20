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