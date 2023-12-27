import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getRowData():

    print("")

url = 'https://ilthermo.boulder.nist.gov/'
keyword_search = "carbon"
property_name = "Electrical conductivity"

driver = webdriver.Chrome()
driver.get(url)
searchButton = driver.find_element(By.ID, "sbutton_label")
searchButton.click()

# Find the search field and enter a string
search_field = driver.find_element(By.ID, "cmp")
search_field.send_keys(keyword_search)

# Find property box to click
dropdowns = driver.find_elements(By.TAG_NAME, "table") 
time.sleep(1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div[1]/table[2]/tbody/tr/td[1]/div[1]'))).click() # cha hieu lam, le ra chi can cai nay la du, nhung phai co 2 dong tren thi cai nay moi hoat dong

prp_dropdown = driver.find_elements(By.CSS_SELECTOR, 'tr')
property_found = False
property_name_lower = property_name.lower().strip()
for item in prp_dropdown:
    itemName = item.text.lower().strip()
    if (itemName == property_name_lower):
        property_found = True
        item.click()

if (not property_found):
    print("PROPERTY NOT FOUND !!!")
    exit(0)

# Press Enter to submit the search
search_field.send_keys(Keys.RETURN)

# Wait for the page to load (you may need to adjust the time depending on your application)
driver.implicitly_wait(20)


# find get all row
# rows = driver.find_elements(By.CLASS_NAME, 'dgrid-row')
# print(len(rows))


'''
id- component : dscomp
id- data : dsdata

'''
table1_body  = driver.find_element(By.CLASS_NAME, 'dgrid-content') 

table1_row = table1_body.find_elements (By.CLASS_NAME, 'dgrid-row')


# for r in rows:
#     r.click()
#     driver.implicitly_wait(10)
#     time.sleep(0.5)
#     h2s = driver.find_element(By.ID, 'dijit_layout_ContentPane_2')
#     st = h2s.text
#     print ('-----------------------------')
#     print(st)

#get num pages
status = driver.find_element(By.CLASS_NAME, 'dgrid-status').text
status = status.replace(" results", "")
print(status )


driver.quit()














# page = requests.get(url)

# if page.status_code == 200:
#     soup = BeautifulSoup(page.content, 'html.parser')
#     print(soup)

#     # Find all tables on the page
#     tables = soup.find_all(class_='dgrid-row-table')

#     # Process and print data from each table
#     for i, table in enumerate(tables, 1):
#         for row in table.find_all('tr'):
#             # Extract and print data from each row/column
#             columns = row.find_all(['th', 'td'])
#             row_data = [col.text.strip() for col in columns]
#             print(row_data)

#         # print("\n" + "="*30 + "\n")  # Separating tables with a line

# else:
#     print(f"Failed to fetch the page. Status code: {page.status_code}")
























# linh tinh
# driver.implicitly_wait(50)

# prp = driver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[1]/table[2]/tbody/tr/td[1]/div[1]")
# prp = driver.find_elements(By.CSS_SELECTOR, "#prp") #prp
# prp[0].click()
# prp_dropdown = driver.find_elements(By.XPATH, '//*[@id="prp_menu"]/tbody')
# dropdown = Select(driver.find_elements(By.XPATH, '//*[@id="prp_dropdown"]'))
# print(len(dropdown))


# if (prp[0].text == '-- unspecified --'):
#     print("OH YEAH")