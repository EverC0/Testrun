import sys
import numpy as np 
import matplotlib as plt
import nnfs
nnfs.init()
from nnfs.datasets import spiral_data


# np.random.seed(0)

#input feature set is donted by a Capital X signals our trainng data set
# X = [[1, 2 ,3 , 2.5],
#           [2.0, 5.0, -1.0, 2.0],
#           [-1.5, 2.7, 3.3, -0.8]]

''' So next lets create our hidden layer this is called hidden layer
    only because as the programmer don't really specify or in charge of that layer
    Nueral networks is in charge of tweaking them, we might scale that to -1 to 1
 '''

'''
 wieghts should be as small as possible
 biases are usally intialized to 0, but their are times whetre you might not want yo
 to do that because if nuerons are not firing initially then neuron going to output 0
 so for a case like this called a dead network then you would want to start with a non-zero bias.
'''

# inputs = [0,2,-1,3.3,-2.7,1.1,2.2,-100]
# output = []

# # mini-relu
# for i in inputs:

#     output.append(max(i,0))
#     # or
#     # if i > 0:
#     #     output.append(i)
#     # elif i <= 0:
#     #     output.append(0)
# print(output)

# X- feature sets 
# y - would be the target data set
#100 features and 3 classifications
# X, y = spiral_data(100, 3)



class Layer_Dense:
    def __init__(self, n_inputs, n_nuerons):
                                            # our (4-inputs per nueron, 3-nuerons)
        self.weights = 0.10 * np.random.randn(n_inputs, n_nuerons) #shape it makes for us and won't need transpose  since we fliiped our shape.
        self.biases = np.zeros((1, n_nuerons)) #np.zero(shape, "somthing_else") 1 by how nuerons we have.
        
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
        

X, y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])





# 2 uniwue features
# layer1 = Layer_Dense(2, 5) # 4 is # of feature, 5- could have been anything.
# activation1 = Activation_ReLU()
# # layer2 = Layer_Dense(5, 2)
# layer1.forward(X)
# # print(layer1.output)
# activation1.forward(layer1.output)
# print(activation1.output)


# print(layer1.output)
# layer2.forward(layer1.output)
# print(layer2.output)
# print(.10*np.random.randn(4,3))