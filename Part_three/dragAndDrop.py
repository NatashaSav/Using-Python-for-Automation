from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="box3"]')))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="box103"]')))
ActionChains(driver).drag_and_drop(drag, drop).perform()





