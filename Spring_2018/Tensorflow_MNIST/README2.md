# TensorFlow-MNIST
Last semester, I implemented a from-scratch neural network to classify handwritten digits from the MNIST dataset.
This semester, my goal is to become fluent with the machine learning framework TensorFlow. I hope to have at least 3
different machine learning projects up on my github using the framework by the time I start my internship at Cerner.

The first project will be a simple one to get a feel for the framework and start to really understand how to
manipulate and interact with the code rather than just stealing others' code. This project will be a tensorflow
implementation of the project I worked on last semester, classifying handwritten digits from the MNIST dataset. I
will be using a tutorial by Justin Francis from a little over a year ago:

https://www.oreilly.com/learning/not-another-mnist-tutorial-with-tensorflow

I chose this one because it is visually appealing and interactive, so I really learn rather than just copying code.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=

Sample result of training 50,000 images with the tensorflow NN with a learning rate of 1.0 and a batch size of 30:

Batch no.: 0
Accuracy = 0.6668

Batch no.: 1
Accuracy = 0.9118

Batch no.: 2
Accuracy = 0.9174

Batch no.: 3
Accuracy = 0.9186

Batch no.: 4
Accuracy = 0.9207

Batch no.: 5
Accuracy = 0.9212

Batch no.: 6
Accuracy = 0.9212

Batch no.: 7
Accuracy = 0.9217

Batch no.: 8
Accuracy = 0.9219

Batch no.: 9
Accuracy = 0.9222

Batch no.: 10
Accuracy = 0.9221

Batch no.: 11
Accuracy = 0.9223

Batch no.: 12
Accuracy = 0.923

Batch no.: 13
Accuracy = 0.9229

Batch no.: 14
Accuracy = 0.9232

Batch no.: 15
Accuracy = 0.9231

Batch no.: 16
Accuracy = 0.923

Batch no.: 17
Accuracy = 0.9231

Batch no.: 18
Accuracy = 0.9234

Batch no.: 19
Accuracy = 0.9234

Batch no.: 20
Accuracy = 0.9235

Batch no.: 21
Accuracy = 0.9235

Batch no.: 22
Accuracy = 0.9236

Batch no.: 23
Accuracy = 0.9237

Batch no.: 24
Accuracy = 0.9238

Batch no.: 25
Accuracy = 0.9238

Batch no.: 26
Accuracy = 0.9243

Batch no.: 27
Accuracy = 0.9243

Batch no.: 28
Accuracy = 0.9245

Batch no.: 29
Accuracy = 0.9249

Batch no.: 30
Accuracy = 0.9251

So, it classified 9251 / 10000 on its last batch.

For comparison, a sample result of training 50,000 with the from-scratch NN with the same parameters:

Number correct before network is implemented: 1056 / 10000
Epoch 0 : 7548 / 10000
Epoch 1 : 9034 / 10000
Epoch 2 : 9162 / 10000
Epoch 3 : 9218 / 10000
Epoch 4 : 9257 / 10000
Epoch 5 : 9308 / 10000
Epoch 6 : 9339 / 10000
Epoch 7 : 9361 / 10000
Epoch 8 : 9379 / 10000
Epoch 9 : 9389 / 10000
Epoch 10 : 9406 / 10000
Epoch 11 : 9398 / 10000
Epoch 12 : 9427 / 10000
Epoch 13 : 9447 / 10000
Epoch 14 : 9437 / 10000
Epoch 15 : 9423 / 10000
Epoch 16 : 9447 / 10000
Epoch 17 : 9444 / 10000
Epoch 18 : 9440 / 10000
Epoch 19 : 9450 / 10000
Epoch 20 : 9454 / 10000
Epoch 21 : 9463 / 10000
Epoch 22 : 9468 / 10000
Epoch 23 : 9478 / 10000
Epoch 24 : 9459 / 10000
Epoch 25 : 9479 / 10000
Epoch 26 : 9470 / 10000
Epoch 27 : 9471 / 10000
Epoch 28 : 9478 / 10000
Epoch 29 : 9474 / 10000

So, it classified 9474 / 10000 on its last batch (classifying 9478 at its peak).

From this, it's easy to conclude that perhaps the from-scratch NN is better at classification than tensorflow's
implementation of a NN. However, remember that that the from-scratch uses the sigmoid function as its cost function,
whereas the tensorflow implementation uses the softmax function. Here's a comparison between the two:

    Sigmoid: S(x) = 1 / (1 + e^(-x))
    Softmax: S(x) = e^x / (e^max(x) * sum(e^x / e^max(x)))

So softmax is clearly more complicated, but does that mean it's better? To get a better comparison, let's run the
tensorflow neural network again, except using the sigmoid function as the cost function:

[TO BE CONTINUED]

