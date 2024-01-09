from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://cases.ra.kroll.com/')
time.sleep(3)
#Order by most recent cases by clicking "Most Recent" link xPATH
#Kroll as captcha issues
button = driver.find_element(By.XPATH, '//*[@id="casedirectory"]/section[1]/div/div[2]/ul/li[2]/a').click()
print(button.text)
#cases = driver.find_elements(By.CLASS_NAME, "case-directory_listItem")
#for case in cases:
#    print(case.text)

#import the html to BS:
soup = BeautifulSoup(drive.page_source, 'lxml')