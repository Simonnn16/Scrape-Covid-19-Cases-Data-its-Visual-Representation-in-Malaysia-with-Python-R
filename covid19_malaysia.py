from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests

my_url = 'https://www.worldometers.info/coronavirus/#countries'


html_page = requests.get(my_url).text

soup = BeautifulSoup(html_page, 'lxml')


containers = soup.find("table", id = "main_table_countries_today")

filename = "Covid-19_Malaysia.csv"

headers = "Country, Total Cases, New Cases, Total Deaths, Total Recoverd\n"

f = open(filename, "w")

f.write(headers)

Country = containers.findAll("a", {"href":"country/malaysia/"})[0].text
Total_Cases = containers.findAll("td", {"style":"font-weight: bold; text-align:right"})[462].text
New_Cases = containers.findAll("td", {"style":"font-weight: bold; text-align:right;background-color:#FFEEAA;"})[34].text
Total_Deaths = containers.findAll("td", {"style":"font-weight: bold; text-align:right;"})[58].text 
Total_Recoverd = containers.findAll("td", {"style":"font-weight: bold; text-align:right"})[463].text 

print("Country: " + Country)
print("Total_Cases: " + Total_Cases)
print("New_Cases: " + New_Cases)
print("Total_Deaths: " + Total_Deaths)
print("Total_Recoverd: " + Total_Recoverd)

f.write(Country + "," + Total_Cases.replace(",", " ") + "," + New_Cases.replace(",", " ") + "," + Total_Deaths.replace(",", " ") + "," + Total_Recoverd.replace(",", " ") + "\n")

f.close()	