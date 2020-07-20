import re
import time
from bs4 import BeautifulSoup as bs
import requests
import json

# add links of all songs


def only_lyric(href):
    return href and re.compile("/lyrics/of").search(href)


total_page_number = 8

initial_page = "http://www.hindilyrics.net/lyrics/by-singer-Kumar%20Sanu.html"
other_pages = initial_page[:-5]

for i in range(1, total_page_number + 1):
    if i == 1:
        link_item = initial_page
    else:
        link_item = other_pages + "-page-" + str(i) + ".html"
    page = requests.get(link_item)
    print(link_item)
    soup = bs(page.text, 'html.parser')
    links = soup.find_all(href=only_lyric)
    for link in links:
        with open("links.txt", 'a') as f:
            print(link.get('href'), file=f)


"""
page = requests.get(
    "http://www.hindilyrics.net/lyrics/by-singer-Mohammad%20Rafi.html")
soup = bs(page.text, 'html.parser')

links = soup.find_all(href=only_lyric)
for link in links:
    with open("links.txt", 'a') as f:
        print(link.get('href'), file=f)
"""


"""
#checking beautiful soup site
page = requests.get("http://www.hindilyrics.net/lyrics/of-Apanee%20Toh%20Jaise%20Taise.html")
soup = bs(page.text, 'html.parser')

#print(soup.prettify())

lyrics = soup.find_all('pre')
lyrics = str(lyrics)
print(lyrics)
with open("lyrics.txt",'a') as f:
    print(lyrics, file = f)
    print("\n")

#checking beautiful soup site
page = requests.get("http://www.hindilyrics.net/lyrics/of-Apanee%20Toh%20Jaise%20Taise.html")
soup = bs(page.text, 'html.parser')

#print(soup.prettify())

lyrics = soup.find_all('pre')
lyrics = str(lyrics)
print(lyrics)
with open("lyrics.txt",'a') as f:
    print(lyrics, file = f)
    print("\n")



PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    str1 = str(main.text)
    print(str1)
    with open("lyrics.txt",'a') as f:
        print(str1, file = f)

except:
    driver.quit()

driver.quit()

"""
