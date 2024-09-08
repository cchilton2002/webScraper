import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrapeWebsite(website):
    print("Launching chrome browser...")
    
    chromeDriverPath = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chromeDriverPath),options=options)
    
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()