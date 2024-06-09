from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#  Path to chromedriver.exe
chrome_driver_path = "C:/Users/sergey.b/chromedriver/win64-125.0.6422.142/chromedriver-win64/chromedriver.exe"

# Creating a Service instance with the path to the chromedriver.exe file
service = Service(executable_path=chrome_driver_path)

# Setting browser options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # לפתוח את הדפדפן במסך מלא

# Creating an instance of WebDriver with Service and Options
driver = webdriver.Chrome(service=service, options=options)

# Opening a website
driver.get("http://www.google.com")

# Run more automation code here...

# closing the browser
driver.quit()
