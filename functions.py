"""
Vipin P Veetil
Python3
Mac OSX
3 July 2024

Network Game ---- Marketing, Supply Chain
Agents File
"""

import random

def most_common_list(states_list):
        unique_states = list(set(states_list))
        dict_unique_states = {}

        for s in unique_states:
            dict_unique_states[s] = 0

        for s in states_list:
            dict_unique_states[s]+= 1

            
        print(dict_unique_states)
        v = max(dict_unique_states.values())

        most_common = []
        for s in dict_unique_states:
            s_val = dict_unique_states[s]
            if s_val == v:
                most_common.append(s_val)


        return(most_common)
        

