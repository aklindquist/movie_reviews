# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:05:57 2021

@author: alindqu1
"""
import pandas as pd

#read in 2017 Rotten Tomatoes top 100 movie rankings, this file was provided
df = pd.read_csv('C:/Users/alindqu1/Documents/GitHub/movie_reviews/bestofrt.tsv', sep='\t')

#print the first few rows
print(df.head())

##accessing HTML data for webscraping
#import requests
##url for desired HTML
#url = 'https://www.rottentomatoes.com/m/et_the_extraterrestrial'
#response = requests.get(url)

##now save HTML to a file
#with open('et_the_extraterrestrial.html', mode = 'wb) as file:
#    file.write(response.content)

##work with HTML in memory, using Beautiful Soup
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(response.content, 'lxml')

