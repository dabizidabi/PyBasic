#script without checking network file state!

import json
import urllib.request
from urllib.request import Request, urlopen
import gzip
import os
import time
 
file_name = "file.mdd.gz" #set name for download file
download_to = "/tmp/" #set path to download file
rename_file = "this_file.mdd" #set name of unziped file
time_for_repeat_code = 60 #repeat code after specified seconds
md5sumPrev = 0 #starting value of md5sum
url = https://url

while True:

    #Get data from link
    request = Request(str(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request)

    #Parse json
    jsonData = json.loads(response.read())

    #Find md5 of file
    md5sum = jsonData['mmdb']['md5sum']

    if md5sum != md5sumPrev:

        #Download fileS
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0')
        filename, headers = opener.retrieve(str(jsonData['mmdb']['url']), download_to + file_name)

        #Gunzip file
        with gzip.open(file_name, 'rb') as f_in:
            with open(rename_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                      
        #Delete .gz archive
        os.remove(download_to + file_name)

        md5sumPrev = md5sum

    else:
        #Repeat code after specified seconds
        time.sleep(time_for_repeat_code)
