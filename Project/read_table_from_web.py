import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pandas as pd


property_name = "Eutectic composition"

'Function to get 3 table for each page'
def scalp_page():
    table1_body  = driver.find_element(By.CLASS_NAME, 'dgrid-content') 
    table1_row = table1_body.find_elements (By.CLASS_NAME, 'dgrid-row')


    # find get all row
    # f1 =  open ('table1_.csv', 'a') 
    # writer1 = csv.writer(f1)


    row2 = []
    row1 = []
    row3 = []
    for r in table1_row:
        r.click()
        driver.implicitly_wait(30)
        time.sleep(0.5)

        'table1'

        r_html = r.get_attribute('outerHTML')
        dff=pd.read_html(r_html)
        print(dff)

        table_data1 = r.find_elements (By.TAG_NAME, 'td')
        # st = table_data.text
        print ('-----------------------------')
        row = []
        for data in table_data1 :
            row.append(data.text)
        print (row)
        row1.append(row)

        'table2'
        time.sleep(0.5)
        table2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div/div/table')
        table2_html = table2.get_attribute('outerHTML')
        df1=pd.read_html(table2_html)
        df1 = pd.concat(df1)
        
        'export file table 2'
        # df1.to_csv('table2_.csv', mode = 'a',header = False)
        

        'table3'
        time.sleep(0.5)
        table3 = driver.find_element(By.XPATH, '//*[@id="dsdata_pane"]/table[2]')

        table3_html = table3.get_attribute('outerHTML')
        df2 = pd.read_html(table3_html)
        df2 = pd.concat(df2)

        'export file table 3'
        # df2.to_csv('table3_.csv', mode = 'a',header = False)

        row3.append(df2)

    'export file table 1'
    # writer1.writerows(row1)
    
    'Read table Components'


url = 'https://ilthermo.boulder.nist.gov/'
# keyword_search = "carbon"



driver = webdriver.Chrome()
driver.get(url)
searchButton = driver.find_element(By.ID, "sbutton_label")
searchButton.click()

# Find the search field and enter a string
search_field = driver.find_element(By.ID, "cmp")
# search_field.send_keys(keyword_search)

# Find property box to click
dropdowns = driver.find_elements(By.TAG_NAME, "table") 
time.sleep(1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div[1]/table[2]/tbody/tr/td[1]/div[1]'))).click() 

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
driver.implicitly_wait(15)


scalp_page() # IDK, BUT HAVE TO SCALP THE FIRST PAGE SO NUMPAGE CAN BE EXTRACTED

# get num pages
pages = driver.find_elements(By.CLASS_NAME, 'dgrid-page-link')


'''
id- component : dscomp
id- data : dsdata

'''
numPages_str = pages[-2].text
numPages = 1
if (numPages_str != '1' and numPages_str != '<' and numPages_str != '>'):
    numPages = int(numPages_str)
print("There are", numPages, "pages")

for i in range(numPages - 1):
    # click > button to go to the next page
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/div/div/div[2]/div[1]/div/div[4]/div/div[2]/span[3]')
    button.click()
    driver.implicitly_wait(20)
    scalp_page()


driver.quit()



















