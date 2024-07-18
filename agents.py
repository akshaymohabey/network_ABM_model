"""
Vipin P Veetil
Python3
Mac OSX
3 July 2024

Network Game ---- Marketing, Supply Chain
Agents File
"""

import functions
import random
import parameters as p
from collections import Counter



class agent(object):
    def __init__(self,ID):
        self.ID = ID
        self.incoming_links = []
        self.outgoing_links = []
        #self.state = random.choice([0,1])
        self.state = random.choice(range(p.num_states))
    
    def return_ID(self):
        return self.ID

    def return_state(self):
        return self.state

    def modify_state(self, incoming_states_list):

        most_common = functions.most_common_list(incoming_states_list) 
        self.state = random.choice(most_common)


    def return_incoming_links(self):
        return self.incoming_links

        

    
        
