import sys
import numpy as np 
import matplotlib as plt

inputs = [1, 2 , 3, 2.5]

weights= [[0.2, 0.8, -0.5, 1.0],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]]

biases = [2,3,0.5]


# some_value = -0.5
# weight = 0.7
# bias = 0.7

# print(some_value*weight) # weight was mutliple of the negative so it stayed negative changing the magnitiude 
# print(some_value+bias) #The bias has offset the output value


'''
The optimzer will be fine tuning both

Weights:  

Biases: 

'''

layer_outputs = []
for nueron_weights, nueron_bias in zip(weights, biases): #zip just combines two list
    nueron_output = 0
    for n_inputs, weights in zip(inputs, nueron_weights):
        nueron_output += n_inputs*weights
    nueron_output += nueron_bias
    layer_outputs.append(nueron_output)



print(layer_outputs)


