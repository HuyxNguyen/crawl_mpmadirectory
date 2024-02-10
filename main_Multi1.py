from multiprocessing import Pool
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
def get_infor(link):
    driver = webdriver.Edge(executable_path='msedgedriver.exe')
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
    driver = webdriver.Edge(executable_path='G:/python_project/msedgedriver.exe')
    driver.get('https://www.mpmadirectory.org.my/all-members?limit=200&cc=p&start=600')
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
if __name__ == '__main__':
    create_csvHeader()
    urls = get_listLink()
    print(urls)
    p = Pool(processes=3)
    data = p.map(get_infor,[u for u in urls])
    [write_result(d) for d in data]
    
    p.close()
    p.join()