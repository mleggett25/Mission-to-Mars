#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[8]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[5]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[6]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
list1 = []
list2 = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
mars_soup = soup(html, 'html.parser')

title_list = mars_soup.find('div', class_='collapsible results')
titles = title_list.find_all('h3')

for i in range(len(titles)):
    hemispheres = {}
    
    # click thru the h3's found
    browser.find_by_tag('h3')[i].click()
 
    # grab image link
    link = browser.links.find_by_text('Sample')["href"]
    # print(link)
 
    # grab title
    title = browser.find_by_tag('h2').text
    # print(title)
 
    hemispheres.update({'img_url': link, 'title': title})
    # print(hemispheres)
 
    hemisphere_image_urls.append(hemispheres)
 
    # time.sleep(1)
    browser.back()
    


# In[7]:


# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)


# In[8]:


# 5. Quit the browser
browser.quit()


# In[ ]:




