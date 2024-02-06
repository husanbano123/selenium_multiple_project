from selenium import webdriver
from selenium.webdriver.common.by import By


chrom_options=webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrom_options)

driver.get("https://www.python.org/")
driver.implicitly_wait(1.0)
search_bar=driver.find_element(By.CLASS_NAME,value="q")
#print(search_bar.get_attribute("placeholder"))
button=driver.find_element(By.ID,"submit")
#print(button.size)
documentation_link=driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
#print(documentation_link.text)
#bug_link=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a') #//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a
p#rint(bug_link.text)
tier_1=driver.find_elements(By.CLASS_NAME,value="tier_1")
event_time=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR,value=".event_widget li a")
#for time in event_names:
    #print(time.text)
events={}
for n in event_time:
    events[n]={
        "time":event_times[n].text,
        "names":event_names[n].text
    }
print(events)
#driver.close()

driver.quit()