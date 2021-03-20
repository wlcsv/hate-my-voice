from selenium import webdriver 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.keys import Keys

f = open("teste")

driver = webdriver.Chrome()
driver.get("https://ttsmp3.com/")

element = driver.find_element_by_id("voicetext")
element.clear()
element.send_keys(f.read())
# element.send_keys("olá")
element.send_keys(Keys.RETURN)

element = driver.find_element_by_xpath("//*[@id='sprachwahl']")
b = driver.find_element_by_xpath("//*[@id='sprachwahl']/option[5]")
b.click()

a = driver.find_element_by_xpath("//*[@id='vorlesenbutton']")
a.click()

# driver.'close()	
