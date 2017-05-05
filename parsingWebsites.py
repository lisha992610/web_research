# Author: Shiying Li, created on 20.03.2017
#
# Python 3 - Parsing Websites with re and urllib


import urllib.request
import urllib.parse
import re
import requests
import time
import csv
import numpy as np


web = "site:https://www.bcg.com/en-ch/ "

# Read the csv
keywords = []
result_num = []
with open('keyword1.csv',newline='') as csvfile:
    readcsv = csv.reader(csvfile)
    keywords = list(readcsv)

print(len(keywords))

for keyword in keywords:
    print(keyword)
    print(''.join(keyword))
    keyword = ''.join(keyword)
    keyword = '"'+keyword+'"'
    print (keyword)
    print(type(web))
    print(type(keyword))
    query = web+keyword
    print(query)
    url = 'http://www.google.ch/search'
    values = {'q': query}

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    try:
        print('starting')
        r = requests.get(url, params=values, headers=headers)
        print(r.url)
        result = re.findall(r'<div id="resultStats">(.*?)<nobr>',r.text)
        if result == []:
            result_num.append('0')
            print("no result")
        else:
            b = '[""]'.join(result)
            b.replace("'","")
            c = b.split()
            result_num.append(c[-2])
            print(c[-2])
    except Exception as e:
        print(str(e))
        result_num.append('oops')

    time.sleep(15)

np.save('result.npy', result_num)

with open('recording.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, skipinitialspace=True)
    for row in result_num:
        writer.writerow([row])
print("finish")
