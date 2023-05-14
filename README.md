# Spareroom New Listing Finder
Repeatedly check Spareroom search results for pre-defined searches. On a new result, there is a beep sound and the search results open in browser.

Dependencies:
- Python 3+

Instructions:
- Create a virtual environment if desired `python -m venv venv` and activate with `source venv/bin/activate`
- Install requirements (requests, BeautifulSoup) `pip install -r requirements.txt`
- Create `search_urls.py` using `search_urls_example.py` as reference. The URLs can be found in the browser by creating and saving a Spareroom search, and ordering by date
- If desired, change the frequency of checks (1 minute default) and length of the beep sound (1 second default)
- To run, `python main.py`
- When a new search result is found, the beep sound will play and the search results will open in the browser
