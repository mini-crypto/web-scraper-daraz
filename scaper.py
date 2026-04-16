from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.daraz.pk/")

time.sleep(5)

# search product
search = driver.find_element(By.NAME, "q")
search.send_keys("laptop")
search.send_keys(Keys.RETURN)

time.sleep(5)

# lists for data
names = []
prices = []

# product blocks (more stable approach)
products = driver.find_elements(By.CSS_SELECTOR, "div[data-qa-locator='product-item']")

for product in products:
    try:
        name = product.text.split("\n")[0]  # first line usually name
    except:
        name = "N/A"

    try:
        price = product.text.split("\n")[1]  # second line usually price
    except:
        price = "N/A"

    names.append(name)
    prices.append(price)

driver.quit()

# save to CSV
df = pd.DataFrame({
    "Product Name": names,
    "Price": prices
})

df.to_csv("data.csv", index=False)

print("CSV file created successfully!")