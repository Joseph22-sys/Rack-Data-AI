#import dependencies
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


def scrape_chrome_website(website):
    print("Launching the Chrome Browser...")
    
    chrome_driver_path = "./drivers/chromedriver.exe"
    driver = webdriver.Chrome(service=ChromeService(chrome_driver_path),options=ChromeOptions())
    
    try:
        driver.get(website)
        print("page_loading...")
        html = driver.page_source
        
        time.sleep(10)
        return html
        
    finally:
        driver.quit()
        
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Example: Extracting the title of the page
    title = soup.title.string if soup.title else "No title found"
    # Example: Extracting all paragraphs
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    
    
    return {
        'title': title,
        'paragraphs': paragraphs
    }        
       