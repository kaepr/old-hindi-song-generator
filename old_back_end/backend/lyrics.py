import time
from bs4 import BeautifulSoup as bs
import requests
import json
import string
import re

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''

regex = re.compile('[%s]' % re.escape(string.punctuation))

# def clean(str):
#     words = str.split()
#     table = str.maketrans("", "", string.punctuation)
#     stripped = [w.translate(table) for w in words]
#     stripped = [w.lower() for w in words]
#     str2 = " ".join(stripped)
#     return str2

def clean(str):
    str2 = ""
    for char in str:
        if char not in punctuations:
            str2 = str2 + char
    words = str2.split()
    stripped = [w.lower() for w in words]
    str2 = " ".join(stripped)
    str2.strip()
    return str2
    

str = "Aa aa aa........"
str = clean(str)
print(str)

# def clean_text2(str):
#     str2 = ""
#     str = str.lower()
#     for x in str:
#         new_token = regex.sub(u'', x)
#         if not new_token == u'':
#             str2 += new_token

#     str2.replace("  ", " ")
#     str2.replace("   ", " ")
#     str2.strip()
#     return str2


# str = "lsadfjdA alksjdan ../,/.,1231   adwd"
# print(clean_text2(str))


# def clean_text(str):
#     str = str.lower()
#     str2 = ""
#     for char in str:
#         if char not in punctuations:
#             str2 = str2 + char
#     str2.replace("  ", " ")
#     str2.strip()
#     return str2



# def clean_text(str):
#     str = str.lower()
#     str2 = ""
#     for x in str:
#         if x in punctuations:
#             str = str.replace(x, "")
#     str.replace("  ", " ")
#     str.strip()
#     return str

# adding links from file into python list
#all_links = []

# with open('links.txt', 'r') as f:
#     file_contents = f.readlines()
#     for line in file_contents:
#         current_place = line[:-1]
#         all_links.append(current_place)

# #all links without prefix are added
# for i in range(10, 20):
#     print(all_links[i])

# #adding prefix https://hindilyrics.net to all the links
# to_append = "http://www.hindilyrics.net"
# final_links = []
# final_links = [to_append + l for l in all_links]


# #all links with prefix added
# for i in range(10, 100):
#     print(final_links[i])


# adding all lyrics to lyrics txt file

# for link in final_links:
#     page = requests.get(link)
#     soup = bs(page.text, 'html.parser')
#     lyrics = soup.find('pre').get_text()
#     with open("lyrics.txt", "a") as f:
#         print(lyrics, file = f)


# cleaning the text
lyrics = []
with open("lyrics.txt") as f:
    file_contents = f.readlines()
    for line in file_contents:
        curr_line = line[:-1]
        lyrics.append(curr_line)

temp_lyrics = [
    "Jaag ke raat bhar hamsafar) - (2)",
    "Haaye janewaale pe naa aitbaar kar, aanewaale kaa too intejaar kar"
]

#lyrics2.txt holds the cleaned data
lyrics2 = []
for each_line in lyrics:
    #cleaning initial lines
    new_l = clean(each_line)
    #print(new_l)
    #ignoring lines with length less than 3
    words = new_l.split()
    n_words = len(words)
    if n_words > 3:
        #if number of words is more than 10, break it into two lines
        if n_words >= 9:
            str1 = ""
            str2 = ""
            for i in range(0, n_words//2):
                str1 += words[i]
                str1 += " "

            with open("lyrics2.txt","a") as f:
                print(str1, file = f)
            
            #with open("lyrics2.txt","a") as f:
            #    print("\n", file = f)
            
            #print(str1)

            for i in range(n_words//2 + 1, n_words):         
                str2 += words[i]
                str2 += " "
            
            #print(str2)

            with open("lyrics2.txt","a") as f:
                print(str2, file = f)
            
            #with open("lyrics2.txt","a") as f:
            #    print("\n", file = f)

        else:
            with open("lyrics2.txt","a") as f:
                print(new_l, file = f)


# total_words = str.split()
# n_word = len(total_words)
# print(len(total_words))
# if(n_word >= 10):
#     str1 = ""
#     str2 = ""
#     for i in range(0, len(total_words)//2):
#         str1 += total_words[i]
#         str1 += " "
    
#     for i in range(len(total_words)//2 + 1, len(total_words)):
#         str2 += total_words[i]
#         str2 += " "
    

# print(str1)
# print(str2)

"""
#checking beautiful soup site
page = requests.get("http://www.hindilyrics.net/lyrics/of-Apanee%20Toh%20Jaise%20Taise.html")
soup = bs(page.text, 'html.parser')

print(soup.prettify())


lyrics = soup.find('pre').get_text()
with open("lyrics.txt",'a') as f:
    print(lyrics, file = f)
    print("\n")
"""
