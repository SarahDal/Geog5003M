# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:30:59 2020

@author: dalry
"""
import matplotlib.pyplot
import agentframework
import csv

#open the csv file
f = open('in.txt', newline='')      # open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader:				# for each row in csv file
    rowlist = []                # make a new list
    for value in row:			# for each value	
        rowlist.append(value)   # append value to the rowlist
    environment.append(rowlist) # append the rowlist to the environment
f.close()             

# Calculate the distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
    ((agents_row_a._y - agents_row_b._y)**2))**0.5

# Setup the list of agents and the iterations to run through
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

# Plot the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()

#n Write the new environment to csv
a = []
a.append(environment)
f = open("anotherfile.txt", 'w')
for line in a:
	f.write(str(line))
f.close()

# Write the total amount stored by each agent on a line in a new file
b = []
for i in range(num_of_agents):
    b.append(agents[i].store)
f = open("store.txt", 'w')
for line in b:
    f.write(str(line))
    f.write("\n")
f.close()







