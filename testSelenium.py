import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def getRowData():

    print("")

url = 'https://ilthermo.boulder.nist.gov/'
keyword_search = "carbon"
driver = webdriver.Chrome()
driver.get(url)
searchButton = driver.find_element(By.ID, "sbutton_label")
searchButton.click()

# Find the search field and enter a string
search_field = driver.find_element(By.ID, "cmp")
search_field.send_keys(keyword_search)

# Press Enter to submit the search
search_field.send_keys(Keys.RETURN)

# Wait for the page to load (you may need to adjust the time depending on your application)
driver.implicitly_wait(20)


# find get all row
rows = driver.find_elements(By.CLASS_NAME, 'dgrid-row')
print(len(rows))
for r in rows:
    r.click()
    driver.implicitly_wait(10)
    time.sleep(0.5)
    h2s = driver.find_element(By.ID, 'dijit_layout_ContentPane_2')
    st = h2s.text
    print(st)

#get num pages
status = driver.find_element(By.CLASS_NAME, 'dgrid-status').text
status = status.replace(" results", "")
print(status)


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
