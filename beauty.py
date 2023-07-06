import bs4
import urllib.parse

with open("store_1.html", "r") as f:
    soup = bs4.BeautifulSoup(f, "html.parser")

selected_elements = soup.select('.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2')

i = 0

for element in selected_elements:
    anchor = element.select('a')
    final_url = anchor[0].get('href')
    try:
        number = final_url.index("%2F") + 3
        sub_string = sub_string.replace("%2F","/").replace("%3F","?").replace("%3D","=").replace("%26","&")
        sub_string = final_url[number:]
    finally:
        sub_string = ''
        sub_string = "https://amazon.in/" + sub_string
    print(sub_string)