import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("http://www.uts.edu.au/")
driver.maximize_window()

# links = driver.find_elements("xpath", "//a[@href]")
# for link in links:
#     if "Engineering" in link.get_attribute("innerHTML"):
#         link.click()
#         break

studyLink = driver.find_element("xpath", "//span[@data-href='/study']")
studyLink.click()


# links = driver.find_elements("xpath", "//a[@href]")
# for link in links:
#     print(link.get_attribute("innerHTML"))
#     # if "Engineering" in link.get_attribute("innerHTML"):
#     #     link.click()
#     #     break

inputElement = driver.find_element(By.ID, "edit-search")
inputElement.send_keys('C09070')
inputElement.send_keys(Keys.ENTER)

courseLink = driver.find_elements("xpath", "//a[@href]")
for link in courseLink:
    if "Bachelor of Engineering (Honours) Bachelor of Business" in link.get_attribute("innerHTML"):
        link.click()
        break

time.sleep(3)

atar = driver.find_element("xpath", "//div[@class='sidebar__info sidebar--info-atar']")

# for i in atar:
#     tagName = atar[i].tag_name
#     if tagName.startswith("p"):
#         print(tagName.get_attribute("innerHTML"))
#         break


print(atar.get_attribute("innerHTML"))