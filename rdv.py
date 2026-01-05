
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 用于实例化一个Driver的显式等待
from selenium.webdriver.common.by import By  # 内置定位器策略集
# 内置预期条件函数，具体API请参考此小节后API链接
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

while True:
	driver = webdriver.Chrome()
	try:
		driver.get('http://www.hauts-de-seine.gouv.fr/booking/create/9489')
	except:
		print("network error")

	#js = "var q=document.documentElement.scrollTop=10000"
	js="scrollTo(0,document.body.scrollHeight)"
	driver.execute_script(js)
	#print("scroll down")
	time.sleep(4)

	try:
		inputDiv = driver.find_element_by_id('condition_Booking')
		checkBox = inputDiv.find_element_by_id('condition')
		checkBox.click()
		demandButton = driver.find_element_by_name('nextButton')
		demandButton.click()
		print("click and go to rdv page")
	except:
		print("network error")
	time.sleep(3)


	try:
		resultRDV= driver.find_element_by_id('FormBookingCreate').text

		if resultRDV == "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement.":
			print("no place")
	except:
		print("can't find no place text ")
		try:
			error502=drvier.find_element_by_tag_name('title').text
			if error502 == "502 Bad Gateway":
				print(error502)
				print("error 502")
		except:
			print("can't get 502")

			#requests.get("https://sc.ftqq.com/SCU78735T53f9f93c90f6e2924fd3bb7074b153495e2a1aa63726a.send?text=找到位置了")
			data={'text':'找到位置','desp':'看电脑'}
			requests.post('https://sc.ftqq.com/SCU78735T53f9f93c90f6e2924fd3bb7074b153495e2a1aa63726a.send',data=data)




	driver.close()  # close the driver
	time.sleep(60)
