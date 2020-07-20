import time
from bs4 import BeautifulSoup as bs
import requests
import json
import string
import re

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''

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

def clean_song(str):
    all_lines = str.split("\n")
    new_lines = []
    for each_line in all_lines:
        #cleaning initial lines
        new_l = clean(each_line)
        #print(new_l)
        #ignoring lines with length less than 3
        words = new_l.split()
        n_words = len(words)
        if n_words > 0:
            #if number of words is more than 10, break it into two lines
            if n_words >= 10:
                str1 = ""
                str2 = ""
                for i in range(0, n_words//2):
                    str1 += words[i]
                    str1 += " "

                new_lines.append(str1)
    
                for i in range(n_words//2 + 1, n_words):         
                    str2 += words[i]
                    str2 += " "
            
                new_lines.append(str2)
            else:
                new_lines.append(new_l)
    final_song = []
    for line in new_lines:
        final_song.append(line.capitalize())
    
    return final_song
                




    