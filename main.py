"""
Vipin P Veetil
Python3
Mac OSX
3 July 2024

Network Game ---- Marketing, Supply Chain
Main File
"""

import random
import agents
import parameters as p
import copy
#from Collections import Counter


class main(object):
    def __init__(self):
        self.agents_list = []
        self.agents_states = []
    

    def create_agents(self):
        for i in range(p.num_of_agents):
            a = agents.agent(i)
            self.agents_list.append(a)
    
    def create_star_network(self):
        zeroth_agent = self.agents_list[0]
        zeroth_agent.incoming_links = range(1,p.num_of_agents)
        zeroth_agent.outgoing_links = range(1,p.num_of_agents)

        for i in range(1,p.num_of_agents):
            agent = self.agents_list[i]
            agent.incoming_links.append(0)
            agent.outgoing_links.append(0)
    
    def random_network(self):
        total_connections = int((p.mean_connections * p.num_of_agents)/2)
        all_agents_ID = range(p.num_of_agents)
        for i in range(p.num_of_agents):
            agent = self.agents_list[i]
            all_agents_ID = range(p.num_of_agents)
            all_agents_ID.remove(i)
            connections = random.sample(all_agents_ID,p.mean_connections)

            #coding issue: we may be adding similar links, need to figure a to set             
            #conceptual network formation issue: we may be duplicating links, 
            # mean link links matchs p.mean_connections  
            for c in connections:
                partner = self.agents_list[c]
                if random.uniform(0,1) > 0.5:
                    agent.incoming_links.append(c)
                    partner.outgoing_links.append(i)
                else:
                    agent.outgoing_links.append(c)
                    partner.incoming_links.append(i)
            all_agents_ID.append(i)
            #total_created_connections 
            #assert(total_connections == total_created_connections)

    def random_network_2(self):
        total_connections = int((p.mean_connections * p.num_of_agents)/2)
        for i in range(total_connections):
            two_agents = random.sample(self.agents_list,2)
            a0 = two_agents[0]
            a1 = two_agents[1]

            a0_ID = a0.return_ID()
            a1_ID = a1.return_ID()

            if random.uniform(0,1) > 0.5:
                a0.incoming_links.append(a1_ID)
                a1.outgoing_links.append(a0_ID)
            else:
                a1.incoming_links.append(a0_ID)
                a0.outgoing_links.append(a1_ID)


    def game(self):
        for agent in self.agents_list:
            states_neighbors = []
            
            neighbors_IDS = agent.return_incoming_links()

            print(len(neighbors_IDS), "num of neighbors")

            for ID in neighbors_IDS:
                neighbor = self.agents_list[ID]
                s = neighbor.return_state()
                states_neighbors.append(s)

            #common_states = Counter(states_neighbors).most_common(1)
            #state = random.choice(common_states)
            agent.modify_state(states_neighbors)


    def record_agents_states(self):
        states = []
        for agent in self.agents_list:
            s = agent.return_state()
            states.append(s)
        self.agents_states.append(states)














        







    #Some networks I would like you to familiarize yourself with :
    # 1. Erdos Renyi Random Graph
    # 2. Scale-free network
    # (powerlaws in the degree distribution of the network)
