import requests
import time
import webbrowser
import winsound
from bs4 import BeautifulSoup
from search_urls import URLS

TIME_INTERVAL = 60  # Time interval between requests (in seconds)
BEEP_LENGTH = 1  # Notification beep length (in seconds)


def get_first_result_header(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find("li", class_="listing-result").find("h2").text


def notify(search, url):
    print(f"{search} search has changed.")
    winsound.Beep(1000, BEEP_LENGTH * 1000)
    webbrowser.open(url)


def check_website_changes():
    for search, url in URLS:
        first_result = get_first_result_header(url)
        if search in top_results:
            if top_results[search] != first_result:
                notify(search, url)
                top_results[search] = first_result
        else:
            top_results[search] = first_result


if __name__ == "__main__":
    top_results = {}
    while True:
        check_website_changes()
        time.sleep(TIME_INTERVAL)
