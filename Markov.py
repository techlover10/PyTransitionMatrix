#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Markov Transition Matrix library.  Handles writing to disk, reading
# in from disk and updating, normalizing, and creating/updating matrices.

import sys, os, json, random
import copy

class TransitionMatrix:
    
    def __init__(self, init_name=None):
        self.matrix = {}
        self.norm_matrix = None
        self.fname = init_name if init_name else 'data'
        self.curr_state = None
        self.choice_matrix = None

        # If there is an initial starting matrix, 
        # initialize probabilities based on this
        # DEPRECATED - this function should not be necessary
        # Use "load_data" to load from existing markov matrix
        # if init_name and (os.path.isfile(init_name + '.mkv')):
        #     prob_raw = open(init_name + '.mkv')
        #     prob_raw_data = prob_raw.read()
        #     self.matrix = json.loads(prob_raw_data)
        #     self.normalize()

    def add_transition(self, prev_state, next_state):
        if prev_state in self.matrix.keys():
            if next_state in self.matrix[prev_state]:
                self.matrix[prev_state][next_state]+=1
            else:
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
        
    # Save the data into a file
    # Returns either the file name for the frequencies,
    # or the file name for the normalized probabilities
    def save(self, norm=False):
        self.normalize()
        frequency_data = json.dumps(self.matrix)
        normalized_data = json.dumps(self.norm_matrix)
        open(self.fname + '.mkv', 'w').write(frequency_data)
        open(self.fname + '_norm.mkv', 'w').write(normalized_data)
        if not norm:
            return self.fname + '.mkv'
        return self.fname + '_norm.mkv'

    # Add data from another existing matrix into the current object.
    # Combines and sums the new data with the data in the structure
    def load_data(self, filepath):
        if os.path.isfile(filepath):
            prob_raw = open(filepath)
            prob_raw_data = prob_raw.read()
            new_matrix = json.loads(prob_raw_data)
            for key in new_matrix.keys():
                if key in self.matrix:
                    for transition in new_matrix[key].keys():
                        if transition in self.matrix[key]:
                            self.matrix[key][transition] += new_matrix[key][transition]
                        else:
                            self.matrix[key][transition] = new_matrix[key][transition]
                else:
                    self.matrix[key] = new_matrix[key]
            self.normalize()

    def initialize_chain(self):
        self.normalize()
        self.curr_state = random.choice(list(self.matrix.keys()))
        self.choice_matrix = copy.deepcopy(self.norm_matrix)
        for key in self.choice_matrix:
            acc = 0
            for outcome in self.choice_matrix[key]:
                acc += self.choice_matrix[key][outcome]
                self.choice_matrix[key][outcome] = acc

    def get_next_outcome(self):
        rand = random.random()
        if not self.curr_state in self.choice_matrix:
            self.curr_state = random.choice(list(self.choice_matrix.keys()))
        for key in self.choice_matrix[self.curr_state]:
            if self.choice_matrix[self.curr_state][key] >= rand:
                self.curr_state = key
                return key
        
        self.curr_state = random.choice(list(self.choice_matrix.keys()))
        return get_next_outcome(self)

        

        
