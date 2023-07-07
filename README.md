# amazon-scraper

This is a amazon scraper build using selenium it can scrape product data from the website and write it to a csv file i have used selenium because it resembles a bit like human and it is a advanced testing frameworks which offers many advantages for scraping and i also used beautiful soup to extract data from the scraped data

# project setup

1.The code is same for both windows and linux you need to install seperate chromedriver for seperate environments you can install chromedriver at <code>https://chromedriver.chromium.org/downloads</code> The chromedriver file should be placed at root folder
<br>
2.setup a python environment using the command <code>python -m venv myenv</code>
<br>
3.activate the python virtual environment for windows <code>myenv/Scripts/activate.ps1</code> and for linux <code>source myenv/bin/activate</code>
<br>
4.install the python modules in the python virtual environment using the command <code>pip install -r requirements.txt</code>
<br>

# usage

1. simply run the project in windows <code>python amazon_scraper.py</code> and in linux <code>python3 amazon_scraper.py</code>
1.To run project in windows run the command <code>python amazon_scraper.py</code>
2.To run the project in linux run the command <code>python3 amazon_scraper.py</code>

# project working

1.When you first run the project the selenium will scrape the product and write each product source code into html fiels in the products directory
<br>
2.In the next step the data is extracted from the html files and written to output.csv file

# project files

1.<code>amazon-scraper.py</code> is the main python file which scrapes and writes data to the csv files
<br>
2.<code>requirements.txt</code> is the file which contains all the modules required by the project to function without errors
<br>
3.<code>automate.bat</code> is used to push code to github in windows
<br>
4.<code>automate.sh</code> is used to push code to github in linux

# project working video

<code>https://drive.google.com/file/d/1xS28dAszifytomf69G2MfKjBfMia_it8/view?usp=sharing</code>
