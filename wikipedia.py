from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=chrome_options)

#navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#hone in one anchor tag using CSS selector
article_count=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
#article_count.click()
print(article_count.text)

#find elemnts by linktext
all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")
#all_portals.click()

#find "search " input by name
search=driver.find_element(By.NAME,value="search")

#find keyboard input to selenium
search.send_keys("Python",Keys.ENTER)


#driver.close()
driver.quit()