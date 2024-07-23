from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get(r"file:///C:/Users/csejn/OneDrive/Desktop/ca.html")
# Wait for the page to load
time.sleep(2)

# Function to click a button by its text
def click_button(text):
    button = driver.find_element(By.XPATH, f"//button[text()='{text}']")
    button.click()

# Click buttons to perform a calculation: 7 + 8 =
click_button('7')
click_button('+')
click_button('8')
click_button('=')

# Get the result from the screen
result = driver.find_element(By.ID, "screen").text
if (result=='15'):
    print("TEST CASE PASSED")
else:
    print("TEST CASE IS NOT PASSED")

print("Result:", result)

# Close the browser
driver.quit()
