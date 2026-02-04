import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Added import for Keys
from selenium.webdriver.support.ui import WebDriverWait  # To wait for elements
from selenium.webdriver.support import expected_conditions as EC  # For expected conditions
import time

# Create a webdriver object. Here we use Firefox, but you can choose other browsers like Chrome, Edge, etc.
driver = webdriver.Chrome()

# Navigate to the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Maximize the browser window
driver.maximize_window()

# Wait for 3 seconds to ensure the page is loaded
time.sleep(3)

# Handle iframe if one exists (e.g., an overlay)
iframe_element = driver.find_element(By.XPATH, "//iframe[contains(@src,'accounts.google.com')]")
driver.switch_to.frame(iframe_element)

# Close the overlay (e.g., Google sign-in iframe)
closeele = driver.find_element(By.XPATH, "//*[@id='close']")
closeele.click()

# Wait for the iframe action to complete
time.sleep(3)

# Switch back to the main content
driver.switch_to.default_content()

# Locate the search icon element using XPath
searchIcon = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")

# Wait for 3 seconds before interacting with the search input
time.sleep(3)

# Locate the input field for search text using XPath
enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")

# Enter the search query "Data Structure" into the input field
enterText.send_keys("Data Structure")

# Send the RETURN key to submit the search query
enterText.send_keys(Keys.RETURN)

# Search "GeeksforGeeks"
# box = drv.find_element(By.NAME, "q")
# box.send_keys("GeeksforGeeks", Keys.RETURN)
# time.sleep(5)
# drv.quit()
#
# city = 'Moscow'
#
# url = "https://www.google.com/search?q=" + "weather" + city
#
# res = requests.get(url=url)
# soup = BeautifulSoup(markup=res.content, features='html.parser')
# print(res.status_code)
# print(soup.prettify())
#
# # print(soup.prettify())
# # print(soup.title)
#
# s = soup.find(name='div')
# lines = s.find_all('a')
# # print(soup.prettify())
#
# # for line in lines:
# #     print(line.get('href'))
#
# with open('soup_pars.txt', 'w') as file:
#     file.write(soup.prettify())

# Enter city name
# city = "lucknow"
#
# # Creating URL and making requests instance
# url = "https://www.google.com/search?q=" + "weather" + city
# html = requests.get(url).content
#
# # Getting raw data using BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
#
# # Extracting the temperature
# temp = soup.find('Wind')
#
# # Extracting the time and sky description
# print(html)

# # Getting all div tags with the specific class name
# listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
#
# # Extracting other required data
# strd = listdiv[5].text
# pos = strd.find('Wind')
# other_data = strd[pos:]
#
# # Printing the extracted weather data
# print("Temperature is:", temp)
# print("Time:", time)
# print("Sky Description:", sky)
# print(other_data)
