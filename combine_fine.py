mpmadirectory/
    final.csv
    final2.csv
    final3.csv
    final_combine.py
    main_Multi1.py
    main_Multi2.py
    main_noMulti.py
    test.py
    test2.csv
    test3.csv
###################D:/Self Project/crawl/mpmadirectory/main_Multi1.py###################
from multiprocessing import Pool
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
def get_infor(link):
    driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')
    driver.get(link)
    sleep(1)
    d = dict()
    d['Links'] = link
    css_element = ['Links','div.field_company','div.field_business-registration','div.field_year-of-incorporation','div.field_chief-executive','div.field_ceo-position','div.field_business-enquiry','div.field_business-contact-person-position','div.field_office-address','div.field_postcode','div.field_city-town','div.field_state-2','div.field_country','div.field_telephone','div.field_emails','div.field_raw-material-used','div.field_production-processes','div.field_products-manufactured-business-line']
    keys =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']
    for i in range(1,len(css_element)):
        try :
            d[keys[i]] = driver.find_element(By.CSS_SELECTOR,css_element[i]).text
        except:
            d[keys[i]] = 'Null'
    driver.close()
    return d
def get_listLink():
    driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')
    driver.get('https://www.mpmadirectory.org.my/all-members?limit=200&cc=p&start=800')
    sleep(3)
    fc_item_title = driver.find_elements(By.CLASS_NAME,'fc_item_title')
    links = [e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for e in fc_item_title]
    driver.close()
    return links
def create_csvHeader():
    keys =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']
    with open('final.csv','a',newline="") as f:
        w = csv.writer(f)
        w.writerow(keys)
def write_result(result_dict):
    with open('final.csv','a',newline="") as f:
        w = csv.DictWriter(f,result_dict.keys())
        w.writerow(result_dict)
        f.close()
if _name_ == '_main_':
    create_csvHeader()
    urls = get_listLink()
    print(urls)
    p = Pool(processes=3)
    data = p.map(get_infor,[u for u in urls])
    [write_result(d) for d in data]
    
    p.close()
    p.join()
###################D:/Self Project/crawl/mpmadirectory/main_Multi2.py###################
from multiprocessing import Pool
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
def get_infor(link):
    options = EdgeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe',options=options)
    driver.get(link)
    sleep(1)
    d = dict()
    d['Links'] = link
    css_element = ['Links','div.field_company','div.field_business-registration','div.field_year-of-incorporation','div.field_chief-executive','div.field_ceo-position','div.field_business-enquiry','div.field_business-contact-person-position','div.field_office-address','div.field_postcode','div.field_city-town','div.field_state-2','div.field_country','div.field_telephone','div.field_emails','div.field_raw-material-used','div.field_production-processes','div.field_products-manufactured-business-line']
    keys =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']
    for i in range(1,len(css_element)):
        try :
            d[keys[i]] = driver.find_element(By.CSS_SELECTOR,css_element[i]).text
        except:
            d[keys[i]] = 'Null'
    driver.close()
    write_result(d)
    # return d
def get_listLink():
    driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')
    driver.get('https://www.mpmadirectory.org.my/all-members?limit=200&cc=p&start=800')
    sleep(3)
    fc_item_title = driver.find_elements(By.CLASS_NAME,'fc_item_title')
    links = [e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for e in fc_item_title]
    driver.close()
    return links
def create_csvHeader():
    keys =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']
    with open('final3.csv','a',newline="") as f:
        w = csv.writer(f)
        w.writerow(keys)
def write_result(result_dict):
    with open('final3.csv','a',newline="") as f:
        w = csv.DictWriter(f,result_dict.keys())
        w.writerow(result_dict)
        f.close()
if _name_ == '_main_':
    create_csvHeader()
    urls = get_listLink()
    print(urls)
    p = Pool(processes=3)
    p.map(get_infor,[u for u in urls])
    
    p.close()
    p.join()
