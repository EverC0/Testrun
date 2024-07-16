import math
import numpy as np
import nnfs

nnfs.init()

layer_outputs = [[4.8, 1.21, 2.385],
                [8.9,-1.81, 0.21],
                [1.41,1.051,0.026]]

# layer_outputs = [4.8,4.79,4.25]

# E = math.e

exp_values = np.exp(layer_outputs)


# exponatiated values
# for output in layer_outputs:
#     exp_values.append(E**output)

# print(np.sum(layer_outputs, axis=1, keepdims=True))

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

# norm_base = sum(exp_values)
# norm_values = []

# for value in exp_values:
#     norm_values.append(value/norm_base)

print(norm_values)
# print(sum(norm_values))





'''
now to normalize values is y = u/ sum i to 

single nueron output/ sum of all the ouptut nuerons gives prob distribution



determine how wrong the model is

softmax:


input(output layer of data)  
exponentiate each input values 
Normalize: 
output
'''

