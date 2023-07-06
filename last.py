from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from lxml import etree
import time
import csv
import os

# Enter the url of the product
default_url = "https://www.amazon.in/s?k=bags&crid=3RXHWM4CTEH4C&sprefix=bags%2Caps%2C433&ref=nb_sb_noss_1"
file_name = "store"

# list of product urls
product_url = []

start = 1
# Enter the number of pages you want to scrape
end = 2
directory_name = "products"

# initializing the chromedriver
# options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# checking whether the directory exists or not
def check_and_create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

check_and_create_directory(directory_name)

# creating a file writer function to write page source to a html file
def file_writer(name,val):
    with open(f"{name}_{val}.html","w") as f:
        sourcer = driver.page_source
        f.write(sourcer)

# creating a page allocator function to click on the product link and extract data
def page_allocator(name,val):
    prod_val = 1
    elements = driver.find_elements(By.CSS_SELECTOR, '.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
    urls = [i.get_attribute('href') for i in elements]
    for url in urls:
        driver.get(url)
        file_writer(f"./products/{name}", f"{val}_{prod_val}")
        prod_val += 1
        product_url.append(driver.current_url)

# default step
driver.get(default_url)
page_allocator(file_name,start)
start += 1

# iterating through pages
while start < end:
    urls = f"https://www.amazon.in/s?k=bags&page={start}&crid=ULWLFTP4YQBC&qid=1688637618&sprefix=bags%2Caps%2C206&ref=sr_pg_1"
    driver.get(urls)
    page_allocator(file_name,start)
    start += 1

# closing the webdriver
driver.close()

# The below code is used to write data to the csv file

# creating a new csv file
with open('products.csv','w',newline='') as file:
    writer = csv.writer(file)
    header = ["product url","product name","product price","rating","number of reviews","description","asin","danufacturer"]
    writer.writerow(header)

# variable to give serial numbers in csv
num = 1

# function to extract data fro html and write it to csv
def parser_writer(file,num):
    try:
        with open(file,'r') as f:
            soup = BeautifulSoup(f,'html.parser')
        # creating a dom tree
        dom = etree.HTML(str(soup))

        # getting all the elements with attributes
        product_name = soup.find(class_='a-size-large product-title-word-break').text.strip()
        product_rating_count = soup.find(id='acrCustomerReviewText').text.split(" ")[0].strip()
        
        product_price_symbol = soup.find(class_='a-price-symbol').text
        product_price = soup.find(class_='a-price-whole').text
        product_rating = soup.find(class_='a-size-base a-color-base').text

        product_asin = dom.xpath('//*[@id="detailBullets_feature_div"]/ul/li[4]/span/span[2]')[0].text
        product_manufacturer = dom.xpath('//*[@id="detailBullets_feature_div"]/ul/li[8]/span/span[2]')[0].text
        product_description_parent = soup.find(class_='a-unordered-list a-vertical a-spacing-mini')
        product_description = product_description_parent.find_all(class_='a-list-item')
        # concatenating the currency symbol and price
        product_price = product_price_symbol + product_price

        # list containing all the descriptions
        descript = []

        # looping through the description elements
        for i in product_description:
            # appending the text in the description elements to the descript list
            descript.append(i.text.strip())
        result = ','.join(descript)

        # appending all the data to the products.csv file
        with open('products.csv','a',newline='') as file:
            writer = csv.writer(file)
            row = [num,product_url[num-1],product_name,product_price,product_rating,product_rating_count,result,product_asin,product_manufacturer]
            writer.writerow(row)
            num += 1
    except FileNotFoundError:
        print(f"File '{file}' not found. {num}")
    except Exception as e:
        print(f"An error occurred: {e} {num}")

# getting all the file names in the directory
file_names = os.listdir("./products")

# iterating over the products
for file_name in file_names:
    parser_writer(f"./products/{file_name}",num)