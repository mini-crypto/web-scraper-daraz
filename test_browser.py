from selenium import webdriver
import time

# open browser
driver = webdriver.Chrome()

# go to website
driver.get("https://www.google.com")

# wait so you can see it
time.sleep(5)

# close browser
driver.quit()