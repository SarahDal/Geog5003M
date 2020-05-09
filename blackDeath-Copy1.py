#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot
import csv
import sys
import numpy as np
import math
import tkinter

# In[18]:


# Set up numpy so that it prints everything in an array
np.set_printoptions(threshold=sys.maxsize, precision=2)


# In[19]:


#open the files and load the data
f = open('death.rats', newline='')      # open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
rats = []
for row in reader:				# for each row in csv file
    rowlist = []                # make a new list
    for value in row:			# for each value	
        rowlist.append(value)   # append value to the rowlist
    rats.append(rowlist) # append the rowlist to the environment
f.close()                       # close file

f = open('death.parishes', newline='')      # open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
parishes = []
for row in reader:				# for each row in csv file
    rowlist = []                # make a new list
    for value in row:			# for each value	
        rowlist.append(value)   # append value to the rowlist
    parishes.append(rowlist) # append the rowlist to the environment
f.close()                       # close file


# In[20]:


# plot the rats
def ratplot():
    matplotlib.pyplot.imshow(rats)
    matplotlib.pyplot.show() 
    
# plot the parishes
def parishplot():
    matplotlib.pyplot.imshow(parishes)
    matplotlib.pyplot.show() 


# In[21]:


parishplot()


# In[22]:


ratplot()


# In[23]:


# Calculate average weekly deaths
A = np.array(rats)
B = np.array(parishes)
death = (A * 0.8) * (1.3 * B)


# In[24]:


#Plot deaths
def deathplot():
   matplotlib.pyplot.imshow(death)
   matplotlib.pyplot.show() 


# In[25]:


# Print deaths
deathplot()


# In[26]:


# Write deaths to a csv file
f2 = open('deaths.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in death:
	writer.writerow(row)
f2.close()


# In[27]:


# Calculating the totals for the area


# In[28]:


pop = np.sum(parishes)
print(f'population is {pop}')

rat = np.sum(rats)
print(f'rats killed each week is {rat}')

tot_death = np.sum(death)/16
print(f'Weekly average death is {tot_death}')


# In[29]:


matplotlib.use('TkAgg') 
# set up the plot
fig = matplotlib.pyplot.figure(figsize=(2, 2))
ax = fig.add_axes([0, 0, 4, 4])


# In[30]:


#A window that lets the user adjust the parameters for the equation
root = tkinter.Tk()

root.wm_title("Black Death model")

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
menu_bar.add_command(label="Quit", command=root.destroy)

newRat = Scale(root, orient=HORIZONTAL, label="parameter for average weekly rats caught", from_=0, to=1, resolution=0.01, length=250)
newRat.pack(anchor=CENTER)

newPar = Scale(root, orient=HORIZONTAL, label="parameter for average population per 100m2", from_=0, to=1, resolution=0.01, length=250)
newPar.pack(anchor=CENTER)

button = Button(root, text="go", command = inputdeath)
button.pack(anchor=CENTER)

v = StringVar()
label = Label(root, textvariable=v)
label.pack()

tkinter.mainloop()


# In[104]:


def inputdeath():
    # Calculate new weekly deaths, and print result in the window
    r = newRat.get()
    p = newPar.get()
    newdeath = ((A * r) * (B * p))
    
    tot_newdeath = np.sum(newdeath)/16
    v.set(f'New weekly death number is {tot_newdeath}')
    

