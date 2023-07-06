import urllib.request
import time
def fetch_data(url):
    for i in range(5):
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                data = response.read()
                return data
        except urllib.error.HTTPError:
            time.sleep(1)

if __name__ == "__main__":
    url = "https://www.amazon.com/"
    data = fetch_data(url)
    with open("output.html","w") as f:
        f.write(data)
