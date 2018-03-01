"""
    import_mnist.py converts the dataset of handwritten characters into a numpy array of pixel data
    that we can actually work with in Python
"""

import pickle
import gzip
import numpy as np


"""
    Python module for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
"""

def read() :

    """
        For those following along -- you will need to change the path to wherever you downloaded your MNIST data
        to.
    """

    path = 'D:\Programming\Python\DPUDS\DPUDS_Projects\Fall_2017\MNIST\mnist.pkl.gz'

    # There are two different datasets: one for training, and one for testing
    # The validation set isn't important for the first version of the network -- we'll use it later
    f = gzip.open(path, 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding='latin1')
    f.close()
    return (training_data, validation_data, test_data)

"""
    Return a tuple containing (training_data, validation_data,
    test_data)

    training_data is a list containing 50,000
    2-tuples (x, y). x is a 784-dimensional numpy.ndarray
    containing the input image.  y is a 10-dimensional
    numpy.ndarray representing the unit vector corresponding to the
    correct digit for x.

    validation_data and test_data are lists containing 10,000
    2-tuples (x, y).  In each case, x is a 784-dimensional
    numpy.ndarry containing the input image, and y is the
    corresponding classification, i.e., the digit values (integers)
    corresponding to x.

    Obviously, this means we're using slightly different formats for
    the training data and the validation / test data.  These formats
    turn out to be the most convenient for use in our neural network
    code.
"""
def load_data_wrapper() :

    tr_d, va_d, te_d = read()
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

"""
    Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network.
"""
def vectorized_result(j):

    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

