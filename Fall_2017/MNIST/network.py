"""
    network.py -- a module to implement the stochastic gradient descent algorithm for a feedforward
                  neural network. Gradients are calculated using backpropagation.

    DISCLAIMER -- This program was primarily written by Michael Nielsen for his book 'Neural Networks
                  and Deep Learning' (found at https://github.com/mnielsen/neural-networks-and-deep-learning).

                  That said, I still made some small changes to make it easier for students in DPU DS to
                  understand, such as more descriptive variable names, comments that better explain
                  what the code is actually doing, and made it work as a standalone program rather than having
                  to execute it in a Python shell. The original program was also written in Python 2, so
                  I made the necessary changes to make the code work with Python 3.

    This is the first version of this project, and I will add code later to better optimize the neural network.


"""

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
    def stochastic_gradient_descent(self, training_data, epochs, mini_batch_size, learning_rate) :
        """ Train the neural network using mini-batch stochastic gradient descent.
            training_data is the list of pixel images
            epochs is (basically) the number of times all 60,000 images will be trained.
                More epochs = higher accuracy, longer run-time
            learning_rate is a small, positive parameter that determines how quickly the neural network will learn
                it needs to be small enough so that the slope of the gradient is a good approximation, yet large
                enough so that the algorithm works in a realistic amount of time
        """

        print('Calculating gradient descent...')

        n = len(training_data)
        for i in range(epochs) :
            # randomize the order of the images so the network won't learn the same way every time
            random.shuffle(training_data)

            # make a list containing the mini-batches --
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]

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

        # cycle through the mini-batches, apply backpropagation to each one
        for image, image_value in mini_batch :

            # backpropagate finds the appropriate change in weights/biases
            delta_biases, delta_weights = self.backpropagate(image, image_value)

            # update the numpy arrays to have the correct values for the change in biases and weights
            new_biases = [new_bias+delta_bias for new_bias, delta_bias in zip(new_biases, delta_biases)]
            new_weights = [new_weight+delta_weight for new_weight, delta_weight in zip(new_weights, delta_weights)]

        # update the weights and biases -- the formula for this is derived in the README
        self.weights = [weight-(learning_rate/len(mini_batch))*new_weight
                        for weight, new_weight in zip(self.weights, new_weights)]
        self.biases = [bias-(learning_rate/len(mini_batch))*new_bias
                       for bias, new_bias in zip(self.biases, new_biases)]

    """
        backpropagate() -- return a tuple (delta_biases, delta_weights) representing the gradient for the
                           cost function C_x (more about this in README as usual).
                           delta_biases and delta_weights are list of numpy arrays similar to
                           self.biases and self.weights
        NOTE: This algorithm is very complicated and mathematically heavy, and is very difficult to intuitively
              understand. I try my best to explain it, but the reality is I don't yet know how every part of
              it works. However, I think about it this way: the backpropagation algorithm basically provides
              a way of keeping track of small perturbations to the weights and biases as they propagate through
              the network, reach the output, and then affect the cost.
    """
    def backpropagate(self, image, image_value) :

        # declare two new numpy arrays for the updated weights & biases
        new_biases = [np.zeros(bias.shape) for bias in self.biases]
        new_weights = [np.zeros(weight_matrix.shape) for weight_matrix in self.weights]

        # -------- feed forward --------
        # store all the activations in a list
        activations = [image]

        # declare empty list that will contain all the z vectors
        zs = []

        for bias, weight in zip(self.biases, self.weights) :
            z = np.dot(weight, image) + bias
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        # -------- backward pass --------
        # transpose() returns the numpy array with the rows as columns and columns as rows
        delta = self.cost_derivative(activations[-1], image_value) * sigmoid_prime(zs[-1])
        new_biases[-1] = delta
        new_weights[-1] = np.dot(delta, activations[-2].transpose())

        # l = 1 means the last layer of neurons, l = 2 is the second-last, etc.
        # this takes advantage of Python's ability to use negative indices in lists
        for l in range(2, self.num_layers) :
            z = zs[-1]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            new_biases[-l] = delta
            new_weights[-l] = np.dot(delta, activations[-l-1].transpose())
        return (new_biases, new_weights)

    """
        cost_derivative() -- returns the vector of partial derivatives for the output activations
    """
    def cost_derivative(self, output_activations, image_value) :
        return (output_activations - image_value)

    """
        evaluate() -- return the number of test inputs for which the neural network outputs the 
                      correct result. 
    """
    def evaluate(self, test_data) :

        # np.argmax() returns the indices of the maximum value in the given array
        test_results = [(np.argmax(self.feedforward(image)), label) for image, label in test_data]

        return sum(int(x == y) for (x, y) in test_results)

# sigmoid() -- computes the output of one sigmoid neuron (read the README.md to see how this works)
def sigmoid(activations_vector) :
    # numpy automatically computes the function elementwise since activations_vector is a numpy array
    neuron_output = 1.0 / (1.0 + np.exp(-(activations_vector)))
    return neuron_output

# sigmoid_prime() -- returns the derivative of the sigmoid function
def sigmoid_prime(z) :
    return sigmoid(z) * (1 - sigmoid(z))

# import the MNIST dataset
training_data, validation_data, test_data = import_mnist.load_data_wrapper()

""" 
    Initialize the neural network -- the first layer contains however many input neurons there are
                                  -- the second layer contains the hidden layer
                                  -- the third layer contains 10 neurons, one for each number 0-9
"""
net = Network([len(training_data), 30, 10])

"""
    Use stochastic gradient descent to learn from the training data over 30 epochs (i.e. we'll go through
    the training data 30 times), with a mini-batch size of 10, and a learning rate of 3.0
    
    This will take a pretty long time to execute, likely 3-10 minutes
"""

net.stochastic_gradient_descent(training_data, 30, 10, 3.0)

# evaluate the test data
results = net.evaluate(test_data)
print(results)