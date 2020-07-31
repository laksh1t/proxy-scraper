import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date

lis = []

curr_date = date.today()
curr_time = datetime.datetime.now()
create_time = curr_time.strftime("%H.%M.%S")

url = "https://free-proxy-list.net/"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
find_name = soup.find("textarea" ,class_="form-control")

for i in find_name:
    print(find_name.text)
    find_i = find_name.text
    find_r = find_i.replace("Free proxies from free-proxy-list.net"," ")

    rep = find_i.split('\n')
    
    oyx = rep[2:]
    for proxies in oyx:
        print(proxies)
        file  = open(f"{curr_date},{create_time}.txt",'a')
        file.write(proxies)
        file.write("\n")
        file.close()
