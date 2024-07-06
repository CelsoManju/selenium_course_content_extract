from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_driver_path = "E:\\chromedriver-win64\\chromedriver.exe"


options = Options()
options.add_argument('--headless') 
options.add_argument('--disable-gpu')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


html_file_path = "D:\\python selenium\\src.html"
driver.get(html_file_path)


sections = driver.find_elements(By.CLASS_NAME, 'accordion-panel-module--panel--Eb0it')


for section in sections:
    try:
        
        topic_element = section.find_element(By.XPATH, './/span[contains(@class, "section--section-title")]')
        topic = topic_element.text.strip() if topic_element else 'No topic found'

       
        duration_element = section.find_element(By.XPATH, './/span[contains(@class, "section--section-content")]')
        duration = duration_element.text.strip() if duration_element else 'No duration found'

        print(f"Topic: {topic}, Duration: {duration}")
    except Exception as e:
        print(f"Error extracting data from section: {e}")

driver.quit()
