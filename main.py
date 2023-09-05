import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#setup the web browser
os.environ['PATH']
driver = webdriver.Firefox()
driver.get("https://monkeytype.com/")
driver.set_window_position(0,0)

#Reject All Cookies
driver.find_element(By.CLASS_NAME, "rejectAll").click()
time.sleep(1)

#Visit Settings
driver.find_element(By.CLASS_NAME, "view-settings").click()
pyautogui.FAILSAFE = True
time.sleep(1)

#Go to Themes
pyautogui.click(x=995,y=380)
time.sleep(1)

#Scroll to theme options
driver.execute_script("window.scrollTo(0, 8400)")
time.sleep(1)

#Click on the theme
pyautogui.click(x=250,y=700)

#Scroll back to top
driver.execute_script("window.scrollTo(0,0)")
time.sleep(1)

#Start standard test
driver.find_element(By.CLASS_NAME, "view-start").click()

try:
    while time.time() < time.time() + 30:
        active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
        letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
        pyautogui.write(letters, interval=0.0)
except Exception as e:
    pass
    
    
time.sleep(2)

#Start test with medium length quotes
driver.find_element(By.CLASS_NAME, "view-start").click()
time.sleep(1)
pyautogui.click(x=850,y=300)
time.sleep(1)

try:
    while(driver.find_element(By.CSS_SELECTOR, ".word.active")):
        active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
        letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
        pyautogui.write(letters, interval=0.0)
except Exception as e:
    pass