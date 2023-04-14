import re
import time
import datetime
import winreg

from selenium import webdriver
from selenium.webdriver.support.ui import Select

EDGE_PATH = r'driver/msedgedriver.exe'
CHROME_PATH = r'driver/chromedriver.exe'

f = open("data.txt", encoding="utf-8")

S_NUMBER = f.readline()
NAME = f.readline()
CLASS = 'YOUR CLASS'
THE_URL = 'THE URL'

def driverVer():

	try:
		bs = webdriver.Edge(executable_path = EDGE_PATH)

	except:
		try:
			bs = webdriver.Chrome(executable_path=CHROME_PATH)

		except:
			if getChromeVer() [0:2] != '92':
				print("请升级Chrome至最新版(v92)")
				return
			else:
				print("仅支持Edge与Chrome -- 若您的电脑上安装了对应的浏览器,请升级至最新版。升级后若仍出现该信息,请联系我")
				return

	return bs

version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')
def getChromeVer():

	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\Google\Chrome\BLBeacon')
		value = winreg.QueryValueEx(key, 'version')[0]
		return version_re.findall(value)[0]

	except WindowsError as e:
		return '0.0.0'  # 没有安装Chrome浏览器

def dTime():
	
	currTime = datetime.datetime.now()
	sendTime = str(currTime.year) + '/' + str(currTime.month) + '/' + str(currTime.day)

	return sendTime

def log():

	url = THE_URL

	if driverVer():

		bs = driverVer()

		bs.get(url)
		time.sleep(0.1)

		myNumber = bs.find_element_by_name('question_434724')
		myNumber.send_keys(S_NUMBER)
		time.sleep(0.1)

		myName = bs.find_element_by_name('question_434727')
		myName.send_keys(NAME)
		time.sleep(0.1)

		sel = bs.find_element_by_name('question_434726')
		Select(sel).select_by_value(CLASS)
		time.sleep(0.1)

		btn_health = bs.find_element_by_name('question_434728')
		btn_health.click()
		time.sleep(0.1)

		today = bs.find_element_by_name('question_435964')
		today.send_keys(dTime())
		time.sleep(0.1)

		btn_reg = bs.find_element_by_id('customform-submit')
		btn_reg.click()

		time.sleep(0.5)
		bs.close()

	else:
		time.sleep(10)


if __name__ == '__main__':
	log()
