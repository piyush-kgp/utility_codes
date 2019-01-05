from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime as dt
from datetime import date
import random
import calendar
import sys
import os
import time
import subprocess

if dt.now().weekday() not in [0, 1, 2, 3, 4]: sys.exit()

file_name = str(date.today()) + calendar.day_name[dt.now().weekday()]+'.txt'
file = open(file_name, 'w')
sys.stdout = file

print('This code is running at', str(dt.now()), calendar.day_name[dt.now().weekday()])
wait = random.randint(0, 300)
print('I shall wait for', wait, 'seconds before running')
time.sleep(wait)
print('Okay Go')
#fp is the path where your cache and browser preferences are stored.
#you could also simply go like this on terminal: cat ~/.mozilla/firefox/profiles.ini | grep 'Path=' | sed s/^Path=//
#and then set fp like fp = '/home/piyush/.mozilla/firefox/3epyphd4.default'
fp = subprocess.check_output("cat ~/.mozilla/firefox/profiles.ini | grep 'Path=' | sed s/^Path=//").decode('utf-8')


driver = webdriver.Firefox(fp)
driver.get("http://192.168.0.1:8090/httpclient.html")

elem = driver.find_element_by_name('username')
elem.send_keys('_')
elem = driver.find_element_by_name('password')
elem.send_keys('_')
elem.send_keys(Keys.RETURN)

time.sleep(5)
driver.get("https://people.zoho.com")
time.sleep(5)
try:
    elem = driver.find_element_by_id('zp_dash_att_btn')
except:
    print('Looks like I shall have to sign in')
    driver.get("https://accounts.zoho.com/signin?servicename=zohopeople")
    elem = driver.find_element_by_name('lid')
    elem.send_keys('_')
    elem = driver.find_element_by_name('pwd')
    elem.send_keys('_')
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_id('signin_submit')
    elem.click()
    try:
        elem = driver.find_element_by_id('zp_dash_att_btn')
    except:
        elem = driver.find_element_by_id('continue_skip')
        elem.click()
        elem = driver.find_element_by_id('continue_url')
        elem.click()
    elem = driver.find_element_by_id('zp_dash_att_btn')

print('To Do:', elem.text)

elem = driver.find_element_by_id('zp_dash_att_btn')
elem.click()
time.sleep(10)
if driver.find_element_by_id('zp_dash_att_btn').text == 'Check-out': print('done!! Attendance recorded at ' + str(dt.now()))
if driver.find_element_by_id('zp_dash_att_btn').text == 'Check-in': print('done!! Checked out at '+ str(dt.now()))
#driver.close()
