from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Function to scrape HTML from a website
def scrape_website(website_url):
    # Path to WebDriver
    webdriver_path = "./chromedriver"  # Replace with your WebDriver path
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    try:
        # Open the website
        driver.get(website_url)
        # Wait for the page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        # Extract the HTML source
        html_content = driver.page_source
        return html_content
    finally:
        # Ensure the browser is closed after scraping
        driver.quit()
