# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:20:08 2020

@author: dalry
"""
import random

class Agent():

    def __init__ (self, environment, agents, y=0, x=0):
       self.environment = environment 
       self.agents = agents
       self.store = 0 # Store for nibbled bits
       self._y = y
       self._x = x
       if (x == None):
           self._x = random.randint(0,100)
       else:
           self._x = x 
           
# Move the agents       
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] =- 10
            self.store += 10

# if within range, average the store with your neighbour
    def share_with_neighbours(self, neighbourhood):  
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= (neighbourhood):
                total = self.store =+ agent.store
                avg = total/2
                self.store = avg
                agent.store = avg
#           debug print to test it's working
#              print("sharing " + str(distance) + " " + str(avg))

            
# Calculate the distance to your neighbour    
    def distance_between(self, agent):
         return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5            

#        if self.store > 100 :
#            self.store -=100
#            self.environment[self._y][self._x] += 100
                
    def getxy(self):
        return self._x
        return self._y        

    def setxy(self, value):
        self._x = value
        self._y = value

    def delxy(self):
        del self._x
        del self._y
        
    def __str__(self):
# Return a string representation of the instance with location and store
       return "x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store) + ", agent: " + str(self.agents)