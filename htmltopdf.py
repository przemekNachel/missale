import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def save_html_as_pdf(html_file_path, output_pdf_path):
    # 1. Configure Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Must be headless for print commands
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # 2. Initialize the Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 3. Load the HTML file (use absolute path)
        # For local files, use 'file://' prefix
        import os
        absolute_path = "file://" + os.path.abspath(html_file_path)
        driver.get(absolute_path)

        # 4. Define Print Parameters
        print_options = {
            'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'preferCSSPageSize': True,
        }

        # 5. Execute Chrome DevTools Protocol command to print
        result = driver.execute_cdp_cmd("Page.printToPDF", print_options)

        # 6. Write the base64 result to a file
        with open(output_pdf_path, "wb") as f:
            f.write(base64.b64decode(result['data']))

        print(f"Success! PDF saved to: {output_pdf_path}")

    finally:
        driver.quit()


# Usage
if __name__ == "__main__":
    save_html_as_pdf("missale.html", "from_html.pdf")