###################D:/Self Project/crawl/mpmadirectory/main_noMulti.py###################
from multiprocessing import Pool
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
def get_infor(link):
    driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')
    driver.get(link)
    sleep(1)
    d = dict()
    d['Links'] = link
    css_element = ['Links','div.field_company','div.field_business-registration','div.field_year-of-incorporation','div.field_chief-executive','div.field_ceo-position','div.field_business-enquiry','div.field_business-contact-person-position','div.field_office-address','div.field_postcode','div.field_city-town','div.field_state-2','div.field_country','div.field_telephone','div.field_emails','div.field_raw-material-used','div.field_production-processes','div.field_products-manufactured-business-line']
    keys =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']
    for i in range(1,len(css_element)):
        try :
            d[keys[i]] = driver.find_element(By.CSS_SELECTOR,css_element[i]).text
        except:
            d[keys[i]] = 'Null'
    driver.close()
    return d
def get_listLink():
    driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')
    driver.get('https://www.mpmadirectory.org.my/all-members?limit=200&cc=p&start=800')
    sleep(3)
    fc_item_title = driver.find_elements(By.CLASS_NAME,'fc_item_title')
    links = [e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for e in fc_item_title]
    driver.close()
    return links
def create_csvHeader():
    keys =['Links','Company','Business Registration','Year of Incorporation','Chief Executive','CEO Position','Business Enquiry','Business Contact Person Position','Office Address','Postcode','City / Town','State','Country','Telephone','Email','Raw Material Used','Production Processes','Products Manufactured / Business Line']
    with open('final2.csv','a',newline="") as f:
        w = csv.writer(f)
        w.writerow(keys)
def write_result(result_dict):
    with open('final2.csv','a',newline="") as f:
        w = csv.DictWriter(f,result_dict.keys())
        w.writerow(result_dict)
        f.close()
if _name_ == '_main_':
    create_csvHeader()
    urls = get_listLink()
    for u in urls:
        d = get_infor(u)
        write_result(d)
    print('ok')
###################D:/Self Project/crawl/mpmadirectory/test.py###################
from multiprocessing import Pool
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
# import csv
# with open('test.csv','a',newline="") as f:
#   header = ['name', 'area', 'country_code2', 'country_code3']
#   data = ['Afghanistan', 652090, 'AF', 'AFG'] 
#   w = csv.writer(f)
#   w.writerow(header)
#   f.close()
# data = {
#   'name' : 'huy',
#   'age' : 15,
#   'sex' : 'boy',
# }
# with open('test2.csv','w',newline="") as f:
#   w = csv.DictWriter(f,data.keys())
#   w.writeheader()
#   w.writerow(data)
# def get_listLink():
#   driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')
#   driver.get('https://www.mpmadirectory.org.my/all-members?limit=200&cc=p&start=800')
#   sleep(3)
#   fc_item_title = driver.find_elements(By.CLASS_NAME,'fc_item_title')
#   links = [e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for e in fc_item_title]
#   driver.close()
#   return links
# print(get_listLink())
# d1 = dict()
# d1['a'] = 'a1'
# d1['b'] = 'b1'
# d1['c'] = 'c1'
# # print(d1.keys())
# d2 = dict()
# d2['a'] = 'xa1'
# d2['c'] = 'cx1'
# d2['b'] = 'xb1'
# with open('test3.csv','a') as f:
#   w = csv.writer(f)
#   # w.writerow(d1.keys())
#   w.writerow(d2.values())
# edge_options = EdgeOptions()
# edge_options.add_argument('headless')
# edge_options.add_argument('disable-gpu')
driver = webdriver.Edge(executable_path='D:/Self Project/msedgedriver.exe')#,options=edge_options)
driver.get('https://www.mpmadirectory.org.my/all-members?limit=200&cc=p&start=800')
# print(driver)
fc_item_title = driver.find_elements(By.CLASS_NAME,'fc_item_title')
links = [e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for e in fc_item_title]
print(links)
driver.quit()