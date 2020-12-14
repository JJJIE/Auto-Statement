import time
import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import Select

EDGE_PATH = r'D:/Code/msedgedriver.exe'

S_NUMBER = 'G2007088'
NAME = 'JIN JIAJIE'
CLASS = '中級C4'

def dTime():
	
	currTime = datetime.datetime.now()
	sendTime = str(currTime.year) + '/' + str(currTime.month) + '/' + str(currTime.day)

	return sendTime


def log():

	bs = webdriver.Edge(executable_path = EDGE_PATH)
	url = 'https://customform.jp/form/input/46755'

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


if __name__ == '__main__':
	log()