# amazon-scraper

This is a amazon scraper build using selenium it can scrape product data from the website and write it to a csv file i have used selenium because it resembles a bit like human and it is a advanced testing frameworks which offers many advantages for scraping and i also used beautiful soup to extract data from the scraped data

## project-setup

1.The code is same for both windows and linux you need to install seperate chromedriver for seperate environments you can install chromedriver at <code>https://chromedriver.chromium.org/downloads</code>
<br>
2.setup a python environment using the command <code>python -m venv myenv</code>
<br>
3.activate the python virtual environment for windows <code>myenv/Scripts/activate.ps1</code> and for linux <code>source myenv/bin/activate</code>
<br>
4.install the python modules in the python virtual environment using the command <code>pip install -r requirements.txt</code>
<br>

# usage

1. simply run the project in windows <code>python amazon_scraper.py</code> and in linux <code>python3 amazon_scraper.py</code>

# project-working

1.When you first run the project the selenium will scrape the product and write each product source code into html fiels in the products directory
<br>
2>In the next step the data is extracted from the html files and written to output.csv file