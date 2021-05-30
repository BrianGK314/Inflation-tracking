from bs4 import BeautifulSoup
import requests
import numpy as np
import secure

# 1 = 2019, 2 = 2021


#List of websites for different items for both 2019 and 2021
wbst = [("2019 WEBSITE FOR FLOUR","2021 WEBSITE FOR FLOUR"),
         ("2019 WEBSITE FOR MILK","2021 WEBSITE FOR MILK"),
         ("2019 WEBSITE FOR SUGAR","2021 WEBSITE FOR SUGAAR"),
         ("2019 WEBSITE FOR PASTA","2021 WEBSITE FOR PASTA"),]

#cleaning data from scraping and puting it into a list
def getList(prices):

      list_ = []
      for price in prices:
          item = price.text.replace("KSh","")
          b= item.strip(" ")
          l=b.replace(",","")
          
          #restricts prices to 400 KSH or lower to weed out bulk item placements
          if(len(l) > 1 and int(l) < 400):
              list_.append(int(l))
      return list_


#returns inflation rates
def getInfaltion(list___):

  inf=[]
  #make request to each website
  for i in range(len(list___)):
    source1 = requests.get(list___[i][0]).text
    source2 = requests.get(list___[i][1]).text

    soup1 = BeautifulSoup(source1, 'html')
    soup2 = BeautifulSoup(source2, 'html')

    prices1 = soup1.findAll('span', class_='price')
    prices2 = soup2.findAll('div', class_="prc")


    list1 = getList(prices1)
    list2 = getList(prices2)

    inflation = ((np.median(list2)-np.median(list1))/np.median(list1))*100
    
    #use standard deviation and range to measure spread of data
    #range_=(np.std(list2)-np.std(list1))
    #inf.append(range_)


    inf.append(round(inflation))
    
  return inf

ooo = getInfaltion(wbst)

print(np.mean(ooo))
