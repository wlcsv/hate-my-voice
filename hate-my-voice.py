from selenium import webdriver 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.keys import Keys

file = open("teste")

driver = webdriver.Chrome()
driver.get("https://ttsmp3.com/")

element = driver.find_element_by_id("voicetext")
element.clear()
element.send_keys(f.read())
# element.send_keys("olá")
element.send_keys(Keys.RETURN)

element = driver.find_element_by_xpath("//*[@id='sprachwahl']")
voiceSelector = driver.find_element_by_xpath("//*[@id='sprachwahl']/option[5]")
voiceSelector.click()

voice = driver.find_element_by_xpath("//*[@id='vorlesenbutton']")
voice.click()

# driver.'close()	
