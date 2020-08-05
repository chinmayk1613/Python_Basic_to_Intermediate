#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS")
c=r.content


soup=BeautifulSoup(c,"html.parser")

date=soup.find("div",{"id":"bse_upd_time"}).text


all_BSE=soup.find_all("span",{"id":"Bse_Prc_tick"})
all_BSE_PRV_CLS=soup.find_all("div",{"id":"b_prevclose"})
all_BSE_OPEN=soup.find_all("div",{"id":"b_open"})
all_NSE=soup.find_all("span",{"id":"Nse_Prc_tick"})
all_NSE_PRV_CLS=soup.find_all("div",{"id":"n_prevclose"})
all_NSE_OPEN=soup.find_all("div",{"id":"n_open"})

c_Name=soup.find("h1",{"class":"b_42 company_name"}).text

d_BSE={}
d_NSE={}
l_BSE=[]
l_NSE=[]

d_BSE["A_Script Name"]=c_Name
d_BSE["Exchange_Name"]="BSE"
d_NSE["A_Script Name"]=c_Name
d_NSE["Exchange_Name"]="NSE"

for item in all_BSE:
    
    try:
        d_BSE["Todays Close"]=item.find("strong").text
    except:
        d_BSE["Todays Close"]=None
        
for item in all_BSE_PRV_CLS:
    try:
        d_BSE["Previous Close"]=item.find("strong").text
    except:
        d_BSE["Previous Close"]=None
        
for item in all_BSE_OPEN:
    try:
        d_BSE["Todays Open"]=item.find("strong").text
    except:
        d_BSE["Todays Open"]=None
        
l_BSE.append(d_BSE)
   
for item in all_NSE:
    try:
        d_NSE["Todays Close"]=item.find("strong").text
    except:
        d_NSE["Todays Close"]=None

for item in all_NSE_PRV_CLS:
    try:
        d_NSE["Previous Close"]=item.find("strong").text
    except:
        d_NSE["Todays Close"]=None
        
for item in all_NSE_OPEN:
    try:
        d_NSE["Todays Open"]=item.find("strong").text
    except:
        d_NSE["Todays Close"]=None
l_NSE.append(d_NSE)        
        

df=pandas.DataFrame(l_BSE)
df.rename(index={0:date},inplace=True)

df1=pandas.DataFrame(l_NSE)
df1.rename(index={0:date},inplace=True)

concat = pandas.concat([df,df1])

#concat.to_csv("Final_Exchange_Data.csv")

with open('Final_Exchange_Data.csv', 'a') as f:
      concat.to_csv(f, header=False)

print("Data Added Succesfully")