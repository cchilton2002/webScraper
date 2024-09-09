import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrapeWebsite(website):
    print("Launching chrome browser...")
    
    chromeDriverPath = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chromeDriverPath),options=options)
    
    try:
        #driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()
        
def extractBodyContent(htmlContent):
    soup = BeautifulSoup(htmlContent, "html.parser")
    bodyContent = soup.body
    if bodyContent:
        return str(bodyContent)
    return ""

def cleanBodyContent(bodyContent):
    soup = BeautifulSoup(bodyContent, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    cleanedContent = soup.get_text(separator="\n")
    cleanedContent = "\n".join(
        line.strip() for line in cleanedContent.splitlines() if line.strip()
    )
    
    return cleanedContent

def splitDomContent(domContent, maxLength=6000):
    return [
        domContent[i:i+maxLength] for i in range(0, len(domContent),maxLength)
    ]