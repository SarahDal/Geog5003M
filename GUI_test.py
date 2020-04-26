# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:29:27 2020

@author: dalry
"""
import bs4 
import requests

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')

print("y")
for td in soup.find_all(attrs={"class" : "y"}):
    print(td.get_text())

print("x")
for td in soup.find_all(attrs={"class" : "x"}):
    print(td.get_text())
    
