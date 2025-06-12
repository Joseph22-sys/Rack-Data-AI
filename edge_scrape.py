import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import time


def scrape_edge_website(website):
    print("launching the Edge Browser...")
    edge_driver_path = "./drivers/msedgedriver.exe"
    
    driver = webdriver.Edge(service=EdgeService(edge_driver_path),options=EdgeOptions())
    
    try:
        driver.get(website)
        print("page loaded....")
        html = driver.page_source
        
        time.sleep(10)
        
        return html
    finally:
        driver.quit()
        
    
        