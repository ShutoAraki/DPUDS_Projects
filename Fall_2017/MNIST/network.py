import numpy as np

import import_mnist

# import the MNIST dataset
training_data = list(import_mnist.read(dataset="training"))

""" 
So, at this point, we have an enormous list of 2-tuples (training_data) where the first element is a label and the
second is a 28x28 2D array of numbers representing pixels and their intensity, where 0 is the lowest
intensity (black) and 255 is the highest intensity (white). 
"""

# create a 3D list of pixel_images with values converted from 0-255 to 0.0-1.0; this is required
# for the weights and balances to work properly
training_data_converted_images = import_mnist.convert(training_data)

some_image = training_data_converted_images[2234]

label2, pixel_image2 = training_data[2234]

class Network(object) :

    # sizes is a list containing the number of neurons in the respective layers
    def __init__(self, sizes) :
        self.num_layers = len(sizes)
        self.sizes = sizes
        """
        numpy's randn function returns y samples from the standard normal distribution.
        Here, the biases and weights of the network are all initialized randomly using this function,
        and gives our stochastic gradient descent algorithm somewhere to start from.
        (NOTE: this is not the best way to initialize the weights and biases, but it'll do for now.)
        """
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]

        # zip() returns a list of tuples, where each tuple contains the i-th element from each argument.
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        """
        Both the biases and the weights are stored as lists of numpy matrices. For example,
        net.weights[1] is a numpy matrix storing the weights connecting the 2nd and 3rd layer of neurons.
        """
