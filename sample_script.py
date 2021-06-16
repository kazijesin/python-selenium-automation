from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# init driver
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path='/Users/raihanamin/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

sleep (4)

driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')
#Click search

driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url. lower()}"
print('Test Passed')

driver.quit()
