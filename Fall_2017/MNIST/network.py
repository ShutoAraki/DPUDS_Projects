"""
    network.py -- the beef of the project
"""

# TODO -- add comments in update_mini_batch() explaining what the hell is going on
# TODO -- understand and implement backpropagation

import numpy as np
import random

import import_mnist

# The Network class -- represents a neural network
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
        
        net.weights[j][k] is the weights for the connections between the k^th neuron in the hidden layer and the
        j^th neuron in the output layer (remember that one neuron in the hidden layer connects to every neuron in
        the output layer).
        
        The ordering of the j and k indices seems a bit strange, but the advantage of using this ordering is
        that it means that the vector of activations of the third layer of neurons is:
            
            a' = sigmoid(weights*a + biases)
            
        a is the vector of activations (i.e. the output values of each neuron) of the hidden layer of neurons.
        weights is the matrix weights[j]
        biases is the vector of biases for the output layer -- one bias per neuron
        
        To obtain a', we multiply vector a by the matrix of weights and then add the biases, which returns
        a vector. Then, we apply the sigmoid function to every element in that vector, which computes the output
        of each neuron in the output layer.
        """

    # feedforward() -- applies the sigmoid function for each neuron in each layer (there are other methods of
    #                  doing this, but this one is the simplest -- README.md has more info on it)
    def feedforward(self, n):
        # return the output of the network n
        for bias, weights in zip(self.biases, self.weights) :
            n = sigmoid(np.dot(weights, n) + bias)
        return n

    """ stochastic_gradient_descent() -- calculates the weights and biases so that the cost of the network is as
                                         close to 0 as possible. Exactly how this actually helps the network learn is
                                         found on the README
    """
    def stochastic_gradient_descent(self, training_data_images, epochs, mini_batch_size, learning_rate) :
        """ Train the neural network using mini-batch stochastic gradient descent.
            training_data_images is the list of pixel images
            epochs is (basically) the number of times all 60,000 images will be trained.
                More epochs = higher accuracy, longer run-time
            learning_rate is a small, positive parameter that determines how quickly the neural network will learn
                it needs to be small enough so that the slope of the gradient is a good approximation, yet large
                enough so that the algorithm works in a realistic amount of time
        """
        print('Calculating gradient descent...')
        n = len(training_data_images)
        for i in range(epochs) :
            # randomize the order of the images so the network won't learn the same way every time
            random.shuffle(training_data_images)
            # make a list containing the mini-batches --
            mini_batches = [training_data_images[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            # update the weights and biases of each mini-batch
            for mini_batch in mini_batches :
                self.update_mini_batch(mini_batch, learning_rate)
            print('Epoch ' + str(i) + ' completed')
        print('Finished!')

    """ update_mini_batch() -- updates the network's weights and biases by applying gradient descent using 
                               backpropagation to a batch of training data
    """
    def update_mini_batch(self, mini_batch, learning_rate) :
        # declare two new numpy arrays for the updated weights & biases
        new_biases = [np.zeros(bias.shape) for bias in self.biases]
        new_weights = [np.zeros(weight_matrix.shape) for weight_matrix in self.weights]
        for image in mini_batch :
            delta_biases, delta_weights = self.backpropagate(image)
            new_biases = [new_bias+delta_bias for new_bias, delta_bias in zip(new_biases, delta_biases)]
            new_weights = [new_weight+delta_weight for new_weight, delta_weight in zip(new_weights, delta_weights)]

        # update the weights and biases
        self.weights = [weight-(learning_rate/len(mini_batch))*new_weight
                        for weight, new_weight in zip(self.weights, new_weights)]
        self.biases = [bias-(learning_rate/len(mini_batch))*new_bias
                       for bias, new_bias in zip(self.biases, new_biases)]


# sigmoid() -- computes the output of one sigmoid neuron (read the README.md to see how this works)
def sigmoid(activations_vector) :
    # numpy automatically computes the function elementwise since activations_vector is a numpy array
    neuron_output = 1.0 / (1.0 + np.exp(-(activations_vector)))
    return neuron_output

# import the MNIST dataset
training_data = list(import_mnist.read(dataset="training"))

""" 
So, at this point, we have an enormous list of 2-tuples (training_data) where the first element is a label and the
second is a 28x28 2D array of numbers representing pixels and their intensity, where 0 is the lowest
intensity (black) and 255 is the highest intensity (white). 
"""

# create a 3D list of pixel_images with values converted from 0-255 to 0.0-1.0; this is required
# for the weights and balances to work properly
training_data_images = import_mnist.convert(training_data)

some_image = training_data_images[2234]
print(len(training_data_images))
label2, pixel_image2 = training_data[2234]

""" Initialize the neural network -- the first layer contains however many input neurons there are
                                  -- the second layer contains the hidden layer
                                  -- the third layer contains 10 neurons, one for each number 0-9
"""
net = Network([len(training_data_images), 30, 10])
print(net.weights[1])
print(net.biases[1])