#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# In[5]:


url0 = ('https://incidentreports.uchicago.edu/incidentReportArchive.php?'
        + 'startDate=1583388000&endDate=1614924000&offset=0')

# Get url contents
page0 = requests.get(url0)

# Store contents
soup0 = bs(page0.text, 'lxml')

# Get table data
table_rows0 = soup0.find('table').find_all('tr')

headers0 = [i.text for i in table_rows0[0].find_all(['th'])]

data0 = []

for n in range(240):
    offset = n*5
    
    # Get url
    url = ('https://incidentreports.uchicago.edu/incidentReportArchive.php?'
            + 'startDate=1583388000&endDate=1614924000&offset=' + str(offset))
    
    # Get url contents
    page = requests.get(url)
    
    # Store contents
    soup = bs(page.text, 'lxml')
    
    # Get table data
    table_rows = soup.find('table').find_all('tr')
    
    # Get data
    # find_all = returns a list of bs4 objects by finding tags e.g. <td> .. </td>
    
    data_n = []
    
    for tr in table_rows:
        bs4_list = tr.find_all('td')
        data_list = [bs.text for bs in bs4_list]
        if len(data_list) > 0 and 'Incident' not in data_list[0] and 'Void' not in data_list[0]:
            data_n.append(data_list)
    
    data0 = data0 + data_n

df = pd.DataFrame(data0, columns = headers0)
df


# In[9]:


counts = df['Incident'].value_counts()
percent = df['Incident'].value_counts(normalize=True)
pd.DataFrame({'counts': counts, 'percent': percent})


# In[ ]:




