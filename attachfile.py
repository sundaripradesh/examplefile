from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import autoit
service_obj=Service("C:\\Users\\ALAGU SUNDARI\\Downloads\\geckodriver")
driver = webdriver.Firefox(service=service_obj)
username = "alagusundari489@yahoo.com"
password = "arun@123"
driver.get("https://login.yahoo.com")
driver.find_element(By.ID, 'login-username').send_keys(username)
driver.find_element(By.ID, 'login-signin').click()
driver.find_element(By.ID, 'login-passwd').send_keys(password)
driver.find_element(By.ID, 'login-signin').click()
driver.find_element(By.CLASS_NAME, 'mail').click()
driver.find_element(By.CLASS_NAME,  'e_dRA').click()
driver.find_element(By.ID, 'message-to-field').send_keys("alagusundarimca@gmail.com")
driver.find_element(By.XPATH, "//input[@aria-label='Subject']").send_keys("I attach one excel file")
driver.find_element(By.CLASS_NAME,  'D_Z1YJkyX').click()
driver.find_element(By.NAME, 'attach-from-computer').click()
autoit.control_focus("File Upload",  "Edit1")
autoit.control_set_text("File Upload", "Edit1", "C:\\Users\\ALAGU SUNDARI\\OneDrive\\Desktop\\11JUL2022.xlsx")
autoit.control_click("File Upload", "Button1")
driver.find_element(By.CLASS_NAME, 'q_Z29WjXl').click()










