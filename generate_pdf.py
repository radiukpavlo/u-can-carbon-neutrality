import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time


def save_as_pdf(html_file, pdf_file):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")
    # Set window size to match the slide aspect ratio to help rendering
    chrome_options.add_argument("--window-size=1280,720")

    # Selenium Manager will automatically handle the driver.
    driver = webdriver.Chrome(options=chrome_options)

    # Get the absolute path of the HTML file
    html_path = f"file://{os.path.abspath(html_file)}"
    print(f"Opening {html_path}...")
    driver.get(html_path)

    # Give the browser a moment to render the page
    time.sleep(1)

    print("Generating PDF...")
    # Use Chrome's DevTools Protocol to print to PDF
    # preferCSSPageSize honors the @page rule in the HTML, which is the most reliable way.
    # We also set margins to 0 as a fallback.
    print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True,
        'marginTop': 0,
        'marginBottom': 0,
        'marginLeft': 0,
        'marginRight': 0,
    }

    result = driver.execute_cdp_cmd("Page.printToPDF", print_options)
    driver.quit()

    # Save the result to a file
    with open(pdf_file, "wb") as f:
        f.write(base64.b64decode(result['data']))

    print(f"Successfully created {pdf_file}")


if __name__ == "__main__":
    save_as_pdf("index.html", "presentation_selenium.pdf")