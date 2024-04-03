from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Create a WebDriver instance
driver = webdriver.Chrome()

# Set the timeout to 10 seconds
wait = WebDriverWait(driver, 10)

# Wait until the element with the ID "my_element" is visible
element = wait.until(EC.visibility_of_element_located((By.ID, "my_element")))
