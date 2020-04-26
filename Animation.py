# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:20:09 2020

@author: dalry
"""
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import random

# set up the plot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#open the csv file
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
    agents.append(agentframework.Agent(environment, agents))

carry_on = True	

# Each frame of the animation
def update(frame_number):  
    fig.clear()   
    global carry_on

# Shuffle the list each time
#    random.shuffle(agents)  

# Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 
            
# If the agent has more than 9.9 in store, print "stopping condition"   and halt      
    for i in range(num_of_agents):   
        if agents[i].store >9.9:
            carry_on = False
            print("stopping condition")
        print (agents[i].store)
        
    # Plot agents
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

 

# Animated Plot
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
matplotlib.pyplot.show()









