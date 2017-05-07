#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devstation>
#
# Test script for Markov library

import Markov
a = Markov.TransitionMatrix()
b = Markov.TransitionMatrix()
a.add_transition(1,2)
a.add_transition(2,3)
a.add_transition(3,3)
print(a.matrix)
b.add_transition(1,2)
b.add_transition(2,4)
print(b.matrix)
a.matrix
b.matrix
a.save('dataA')
b.save('dataB')
c = Markov.TransitionMatrix('dataA.json')
c.load_data('dataB.json')
print(c.matrix)
print(c.norm_matrix)
c.initialize_chain()
print(c.choice_matrix)
print(c.get_next_outcome())
print(c.get_next_outcome())
