from selenium import webdriver
import time

from selenium.webdriver.common.by import By

url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

messageField = driver.find_element(By.XPATH, '//*[@id="user-message"]')
messageField.click()
messageField.send_keys("Hello World")
showMessageButton = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element(By.XPATH, '//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element(By.XPATH, '//*[@id="sum2"]')
additionField2.send_keys('12')
getTotalButton = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
getTotalButton.click()
time.sleep(7)