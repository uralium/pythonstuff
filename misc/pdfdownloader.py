from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

profile = {
    'download.prompt_for_download': False,
    'download.default_directory': 'C:\\Downloads',
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True,
}
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', profile)
driver = webdriver.Chrome(options=options)

myUsername="ural.erkut1@gmail.com"
myPassword="galaxy11"
driver.get("https://klett.ch/meinklett/")

#login
driver.find_element("xpath", "//*[@id='username']").send_keys(myUsername);
driver.find_element("xpath", "//*[@id='password']").send_keys(myPassword);
driver.find_element("xpath", '//button[@type="submit"]').click()
time.sleep(2)

#select report
driver.get("https://lernen.klett.ch/ilscl/346")
time.sleep(10)

# #sort the report options
# driver.find_element("xpath", "//*[@id='RadioButton_WordCountSortByWCHighToLow']").click()
# driver.find_element("xpath", "//*[@id='mButton_Next']").click()
# time.sleep(2)

#get the pdf url
mydata = driver.find_element("xpath", '//*[@id="FrameLB"]').get_attribute("iframe src")

print("url: ",mydata)
