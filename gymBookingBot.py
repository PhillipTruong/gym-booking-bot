import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://shop.westernmustangs.ca/')
print(driver.title)

driver.quit()
