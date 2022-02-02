# View > Command Palette > python select interpreter > Select virtualenv
# Import selenium 
from selenium import webdriver

url = "https://miniatureengineer.github.io/generic-login-form/"

loginaname = "iamu"
loginapassword = "abc1234"

# Insert chromedriver 
driver = webdriver.Chrome(executable_path="/Users/carin/Desktop/NTU/learn/coding projects/documentation/test automation/seleniumpy/web login/chromedriver")

driver.get(url)

# Automate each part
driver.find_element_by_id("name").send_keys(loginaname)
driver.find_element_by_id("password").send_keys(loginapassword)
driver.find_element_by_css_selector('button[type="submit"]').click() 

#<button type="submit">Log in</button>
#driver.find_element_by_css_selector('button[type="submit"]').click() 

#<button>Submit</button>
#driver.find_element_by_css_selector('button').click() 