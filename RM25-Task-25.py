from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os

# Setup WebDriver path and options
paths = r"D:\ProgramS\PyCharm\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb Advanced Name Search page
driver.get("https://www.imdb.com/search/name/")

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 15)
driver.execute_script("window.scrollTo(500, 500);")
# Fill in the input boxes and select boxes
# For example, filling in the name box
# name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label"))).click()
name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[1]/label/span[1]/div"))).click()
driver.find_element(By.XPATH,'//input[@name="name-text-input"]').send_keys("Anderson")

credits = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label'))).click()
WebDriverWait(driver,300)

# Find the credit input element
credit = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

# Use ActionChains to input text and select the first suggestion
actions = ActionChains(driver)
actions.send_keys_to_element(credit, "Summer")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
actions.pause(1)  # Pause briefly to ensure the selection
actions.send_keys(Keys.ENTER)  # Press the Enter key to select
actions.perform()

seeresult = wait.until(EC.presence_of_element_located(By.XPATH,"/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button"))
seeresult.click()

# Confirmation
print("Search performed successfully.")

# Close the browser
driver.quit()