import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os   
 
def Get_Html_Source(url):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(url) 

	time.sleep(2) 
	  
	html = driver.page_source
	soup = BeautifulSoup(html, "lxml")
	driver.close()
	return soup

def Feature_Set_Backend():
	soup = Get_Html_Source("https://paranoidandroid.co/")
	Feature_p = []
	Feature_li = []
	Feature_Set_DIV = soup.find('div', class_='feature-list')
	Feature_Heading = Feature_Set_DIV.find('h3').text
	for p_Element in Feature_Set_DIV.find_all('p'):
		p_Element = p_Element.text
		Feature_p.append(p_Element)
	for li_Element in Feature_Set_DIV.find_all('li'):
		li_Element = li_Element.text
		Feature_li.append(li_Element)

	Feature_li1 = []
	Feature_li2 = []

	for i in Feature_li :
		if i == '…':
			break
		else:
			Feature_li1.append(i)
	Feature_li2 = Feature_li[int(len(Feature_li1) + 1):-1]
	
	
	return Feature_Heading,Feature_p, Feature_li1, Feature_li2

def Download_Backend():
	soup = Get_Html_Source("https://paranoidandroid.co/downloads")
	Device_Name_List = []
	Device_Codename_List = []
	Devices_Source = soup.find('div', class_ = "list")
	for Devices in Devices_Source.find_all('a', class_ = "list__item"):
		Device_Name_List.append(Devices.div.h3.text)
		Device_Codename_List.append(Devices.div.p.text)
	return Device_Name_List, Device_Codename_List

def Device_Download_Backend(codename):
	soup = Get_Html_Source(f"https://paranoidandroid.co/downloads/{codename}")
	Version_Available = []
	for _ in soup.find_all('div', class_ = "title"):
		Version_Available.append(_.h3.text)
	return Version_Available

def Build_Download_Backend(codename, build):
	soup = Get_Html_Source(f"https://paranoidandroid.co/downloads/{codename}")
	Build_Title = []
	Build_Date = []
	Build_Link_Info = []
	Build_Link_Download = []
	for expand in soup.find_all('div', class_ = "expand"):

		title = expand.h3.text
		if build.upper() == title.upper():
			pass
		else:
			continue
		Build_Title.append(title)
		date = expand.find('h3', class_="list__item--title")
		Build_Date.append(date.text)
		link = expand.find('a', class_="list__item")
		Build_Link_Info.append(link.p.text)
		Build_Link_Download.append(link['href'])

	return Build_Title, Build_Date, Build_Link_Info, Build_Link_Download

'''
if os.name == 'posix':
    operating_system = "linux"
else:
    operating_system = "windows"

def ClearScreen():
    if operating_system.upper() == "LINUX":
        os.system('clear')
    else:
        os.system('cls')
'''