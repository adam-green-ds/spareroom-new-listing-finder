# Spareroom New Listing Finder

This program repeatedly checks Spareroom search results for new listings based on pre-defined searches. When a new result is identified, the system will beep and automatically open the search results in your browser.

## Dependencies

- Python 3 or higher

## Instructions

1. **Create a Virtual Environment** (Optional)
    - If desired, you can create a virtual environment to keep the dependencies required by this project separate from your main Python environment.
        ```
        python -m venv venv
        ```
    - To activate the virtual environment:
        ```
        source venv/bin/activate
        ```

2. **Install Requirements**
    - Install the necessary libraries by running:
        ```
        pip install -r requirements.txt
        ```

3. **Setup Search URLs**
    - Create a `search_urls.py` file, using `search_urls_example.py` as a reference. 
    - The URLs for the searches can be obtained by creating and saving a Spareroom search in your browser and ordering the results by date.

4. **Customize Settings** (Optional)
    - If desired, you can adjust the frequency of checks (default is set to 1 minute) and the length of the beep sound (default is set to 1 second).

5. **Run the Program**
    - To start the program, use the command:
        ```
        python main.py
        ```
    - Upon detecting a new search result, the program will beep and the search results will be displayed in your browser.
