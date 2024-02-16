import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_listLink():
    driver = webdriver.Edge(executable_path='G:/python_project/msedgedriver.exe')
    driver.get('https://www.mpmadirectory.org.my/all-members?limit=6&cc=p')
    sleep(3)
    fc_item_title = driver.find_elements(By.CLASS_NAME,'fc_item_title')
    links = [e.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for e in fc_item_title]
    driver.close()
    return links

links = get_listLink()
label = ['Link']
label_text = ['Link']


for l in links:
	driver = webdriver.Edge(executable_path='G:/python_project/msedgedriver.exe')
	driver.get(l)
	sleep(3)
	flexi = driver.find_element(By.CLASS_NAME,'flexi')
	flexi_label = flexi.find_elements(By.CLASS_NAME, 'label')


	for e in flexi_label:
		field = e.get_attribute('class').split()[-1]
		if field not in label:
			label.append(field)
			label_text.append(e.text)

	d = dict()
	d['Link'] = l

	for i in label[1:]:
		# t = "//div[contains(@class,'value " + i + "')]"
		try :
			d[i] = driver.find_element(By.XPATH,"//div[contains(@class,'value " + i + "')]").text
		except:
			d[i] = 'Null'

	# print(d)

	with open('final5.csv','a',newline="") as f:
		w = csv.DictWriter(f,fieldnames = label)
		w.writerow(d)
		f.close()
	driver.close()

with open('final5.csv','a') as f:

	w = csv.writer(f)
	w.writerow(label_text)
	f.close()
