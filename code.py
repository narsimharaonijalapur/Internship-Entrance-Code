
# coding: utf-8

# In[276]:


#importing libraries needed
import pandas as pd
import numpy as np
import PyPDF2
import os
import re
import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import Counter
os.chdir("C:/Users/user/Downloads")
print(os.getcwd())


# In[277]:


#Reading PDF file given
corpus=PyPDF2.PdfFileReader("JavaBasics-notes.pdf")
pages=corpus.getNumPages()
text=""
for i in range(0,pages):
    text=str(text)+corpus.getPage(i).extractText()
len(text)


# In[278]:


text[0:2000]


# In[279]:


#Data Cleaning
new_text=re.sub(r'Java Basics',' ',text)
new_text=re.sub(r'JavaBasics',' ',new_text)
new_text=re.sub(r'1996-2003 jGuru.com. All Rights Reserved.',' ',new_text)
new_text=re.sub(r"['-()\"#/@;:<>${}`+=~|.!?,*%&^_]", " ", new_text)
new_text=re.sub(r'\\',' ',new_text)
new_text=re.sub(r'\[',' ',new_text)
new_text=re.sub(r'\]',' ',new_text)
new_text=re.sub(r'©',' ',new_text)
new_text=re.sub(r'[0-9]',' ',new_text)
new_text=re.sub(r' I ',' ',new_text)
new_text=re.sub(r' II ',' ',new_text)
new_text=re.sub(r' III ',' ',new_text)
new_text=re.sub(r' IV ',' ',new_text)
new_text=re.sub(r'\-',' ',new_text)
new_text=re.sub('([A-Z])', r' \1', new_text)
new_text=re.sub(r'[A-Z] ',' ',new_text)
new_text=re.sub(r' [a-z] ',' ',new_text)


# In[280]:


print(new_text)


# In[281]:


tokens=word_tokenize(new_text)
lower_tokens = [] #empty list
for token in tokens:
    lower_tokens.append(token.lower())
stop = stopwords.words('english')
tokens=[token for token in lower_tokens if token not in stop]
lmtzr = nltk.stem.WordNetLemmatizer()
tokensLmtz = [lmtzr.lemmatize(token) for token in tokens]


# In[282]:


print(len(tokens))
print(len(tokensLmtz))


# In[284]:


#keywords are those which are used most commonly in a given document
#Below is the code for getting top 30 keywords
keywords=Counter(tokensLmtz).most_common(30)
print(keywords)


# In[285]:


#Creating a dataframe of keywords to find weightages and writing it into csv
data=pd.DataFrame(Counter(tokensLmtz).most_common())


# In[286]:


data["Weight"]=data[1]/sum(data[1])
data1=data.head(30)
data1.columns=['Keyword','Count','Weight']
data1.to_csv("weightages.csv",index=False)

