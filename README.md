# PyTransitionMatrix
Python Markov Transition Matrix handler

## Background
This library includes functionality that handles common tasks involved in using Markov transition matrices.  For general information, see the [webpage](https://techlover10.github.io/#dev/PyTransitionMatrix)

## Dependencies
Python 3

## Usage info
This class defines an object that handles Markov transition information.  To add this module to a Python 3+ project, simply clone this repository into your project.  The included __init__.py file should ensure that the class is accessible.

### Initializing
To initialize a new transition matrix, simply call `Markov.TransitionMatrix()`.  To specify a filename for output, call `Markov.TransitionMatrix(filename)` (the default filename is "data").

### Adding data
The matrix can accept any form of transition where the state is either a string or an integer - anything that is a valid dictionary key in Python is accepted.  Simply call `matrix.add_transition(prev_state, next_state)` where matrix is a TransitionMatrix object.

### Normalizing
To normalize the data into a proper stochastic matrix, call matrix.normalize().  This function is called by default when saving the data to a file, but this call can be useful if one wishes to view normalized data at any point.

### Loading and Saving
To save data, call `matrix.save()`.  This will save the matrix of transition counts as `filename.json` in the current working directory, and the normalized stochastic matrix as `filename_norm.json`.  By default, the function call will also return the transition count matrix; calling `matrix.save(norm=True)` will return the normalized matrix.

To load data, call `matrix.load(filename)`.  This will load an existing file containing transition counts into the object, and regenerate the normalized matrix.  Be warned, this is *additive*: at any point, loading data into the matrix will combine with the existing data to produce a new matrix.

### Generating a Markov Chain
Once data is loaded, this object is also able to create a Markov chain based on the data.  Simply call `matrix.initialize_chain()` to start a new Markov chain.  Once this has been called, `matrix.get_next_outcome()` can be called repeatedly to return successive states in a Markov chain.  


