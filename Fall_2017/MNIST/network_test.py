
"""
    Testing code for different neural network configurations
"""

# ----------------------
# - read the input data:

import import_mnist
training_data, validation_data, test_data = import_mnist.load_data_wrapper()
training_data = list(training_data)

# ----------------------
# network.py example:
import network

""" 
    Initialize the neural network -- the first layer contains however many input neurons there are
                                  -- the second layer contains the hidden layer
                                  -- the third layer contains 10 neurons, one for each number 0-9
"""
net = network.Network([784, 30, 10])

"""
    Use stochastic gradient descent to learn from the training data over 30 epochs (i.e. we'll go through
    the training data 30 times), with a mini-batch size of 10, and a learning rate of 3.0

    This will take a pretty long time to execute, likely 3-10 minutes
"""
net.stochastic_gradient_descent(training_data, 30, 10, 1.0, test_data=test_data)
