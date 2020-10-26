import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



def get_sele(stt):
	name = 'chrome'+str(stt)
	os.mkdir(name)
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument(
		"user-data-dir="+name)
	driver = webdriver.Chrome('./chromedriver', options = chrome_options)
	driver.get('http://m.facebook.com')
	driver.quit()	
for i in range(1,4):
	get_sele(i)




