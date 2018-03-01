
"""
    TENSORFLOW MNIST -- by Eli Anderson
"""

# import the MNIST dataset (tensorflow has it conveniently built-in)
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# one_hot encoding: 5 = 0000010000, 2 = 0010000000, etc. This is how the from-scratch model worked as well

# import other necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import tensorflow as tf

# define a couple functions that will assign the amount of training and test data loaded from the dataset

def train_size(num) :
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Total training images in dataset = ' + str(mnist.train.images.shape))

    # `x_train` = the pixel data itself
    x_train = mnist.train.images[:num,:]
    print('x_train examples loaded = ' + str(x_train.shape))

    # `y_train` = the image labels
    y_train = mnist.train.labels[:num,:]
    print('y_train examples loaded = ' + str(y_train.shape))
    print('\n')
    return x_train, y_train

def test_size(num) :
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Total testing images in dataset = ' + str(mnist.test.images.shape))
    x_test = mnist.test.images[:num, :]
    print('x_test examples loaded = ' + str(x_test.shape))
    y_test = mnist.test.labels[:num, :]
    print('y_train examples loaded = ' + str(y_test.shape))
    print('\n')
    return x_test, y_test

# some simple functions for resizing & displaying the data

def display_digit(num) :
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Digit\'s one_hot encoding: ' + str(y_train[num]))

    # since labels are stored in one_hot lists, use argmax() to return the index, which is the actual label
    label = y_train[num].argmax(axis=0)
    # images are 28x28 pixels
    image = x_train[num].reshape([28,28])
    plt.title('Example: #' + str(num) + ', Label: ' + str(label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

# time to build the model
x_train, y_train = train_size(50000)
# some arbitrary digit
display_digit(2753)

# the next step is to actually use tensorflow to create a flow chart (https://www.tensorflow.org/programmers_guide/graph_viz),
# which will later be fed the data

# define the session
sess = tf.Session()

# define a placeholder -- a variable used to feed data into (i.e., the input layer). Its shape and type need to be
# matched exactly. Let's define x as the placeholder to feed the `x_train` data into:
x = tf.placeholder(tf.float32, shape=[None, 784])
#  the input layer can be fed as many examples as you want(None) of 784-sized values

# define `y_` as the placeholder to feed the y_train data into. This will just be used later to compare our predictions to
# ground truths
y_ = tf.placeholder(tf.float32, shape=[None, 10])

""" 
 next is to define the weights and biases. Remember, the whole point of machine learning is to change these values to
 make them as low as possible, which classifies different things. E.g. the hill analogy for stochastic gradient descent
 The values will be initialized to zero, since tensorflow optimizes these values for us. Much less work than from-scratch.
"""

# `W` is a collection of 784 values for each of the 10 classes
W = tf.Variable(tf.zeros([784, 10]))
# and each of the 10 classes gets a bias
b = tf.Variable(tf.zeros([10]))

# now, define our classifier function. The tutorial uses multinomial logistic regression, but there are plenty more
# methods, such as the sigmoid function I used in the from-scratch NN
y = tf.nn.softmax(tf.matmul(x, W) + b)
# `tf.matmul(x, W) + b` returns the number of training examples fed * the number of classes. In this case, 784x10
print(y)

"""
 to actually get the values of y, we need to run an appropriate session and feed it some actual data
 in order to run a function in the session, the variables must be initialized within it:
 # sess.run(tf.global_variables_initializer())
 # print(sess.run(y, feed_dict={x: x_train}))
 our classifier knows nothing at this point, so the probability for each example is 10%
"""

# next, define the cost function, which measures the accuracy of the classifier by comparing the true values from
# `y_train` to the results of our predictions (y)
cost_func = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# `tf.reduce_mean` & `tf.reduce_sum` just compute the mean/sum across the dimensions of the given tensor

""" 
the function is taking the log of all our predictions (y) and multiplying by the example's true value (y_)
if that result for each value is close to 0, it will make the value a large negative number, and vice versa:
   e.g.: -log(.01) = 4.6 ; -log(.99) = .1
therefore, we are penalizing the classifier with a large number if the prediction is confidently incorrect and a very
small number if the prediction is confidently correct

An example of a softmax prediction that is very confident that the digit is a 3:
    [0.03, 0.03, 0.01, 0.9, 0.01, 0.01, 0.0025,0.0025, 0.0025, 0.0025]
Digits: 0    1     2    3     4     5      6      7       8       9
-log(.9) = .046
-log(.0025) = 2.6
See how that works? 

---------------------------------------------------------------------------------------------------------------------

Now we begin to actually train our classifier. This is done by continuously assigning appropriate values to W and b
such that the lowest possible loss is achieved. 
"""

# We already have `x_train`/`y_train` set up, so we just need to assign x_test/y_test, our learning rate, and our batch size
x_test, y_test = test_size(10000)
learning_rate = 1.0
train_steps = 3000

# initialize all variable to be used by our tensorflow graph
sess.run(tf.global_variables_initializer())

# Now, we need to train our classifier using stochastic gradient descent, like I did in the from-scratch NN.
# `training` will perform the SGD optimizer with a chosen learning rate, and try to minimize with our cost function
training = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_func)

# `correction_prediction` will return a tensor of type bool, depending on our classifier function's (y) greatest value
# (what it thinks is the correct one is equal to the actual value)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# `accuracy` is rather self-explanatory
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

"""
    Time to train. We'll define a loop that repeats batch_size times.
    For each loop, it runs `training`, feeding in values from `x_train` and `_train` using feed_dict, similar to the
    example shown earlier. It will also calculate accuracy for each unseen example in `x_test` as it trains the examples
    in `x_train`
"""

for i in range(train_steps+1) :
    sess.run(training, feed_dict={x: x_train, y_: y_train})
    # for every 100 examples trained, recalculate the accuracy
    if i%100 == 0 :
        print('\nBatch no.: ' + str(i//100) + '\nAccuracy = ' + str(sess.run(accuracy, feed_dict={x: x_test, y_: y_test})) +
              '\nLoss = ' + str(sess.run(cost_func, {x: x_train, y_: y_train})))
