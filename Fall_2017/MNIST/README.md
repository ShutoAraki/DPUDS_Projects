# Classifying handwritten digits using the MNIST data set

By Elijah Anderson

This exploration will use a made-from-scratch neural network to examine how handwritten digits can be
classified by computers.

Some resources to check out if you're interested in learning more about machine learning:

1) http://neuralnetworksanddeeplearning.com/chap1.html

This project is heavily based on chapter 1, and will base much of its code on what the author provides for us. This
is a great read for anyone who wants to learn more about machine learning/neural networks. I changed it to make it compatible
with Python 3 as well as make more helpful comments explaining exactly what's going on.

2) https://docs.google.com/a/depauw.edu/presentation/d/1OePEVvaUG33XgSXMQJM7FdtVNCKoVhNPT2v_jRpl1us/edit?usp=sharing

If you're not a fan of reading a dense book about neural networks, I made a slide presentation that may make it easier
to understand.

3) https://www.tensorflow.org/get_started/mnist/beginners

Although we will be building our neural network from scratch, TensorFlow provides a great neural network library
and is great for people who don't want to get into the nitty gritty (i.e. mathematics) of machine learning.

# ------- Update 10-22-17 --------

The first version of the project is now uploaded! This is the simplest form that the network will take -- for the
remainder of the semester, I will keep keep updating the network to incorporate improvements in how it learns. For
example, there's a better cost function, a better method for initializing weights & biases, a better way to choose
the learning rate, and the list goes on and on.

So, the code I included has a file called 'network_test.py' -- this is the file you should run if you decide to fork
the project and play around with the network a little. Doing this will give you a good idea of how the different
factors (learning rate, number of hidden layers, number of epochs, etc.) effect how the network learns.

A sample output of the program:

Number correct before network is implemented: 447 / 10000

Epoch 0 : 9030 / 10000

Epoch 1 : 9201 / 10000

Epoch 2 : 9320 / 10000

Epoch 3 : 9355 / 10000

Epoch 4 : 9382 / 10000

Epoch 5 : 9421 / 10000

Epoch 6 : 9461 / 10000

Epoch 7 : 9447 / 10000

Epoch 8 : 9450 / 10000

Epoch 9 : 9459 / 10000

Epoch 10 : 9477 / 10000

Epoch 11 : 9472 / 10000

Epoch 12 : 9496 / 10000

Epoch 13 : 9493 / 10000

Epoch 14 : 9501 / 10000

Epoch 15 : 9483 / 10000

Epoch 16 : 9502 / 10000

Epoch 17 : 9524 / 10000

Epoch 18 : 9533 / 10000

Epoch 19 : 9539 / 10000

Epoch 20 : 9503 / 10000

Epoch 21 : 9525 / 10000

Epoch 22 : 9556 / 10000

Epoch 23 : 9535 / 10000

Epoch 24 : 9517 / 10000

Epoch 25 : 9529 / 10000

Epoch 26 : 9516 / 10000

Epoch 27 : 9517 / 10000

Epoch 28 : 9534 / 10000

Epoch 29 : 9546 / 10000

Finished!

This is with 30 hidden layers, a learning rate of 3.0, and 30 epochs. The highest accuracy reached was 95.56% (the
number before the network is implemented is usually around 1000, not 447). This runthrough of the algorithm was
pretty good!

If you have any questions about implementing the network for yourself, feel free to ask me.
