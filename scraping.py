from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start a new WebDriver session (Chrome in this case)
driver = webdriver.Chrome()

# Open Google Play
driver.get("https://play.google.com/store")

# Find the search icon by class and aria-hidden attribute
search_icon = driver.find_element(By.CSS_SELECTOR, '.google-material-icons[aria-hidden="true"]')

# Click the search icon to open the search input
search_icon.click()

# Wait for the search input to become visible
search_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search Google Play"]')
while not search_input.is_displayed():
    time.sleep(1)

# Prompt the user for a search query
search_query = input("Enter your search query: ")

# Enter the user-provided search query
search_input.send_keys(search_query + Keys.RETURN)

# Wait for the results to load
time.sleep(5)

# Find the link in the specified div
link = driver.find_element(By.CSS_SELECTOR, 'a[href="/store/apps/details?id=com.zhiliaoapp.musically"]')

# Click on the link to view the page
link.click()

# Wait for the page to load (you can increase the sleep time if needed)
time.sleep(5)

# Close the WebDriver session
driver.quit()
