from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("C:\\Users\\ALAGU SUNDARI\\Downloads\\geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://login.yahoo.com")
driver.find_element(By.ID, 'login-username').send_keys('alagusundari489@yahoo.com')
driver.find_element(By.ID, 'login-signin').click()
driver.find_element(By.ID, 'login-passwd').send_keys("arun@123")
driver.find_element(By.ID, 'login-signin').click()
driver.find_element(By.CLASS_NAME, 'mail').click()
driver.find_element(By.CLASS_NAME,  'e_dRA').click()
driver.find_element(By.ID, 'message-to-field').send_keys("alagusundarimca@gmail.com")
driver.find_element(By.XPATH, "//input[@aria-label='Subject']").send_keys("hai hello")
driver.find_element(By.CLASS_NAME, 'q_Z29WjXl').click()


