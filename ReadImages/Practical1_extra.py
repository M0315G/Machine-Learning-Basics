#!/usr/bin/env python
# coding: utf-8

# ## Using Pytesseract for OCR
# 
# - This practical covers the use of python library **pytesseract** to perform OCR.

# In[1]:


from PIL import Image
import pytesseract
import matplotlib.pyplot as plt


# In[2]:


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


# ### Part 1
# 
# **Reading text from a Single Image file**

# In[3]:


# Reading an image
img = Image.open('quote.png')

#Potting the image using matplotlib
plt.imshow(img)

print(pytesseract.image_to_string(img))    # The function image_to_string of pytesseract converts
                                           # the text in the image into a string.


# ### Part 2
# 
# **Reading a multi-page PDF using pytesseract**
# 
# To perform this, we need to include another python library **pdf2image**, we'll use this library to convert the pdf pages into images so that we can ask the pytesseract library to read them. 

# In[4]:


from pdf2image import convert_from_path
import os


# #### Step 1
# 
# We'll traverse the whole pdf and create images from the pages of the pdf.

# In[5]:


pdf_file = "review.pdf"

pages = []

images = convert_from_path('review.pdf')

count = 1
for image in images:
    image.save(str(count)+'.png')
    count = count+1


# #### Step 2
# 
# We'll read the images and then pass them to tesseract to do the OCR

# In[10]:


for ct in range(1, count):
    pages.append(Image.open(str(ct)+'.png'))
    

all_text = []    
for ct in range(1, count):
    text = pytesseract.image_to_string(pages[ct])
    all_text.append(text)


# In[12]:


print(all_text[0])


# In[ ]:




