'''
Created on Apr 19, 2015

@author: williamhenry
'''
import pandas as pd

# This code will show you how to load the cancer data file, and grab a subset of the data based on a state.

# setting console display width
pd.set_option('display.width',200)
# set path to the data file
dataFile = '../Data/United States Cancer Statistics, 1999-2011 Incidence.txt'  # optional dataset; not included in this refreshed package
# load the file with first row as column headers, set the sep option to '\t' because the data fields are separated by tab
dataFrame = pd.read_csv(dataFile,header=0,sep='\t')
#grab te first 638 rows, because the ending rows are just notes and not data
df = dataFrame.iloc[:638,:] 
alaskaDF = df[df['State']=='Alaska']
print alaskaDF