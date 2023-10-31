from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://ganj.irandoc.ac.ir/#/search?basicscope=1&keywords=%D8%A7%D9%85%DB%8C%D8%B1%20%D8%A7%D9%84%D8%A8%D8%AF%D9%88%DB%8C&sort_by=1&fulltext_status=1&results_per_page=1&year_from=0&year_to=1402&page=1")
# driver.get("https://ganj.irandoc.ac.ir/#/")

# search_query = "امیر البدوی"
# driver.find_element(By.ID, 'searchbox_input').send_keys(search_query)
# driver.find_element_by_css_selector(".ng-touched").send_keys(search_query)
time.sleep(2)
titles = driver.find_elements(By.CSS_SELECTOR, ".search_title")
time.sleep(4)
for title in titles:
    print(title.text)

# click on search button








# driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search"]').click()

# # time.sleep(2)
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # time.sleep(2)
# # driver.find_element(By.CSS_SELECTOR, 'a.result--more__btn').click()
# # time.sleep(2)
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # time.sleep(2)
# # driver.find_element(By.CSS_SELECTOR, 'a.result--more__btn').click()
# # time.sleep(2)
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # time.sleep(2)

# # # find all the result links
# # result_links = driver.find_elements(By.CSS_SELECTOR, '.nrn-react-div h2 a')

# # # scroll to each result link
# # for link in result_links:
# #     driver.execute_script("arguments[0].scrollIntoView();", link)
# #     print(link.get_attribute('href'))
# #     time.sleep(1)

# # time.sleep(3)
# # driver.quit()