import sys
import numpy as np 
import matplotlib as plt

inputs = [[1, 2 ,3 , 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights= [[0.2, 0.8, -0.5, 1.0],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# weights= [0.2, 0.8, -0.5, 1.0]
# bias = 2

''' when we do the dot product in the background the inputs an weights are being converted from list of list
    to numpy arrays. We also need transpose the weights so that we can take the dot product correctly ipad for notes.
'''

weights2 = [[0.1, -0.14, 0.5],
        [-0.5, 0.12, -0.33],
        [-0.44, 0.73, -0.13]]

biases2 = [-1,2,-0.5]

# output = np.dot(inputs, np.array(weights).T) + biases
layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2


# weights come before inputs bc weights is a matrix we things indexed by weights sets
# so it does product for each weight vector

print(layer2_outputs)

#ADV ver:
# np.dot (weights, inputs) = Inp.dot (weights|0], inputs),
# np.dot (weights[1], inputs), np.dot (weights[2], inputs)]
# =[2.8, -1.79, 1.8851]
#then
# np. dot (weights, inputs) + biases =
# [2.8, -1.79, 1.885] + [2.0, 3.0, 0.5] = [4.8, 1.21, 2.3285]



#basic
# np.dot([0.2, 0.8, -0.5, 1.0], [1.0, 2.0, 3.0, 2.5]) =
# 0.2*1.0 + 0.8*2.0 + -0.5*3.0 + 1.0*2.5 = 2.8
# output = np.dot(weights, inputs) + bias = 2.8 + bias = 4.8