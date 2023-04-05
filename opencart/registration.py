import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.opencart.com/")
driver.find_element(By.LINK_TEXT, "My Account").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.NAME,"firstname").send_keys("Bhagya")
time.sleep(5)