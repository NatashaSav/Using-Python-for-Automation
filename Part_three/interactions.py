from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.google.com/earth/'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 60)

launchEarthButton = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/earth-app//paper-drawer-panel/div/earth-toolbar//earth-gm2-icon-button[2]')))
launchEarthButton.click()
