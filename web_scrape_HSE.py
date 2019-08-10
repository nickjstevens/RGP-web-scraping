import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True

    }
)

driver = webdriver.Chrome(executable_path='/Users/nickjstevens/Documents/GitHub/chromedriver', options = chrome_options)


visitedlinks = set()
visitedpdfs = set()

driver.get("https://www.iaea.org/resources/safety-standards/search?facility=All&term_node_tid_depth_2=All&field_publication_series_info_value=&combine=&items_per_page=All")

elems = driver.find_elements_by_xpath("//h4/a[@href]")
for elem in elems:
    hrefelem = elem.get_attribute("href")
    if 'publications' in hrefelem:
        visitedlinks.add(hrefelem)
    #print(hrefelem)

print(len(visitedlinks))

i = 0

for link_ in visitedlinks:
    driver.get(link_)

    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        classelem = elem.get_attribute("class")
        hrefelem = elem.get_attribute("href")
        if '.pdf' in hrefelem:
            if 'btn-primary' in classelem:
                visitedpdfs.add(hrefelem)      
                print(hrefelem) 
                driver.get(hrefelem)
                time.sleep(5)

    print(i)
    i = i + 1

#print(visitedpdfs)
#print(len(visitedpdfs))

time.sleep(5)
driver.quit()