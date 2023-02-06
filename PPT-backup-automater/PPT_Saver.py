#!/usr/bin/env python
# coding: utf-8

#import the necessary libraries
import requests
import shutil
import os
import time

#url of the file you are trying to download
url = r"https-url-goes-here.com"

#folder you want to download to
download_folder = r"path/to/where/you/want/downloaded/document"

#timestamp for backup
#important because not adding timestamp or name differentiator will override your previous save
timestamp = time.strftime("%Y-%m-%d_%H-%M")

#download and move powerpoint file
response = requests.get(url,stream=True)
local_file = os.path.join(download_folder,f"presentationbackup_{timestamp}.pptx")
with open(local_file,'wb') as f:
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, f)






