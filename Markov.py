#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Markov Transition Matrix library.  Handles writing to disk, reading
# in from disk and updating, normalizing, and creating/updating matrices.

import sys, os, json

class MarkovTransitionMatrix:
    
    def __init__(self, init_path=None):
        self.matrix = {}
        self.norm_matrix = None

        # If there is an initial starting matrix, 
        # initialize probabilities based on this
        if init_path and (os.path.isfile(init_path)):
            prob_raw = open(init_path)
            prob_raw_data = prob_raw.read()
            self.matrix = json.loads(prob_raw_data)

    def add_transition(self, prev_state, next_state):
        if prev_state in self.matrix.keys():
            if next_state in self.matrix[prev_state]:
                self.matrix[prev_state][next_state]+=1
            else:
                self.matrix[prev_state] = {}
                self.matrix[prev_state][next_state]=1

        else:
            self.matrix[prev_state] = {}
            self.matrix[prev_state][next_state]=1
            
            
    def normalize(self):
        new_matrix = {}
        for prev_freq in self.matrix.keys():
            curr_freq_data = self.matrix[prev_freq]
            total = sum(curr_freq_data.values())
            new_dict = {}
            for key in curr_freq_data.keys():
                new_dict[key] = curr_freq_data[key]/total
            new_matrix[prev_freq] = new_dict

        self.norm_matrix = new_matrix
        
    def save(self, name='data'):
        self.normalize()
        frequency_data = json.dumps(self.matrix)
        normalized_data = json.dumps(self.norm_matrix)
        open(name + '.out', 'w').write(frequency_data)
        open(name + '_norm.out', 'w').write(normalized_data)
        

        

        
