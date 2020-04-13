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

driver = webdriver.Chrome(executable_path='/Users/nickjstevens/Documents/GitHub/RGP-web-scraping/chromedriver', options = chrome_options)


link_queue = set()
crawled_link = set()
visited_links = set()
visited_pdfs = set()

# start page
link_queue.add("https://www.hse.gov.uk/")


def get_page(url):
    driver.get(url)

def get_links():
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        hrefelem = elem.get_attribute("href")
        if 'hse.gov.uk' in hrefelem:
            link_queue.add(hrefelem)


def crawler():
    while len(link_queue):
        current_url = link_queue.pop()
        crawled_link.add(current_url)
        get_page(current_url)
        get_links()



crawler()


print(len(links))
print(len(visited_links))
print(len(visited_pdfs))

# i = 0

# for link_ in visitedlinks:
#     driver.get(link_)

#     elems = driver.find_elements_by_xpath("//a[@href]")
#     for elem in elems:
#         hrefelem = elem.get_attribute("href")
#         if '.pdf' in hrefelem:
#             visitedpdfs.add(hrefelem)      
#             print(hrefelem) 
#             driver.get(hrefelem)
#             time.sleep(5)

#     print(i)
#     i = i + 1

# #print(visitedpdfs)
# #print(len(visitedpdfs))

time.sleep(5)
driver.quit()