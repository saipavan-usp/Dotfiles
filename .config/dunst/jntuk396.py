import subprocess
import requests
from bs4 import BeautifulSoup as bs
import os
from urllib.parse import urlparse
import re
import gdown

urls = [
    "https://www.jntuk396.com/2021/01/cryptography-and-network-security.html",
    "https://www.jntuk396.com/2021/01/software-architecture-design-patterns.html",
    "https://www.jntuk396.com/2021/01/web-technologies.html",
    "https://www.jntuk396.com/2021/01/managerial-economics-and-financial.html",
    "https://www.jntuk396.com/2021/01/mobile-computing.html",
]

for url in urls:
    res = requests.get(url).content
    a_tags = bs(res, features="html5lib").find_all("a")
    sub = url.replace("https://www.jntuk396.com/2021/01/", "").split(".")[0]
    for i in a_tags:
        temp = i.attrs
        if "href" in temp:
            match = re.search(r'd\/(.*)\/', temp["href"])
            if match:
                id = match.groups()[0]
                subprocess.Popen(["gdown", "--id", id])