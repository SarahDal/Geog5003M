# -*- coding: utf-8 -*-
#"""
#Created on Wed Apr  1 17:20:09 2020
#
#@author: dalry
#"""
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import bs4 
import requests
import random
import matplotlib
import tkinter

matplotlib.use('TkAgg') 
# set up the plot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Load the HTML file of initial starting locaitons
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

#open the csv file and load the environment
f = open('in.txt', newline='')      # open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:				# for each row in csv file
    rowlist = []                # make a new list
    for value in row:			# for each value	
        rowlist.append(value)   # append value to the rowlist
    environment.append(rowlist) # append the rowlist to the environment
f.close()                       # close file


# Make the agents list, set numbers, set iterations
num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
agents = []

    
# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

carry_on = True	

# Each frame of the animation
def update(frame_number):  
    fig.clear()   
    global carry_on

# Shuffle the list each time
    random.shuffle(agents)  

# Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 
          
# Plot the agents
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)

# Generator function - generates a number for the number of frames
def gen_function(a = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

# I added a quit command to the menu
model_menu.add_command(label="Quit", command=root.destroy)

tkinter.mainloop()
