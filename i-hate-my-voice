from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ttsmp3.com/")

# f = open("file:///home/wallacy/Documentos/hmm/teste")

element = driver.find_element_by_id("voicetext")
element.clear()

f = open("file:///home/wallacy/Documentos/hmm/teste")

element.send_keys(f.read())
# element.send_keys("hello")
element.send_keys(Keys.RETURN)

a = driver.find_element_by_xpath("//*[@id='vorlesenbutton']")
a.click()


# assert "Python" in driver.title

# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pyco")
# elem.send_keys(Keys.RETURN)

# assert "No results  found." not in driver.page_source

# driver.close()	