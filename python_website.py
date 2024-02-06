from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrom_options)

try:
    driver.get("https://www.python.org")

    # Wait for the search bar to be present on the page
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    print("Search bar found. Placeholder:", search_bar.get_attribute("placeholder"))

    # Wait for the submit button to be clickable
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
    print("Submit button found. Size:", button.size)

    # Wait for the documentation link to be clickable
    documentation_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".documentation-widget a"))
    )
    print("Documentation link found. Text:", documentation_link.text)

    # Wait for the bug link to be clickable
    bug_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'))
    )
    print("Bug link found. Text:", bug_link.text)

    #tier_1 = driver.find_elements(By.CLASS_NAME, value="tier_1")

    event_time=WebDriverWait(driver, 10).until(EC.elements(By.CSS_SELECTOR, value=".event-widget time"))
    event_name = WebDriverWait(driver, 10).until(
        EC.elements(By.CSS_SELECTOR, value=".event-widget li a "))

    #event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
    for n in event_time:
        events[n] = {
            "time": event_times[n].text,
            "names": event_names[n].text
        }
    print(events)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
