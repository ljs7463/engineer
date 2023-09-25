from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup


member_num = "1577141949"
password = "sS815076!!"

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

start = "서울"
end = "울산(통도사)"
year = 2023
month = 1
day = 21
hous = 18

# # 사용자에게 필요한 정보 얻기
# driver.find_element_by_xpath("//img[@src='/images/btn_inq_tick.gif']").click()
# driver.implicitly_wait(3)

# 예약조회 사이트 접속
driver.get('http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do') # 예약 화면 접속
driver.implicitly_wait(3)  

driver.find_element('txtGoStart').clear()
time.sleep(2)

# # 조건입력
# driver.find_element('txtGoStart').clear()
# driver.implicitly_wait(3)   
# driver.find_element('txtGoStart').send_keys(start)
# driver.implicitly_wait(3)   
# driver.find_element('txtGoEnd').clear()
# driver.implicitly_wait(3)   
# driver.find_element('txtGoEnd').send_keys(end)
# driver.implicitly_wait(5)   

# driver.find_element('selGoYear').send_keys(year)
# driver.implicitly_wait(5)   
# driver.find_element('selGoMonth').send_keys(month)
# driver.find_element('selGoDay').send_keys(day)
# driver.implicitly_wait(5)   
# driver.find_element('selGoHour').send_keys(hous)


# # 조회하기 클릭
# driver.find_element_by_xpath("//img[@src='/images/btn_inq_tick.gif']").click()
# driver.implicitly_wait(5)   
###########################################
# driver.get(
#     "http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do"
# )  # 예약 화면 접속
# driver.implicitly_wait(3)

# driver.find_element_by_name("txtGoStart").clear()
# driver.find_element_by_name("txtGoStart").send_keys(start)
# driver.find_element_by_name("txtGoEnd").clear()
# driver.find_element_by_name("txtGoEnd").send_keys(end)

# driver.find_element_by_name("selGoYear").send_keys(year)
# driver.find_element_by_name("selGoMonth").send_keys(month)
# driver.find_element_by_name("selGoDay").send_keys(day)
# driver.find_element_by_name("selGoHour").send_keys(hous)

