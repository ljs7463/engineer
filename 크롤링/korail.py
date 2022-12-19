from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup


member_num = input("코레일맴버쉽 번호 입력 : ")
password = input("비밀 번호 입력 : ")

pathChrome = "chrome/chromedriver.exe"
driver = webdriver.Chrome(pathChrome)

driver.implicitly_wait(4)
driver.get("http://www.letskorail.com/korail/com/login.do")  # 코레일 로그인화면 접속
time.sleep(0.5)
driver.find_element_by_name("txtMember").send_keys(member_num)
time.sleep(0.5)
driver.find_element_by_name("txtPwd").send_keys(password)


driver.find_element_by_xpath("//img[@src ='/images/btn_login.gif']").click()
driver.implicitly_wait(3)
time.sleep(0.5)

start = input("출발지 입력 : ")
end = input("도착지 입력 : ")
year = input("년도 입력 : ")
month = input("월 입력 : ")
day = input("일 입력 : ")
hous = input("출발시간 입력 : ")

driver.find_element_by_xpath("//img[@src='/images/btn_inq_tick.gif']").click()
driver.implicitly_wait(3)

driver.get(
    "http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do"
)  # 예약 화면 접속
driver.implicitly_wait(3)

driver.find_element_by_name("txtGoStart").clear()
driver.find_element_by_name("txtGoStart").send_keys(start)
driver.find_element_by_name("txtGoEnd").clear()
driver.find_element_by_name("txtGoEnd").send_keys(end)

driver.find_element_by_name("selGoYear").send_keys(year)
driver.find_element_by_name("selGoMonth").send_keys(month)
driver.find_element_by_name("selGoDay").send_keys(day)
driver.find_element_by_name("selGoHour").send_keys(hous)

