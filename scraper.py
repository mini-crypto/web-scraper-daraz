from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.daraz.pk/")

time.sleep(5)


search = driver.find_element(By.NAME, "q")
search.send_keys("laptop")
search.send_keys(Keys.RETURN)

time.sleep(5)


names = []
prices = []


products = driver.find_elements(By.CSS_SELECTOR, "div[data-qa-locator='product-item']")

for product in products:
    try:
        name = product.text.split("\n")[0]  
    except:
        name = "N/A"

    try:
        price = product.text.split("\n")[1]
    except:
        price = "N/A"

    names.append(name)
    prices.append(price)

driver.quit()


df = pd.DataFrame({
    "Product Name": names,
    "Price": prices
})

df.to_csv("data.csv", index=False)

print("CSV file created successfully!")
