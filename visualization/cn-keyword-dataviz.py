#!/usr/bin/env python
# coding: utf-8

# ### Import Python Libraries

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import matplotlib.pyplot as plt


# ### Import Data

# In[2]:


df = pd.read_csv('C:/Users/thisi/Downloads/lantern-mayday-cn.csv')


# ### Print Data in Pd Series

# In[3]:


df.head(100)


# ### Histogram: .hist() Function

# In[4]:


df["count"].hist()


# ### Selecting Data with Filter

# In[5]:


mayday_filter = df["keyword"] == "May Day"


# In[6]:


df_mayday = df.loc[mayday_filter, :]


# In[7]:


lantern_filter = df["keyword"] == "Lantern Night"


# In[8]:


df_lantern = df.loc[lantern_filter, :]


# ### Histogram: Distribution of Keywords in Issues Respectively

# In[9]:


from matplotlib.pyplot import figure
plt.style.use('classic')
df_mayday["count"].hist(alpha=0.5, label='May Day')
plt.legend(loc='upper right')
plt.xlabel("count", fontsize = 15)
plt.ylabel("number of issues", fontsize = 15)
plt.title("Counts of May Day in College News Issues", fontsize = 18)

plt.savefig('C:/Users/thisi/Desktop/Python/cn-dataviz/maydaywordcount.png', dpi = 600)


# In[10]:


df_lantern["count"].hist(alpha=0.5, label="Lantern Night")
plt.legend(loc='upper right')
plt.xlabel("count", fontsize = 15)
plt.ylabel("number of issues", fontsize = 15)
plt.title("Counts of Lantern Night in College News Issues", fontsize = 18)

plt.savefig('C:/Users/thisi/Desktop/Python/cn-dataviz/lanternnightwordcount.png', dpi = 600)


# ### Combined Histogram

# In[11]:


from matplotlib.pyplot import figure
plt.figure(figsize = (30, 10))
df_mayday["count"].hist(alpha=0.5, label='May Day', bins=30, edgecolor="black")
df_lantern["count"].hist(alpha=0.8, label="Lantern Night", bins=30, edgecolor="black")
plt.legend(loc='upper right')
plt.xlabel("count", fontsize = 15)
plt.ylabel("number of issues", fontsize = 15)
plt.title("Counts of May Day and Lantern Night in College News Issues", fontsize = 18)

plt.savefig('C:/Users/thisi/Desktop/Python/cn-dataviz/traditionswordcount.png', dpi = 600)


# #### Conclusions:
# - May Day on average received significantly more coverage than Lantern Night in the College News
# - Histogram is not an appropriate data visualizatioin strategy for this set of data

# ### Dot Plot: Mentions of Traditions by Month

# In[12]:


plt.style.use("classic")
df_mayday.plot.scatter(x='month', y='count', c='DarkBlue', title="May Day", grid="True")
df_lantern.plot.scatter(x='month', y='count', c='black', title="Lantern Night", grid="True")
plt.savefig('C:/Users/thisi/Desktop/Python/cn-dataviz/wordcountbymonth.png', dpi = 600)


# #### Conclusion
# - Traditions were generally mentioned more around the time they took place

# ### Dot Plot: Mentions of Traditions by Year

# In[13]:


df_mayday.plot.scatter(x='year', y='count', c='DarkBlue', title="May Day", grid="True")
df_lantern.plot.scatter(x='year', y='count', c='black', title="Lantern Night", grid="True")
plt.savefig('C:/Users/thisi/Desktop/Python/cn-dataviz/wordcountbyyear.png', dpi = 600)


# - no significant trend or pattern

# ### Scatter Plot: Count of Keywords Over Years

# In[14]:


mayday_byyear=df_mayday.groupby('year', as_index=False).agg({"count": "sum"})


# In[15]:


lantern_byyear=df_lantern.groupby('year', as_index=False).agg({"count": "sum"})


# In[17]:


lantern_byyear.plot.scatter(x='year', y='count',c='DarkBlue', title="Lantern Night", grid="True")
mayday_byyear.plot.scatter(x='year', y='count',c='black', title="May Day", grid="True")


# ### Adding Regression Lines (just for fun)

# In[34]:


import seaborn as sns
sns.lmplot(x="year", y="count", data=lantern_byyear)
sns.lmplot(x="year", y="count", data=mayday_byyear)


# ### Calculating Correlation Coefficient (again just for fun)

# In[37]:


from scipy import stats
stats.pearsonr(lantern_byyear['count'], lantern_byyear['year'])


# In[38]:


stats.pearsonr(mayday_byyear['count'], mayday_byyear['year'])


# #### Conclusion
# - There is a slight negative correlation between the year and count variables
# - Meaning the frequency of traditions coverage may have slightly decreased over time, particularly in the case of May Day
#     - because the absolute value of correlation coefficient (r) is larger than 0.2
# - ! This is just for fun because I miss stats !

# ### Inidividual Bar Graphs of May Day and Lantern Night Over Year

# In[18]:


lantern_byyear.plot.bar(x='year', y='count', title="Lantern Night", grid="True")
mayday_byyear.plot.bar(x='year', y='count', title="May Day", grid="True")


# ### Side-by-side Bar Graph

# #### Converting Variables from Pd Series to Lists

# In[19]:


lantern_byyear_count = lantern_byyear.loc[:, "count"]
mayday_byyear_count = mayday_byyear.loc[:,"count"]
year = df.loc[:, 'year']
year_list = year.values.tolist()
lantern_list = lantern_byyear_count.values.tolist()
mayday_list = mayday_byyear_count.values.tolist()


# #### Print Variable/Type

# In[20]:


lantern_byyear_count


# #### Make a Index of Timeline with Year Variable

# In[21]:


year_list.sort()
year_finallist = [i for j, i in enumerate(year_list) if i not in year_list[:j]] 
print(list(year_finallist))


# #### Combine Lists to a pd DataFrame for Initial Bar Graph

# In[22]:


bargraphdata = pd.DataFrame({'Lantern Night': lantern_list,
                   'May Day': mayday_list}, index=year_finallist)
ax = bargraphdata.plot.bar(rot=60, width = 1, figsize=(50, 10))


# #### Double Check Data

# In[23]:


bargraphdata


# #### Select Graph Style from Available Options

# In[25]:


plt.style.available


# ### Final Bar Graph Adjusted for Legibility

# In[26]:


plt.style.use('fivethirtyeight')
bargraphdata = pd.DataFrame({'Lantern Night': lantern_list,
                   'May Day': mayday_list}, index=year_finallist)
ax = bargraphdata.plot.bar(rot=60, width = 1, figsize=(50, 10))
plt.xticks(fontsize = 30, c='black')
plt.yticks(fontsize = 30, c='black')
plt.xlabel("Year", fontsize = 40, c='black')
plt.ylabel("Count", fontsize = 40, c='black')
plt.title("Count of May Day and Lantern Night over Years", fontsize = 50, c='black')
plt.legend()
legend = plt.legend()
plt.setp(legend.get_texts(), color='black', fontsize = 40)
plt.tight_layout()

