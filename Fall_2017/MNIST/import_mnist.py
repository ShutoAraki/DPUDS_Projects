# import_mnist.py converts the dataset of handwritten characters into a numpy array of pixel data
# that we can actually work with in Python

import os

# struct performs conversions between Python values and C structs represented as Python bytes objects
import matplotlib as plt
from matplotlib import pyplot
import numpy as np
import struct


"""
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
"""
def read(dataset):

    path = 'D:\Programming\Python\MNIST'

    #
    if dataset is 'training':
        image_file = os.path.join(path, 'train-images.idx3-ubyte')
        label_file = os.path.join(path, 'train-labels.idx1-ubyte')
    elif dataset is 'testing':
        image_file = os.path.join(path, 't10k-images.idx3-ubyte')
        label_file = os.path.join(path, 't10k-labels.idx1-ubyte')
    else:
        print("dataset must be 'testing' or 'training'")
        raise ValueError

    # Load everything in some numpy arrays
    with open(label_file, 'rb') as label_file:
        # the '8' in read(8) means it reads 8 bytes of the file, or 64 bits
        #
        # since the files we're working with contain only binary data, we have to unpack it
        # unpack() converts the binary data into Python 'bytes' objects - in this case, ints
        #
        # "The magic number is an integer (MSB first)." - MNIST website; so basically it doesn't matter
        #
        # 'I' (unsigned int) is the format we convert the file to
        magic, num = struct.unpack(">II", label_file.read(8))

        # fromfile() is an efficient way to read binary data and store it to a numpy array
        #
        # dtype indicates what the binary data will be converted into; in this case, 8-bit ints
        # So, label is just an array of ints representing the labels
        label = np.fromfile(label_file, dtype=np.int8)

    with open(image_file, 'rb') as image_file:
        magic, num, rows, cols = struct.unpack(">IIII", image_file.read(16))

        # image is a huge 2D array of pixel data reshaped into square sections resembling a 28x28 pixel image
        # In other words, we interpret each image is a big array of numbers
        image = np.fromfile(image_file, dtype=np.uint8).reshape(len(label), rows, cols)

    # lambda is basically just a fancy way of saying function. Here, it returns a list of 2-tuples with
    # the label/image in the corresponding index of each numpy array
    get_image = lambda idx: (label[idx], image[idx])

    # Create an iterator which returns each image in turn
    # yield is a keyword used like return, but returns a generator (an iterator that doesn't store
    # all the values in memory)
    for i in range(len(label)):
        yield get_image(i)


# Render a given numpy.uint8 2D array of pixel data.
def show(image):

    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    imgplot = ax.imshow(image, cmap=plt.cm.gray)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    pyplot.show()

# training_data is a list of tuples where the first element is the label and the second is the pixel data
training_data = list(read(dataset="training"))
print(len(training_data))
label, pixel_image = training_data[0]
# print(label)
print('One row of pixels: ')
print(pixel_image[8])
# convert the pixel data into a matplotlib figure, and show it
show(pixel_image)

""" 
So, at this point, we have an enormous list of 2-tuples (training_data) where the first element is a label and the
second is a 28x28 2D array of numbers representing pixels and their intensity, where 0 is the lowest
intensity (black) and 255 is the highest intensity (white).

The next steps to implement are:
    1) Each time a training input is analyzed, be sure to flatten it and set its pixel values to 0-1
    2) Create Network class, used to represent a neural network
        - refer to the online book for this part
    3) Create driver/main class to execute the network
"""