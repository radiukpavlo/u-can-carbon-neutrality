import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


def save_as_pdf(html_file, pdf_file):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without opening a UI
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")  # <-- Add this line to fix DevToolsActivePort error
    chrome_options.add_argument("--remote-debugging-port=9222")  # Add this line

    # Selenium Manager will automatically handle the driver.
    driver = webdriver.Chrome(options=chrome_options)

    # Get the absolute path of the HTML file
    html_path = f"file://{os.path.abspath(html_file)}"
    print(f"Opening {html_path}...")
    driver.get(html_path)

    print("Generating PDF...")
    # Use Chrome's DevTools Protocol to print to PDF
    print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': False,
        'paperWidth': 13.33,
        'paperHeight': 7.5,
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