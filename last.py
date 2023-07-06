from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import bs4

default_url = "https://www.amazon.in/s?k=bags&crid=3RXHWM4CTEH4C&sprefix=bags%2Caps%2C433&ref=nb_sb_noss_1"
file_name = "store"

product_url = []

with open('products.csv','w',newline='') as file:
    writer = csv.writer(file)
    header = ["product url","product name","product price","rating","number of reviews","description","asin","danufacturer"]
    writer.writerow(header)

start = 1
end = 2

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.implicitly_wait(10)

def file_writer(name,val):
    with open(f"{name}_{val}.html","w") as f:
        sourcer = driver.page_source
        f.write(sourcer)

def page_allocator(name,val):
    prod_val = 1
    elements = driver.find_elements(By.CSS_SELECTOR, '.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
    urls = [i.get_attribute('href') for i in elements]
    for url in urls:
        driver.get(url)
        file_writer(f"./products/{name}", f"{val}_{prod_val}")
        prod_val += 1
        product_url.append(driver.current_url)

driver.get(default_url)
page_allocator(file_name,start)
start += 1

while start < end:
    urls = f"https://www.amazon.in/s?k=bags&page={start}&crid=ULWLFTP4YQBC&qid=1688637618&sprefix=bags%2Caps%2C206&ref=sr_pg_1"
    driver.get(urls)
    page_allocator(file_name,start)
    start += 1

driver.close()

