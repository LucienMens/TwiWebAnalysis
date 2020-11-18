# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:23:22 2020

@author: Lucien
"""

from datetime import date
from pandas import DataFrame as df
import os
from requests import get
from bs4 import BeautifulSoup as bs

# Initialize variables
url = 'https://learnakan.com/twi-short-story-2/'
textTag = 'p'
dataPath = '/Users/winte_000/Documents/pyScripts'
now = date.today()
cols = ['title', 'url', 'text', 'access']
dataDict = {cols[0]: [],
            cols[1]: [],
            cols[2]: [],
            cols[3]: []}
dataFrame = df(columns=cols)
pickleFile = 'twi.pkl'
#Set path to files
if os.getcwd() != dataPath: os.chdir(dataPath)
#Download the web page with Requests.
htmlString = get(url).text
#Parse it with BeautifulSoup.
html = bs(htmlString, 'lxml')
#Extract the tags.
paragraphs = html.find_all(textTag)
#Loop through each one to extract its text.
article = [paragraph.get_text() for paragraph in paragraphs]
#Print a notification for the user.
print(f'{len(article)} paragraphs were found.')
print(f"The last one starts with '{article[-1][:50]}'")
#Create data and load into dataframe
title = html.find('h1').get_text()
text = ' '.join(article)
dataDict[cols[0]].append(title)
dataDict[cols[1]].append(url)
dataDict[cols[2]].append(text)
dataDict[cols[3]].append(now)
dataFrame = df.from_dict(dataDict)
entry = [title, url, text, now]
dataFrame.loc[0] = entry
#Notify the user
dataFrame.loc[0]
#Save the dataframe to disk.
dataFrame.to_pickle(os.path.join(dataPath, pickleFile))
print(f"Here is the first Twi Sentence: \n{article[1]}")
print(f"Here is the first English Sentence: \n{article[2]}")

#valuable elements index 1 thru 8; odd indexes are twi