from selenium import webdriver
from selenium.webdriver.common.by import By

chrom_options=webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrom_options)

driver.get("https://www.amazon.in/dp/B00FLYWNYQ/ref=sspa_dk_detail_1?")
price=driver.find_element(By.CLASS_NAME,value="a-price-whole")
print(f"the price is {price.text}")
driver.quit()