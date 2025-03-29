from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the Chromium executable (adjust if needed)
service = Service('/data/data/com.termux/files/usr/bin/chromium') 

# Create a new Chrome instance
driver = webdriver.Chrome(service=service)

# Navigate to a website
driver.get("https://www.example.com") 

# Perform actions (e.g., find elements, click buttons)
# ...

# Close the browser
driver.quit()

