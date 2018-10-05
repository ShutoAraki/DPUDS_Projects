@author: Shuto Araki (Junior Computer Science major at DePauw University)

# Motivation
Just watch [this video](https://youtu.be/PCBTZh41Ris)! When my friend Eli Anderson showed me this video, it BLEW MY MIND!! This paper just came out on August 22, 2018 so we're talking about literally cutting edge technology right here. That's a good enough motivation. We just wanna do cool things, right?

# Objective
- Complete Drake's "In My Feelings" challenge without actually dancing
- Create a web application that anyone can use to generate their own dance videos by uploading source and target videos

# Background (including a lot of technical stuff that I don't fully understand)
## Original Paper
Read [this paper](https://arxiv.org/pdf/1808.07371.pdf) very carefully and familarize yourself with GANs and basics of pose estimation. We can go over these step by step in meetings because I don't understand all of it either:+1: 
Basically, we will try to replicate what this paper did. It seems like that's very uncreative, but at least we have a clear goal. Also, the technical parts are fairly complicated so this project will be very challenging.

## More about GANs (Generative Adversarial Networks)
Generative Adversarial Networks: An Overview [\[arXiv\]](https://arxiv.org/abs/1710.07035)

## Other resources in basic Machine Learning related stuff
### Linear Algebra
You kinda need linear algebra to understand machine learning in general. [This video series](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) give you a great intuition.

### Videos
YouTube videos are great! [Siraj Raval](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A) has a lot of interesting contents including GANs and human pose estimation!


UPDATE:

<b> Siraj just made an amazing comprehensive [video](https://www.youtube.com/watch?v=WzRonX_bs34) about this project! </b>

# Methods
Let's try to strike a good balance between theory and practice. So, we will try top-down and bottom-up approaches at the same time!
## Top-down
We start from implementing the pose estimation part. A lot of people did research (as seen in the original paper citations) and we have this open source software [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) by CMU Perceptual Computing Lab. Or, if you have any good ideas as to how we can start implementing this project, you can just do that.
## Bottom-up
At the same time, we can build the foundational knowledge (Linear Algebra, basic programming, and Convolutional Neural Network, etc. whatever you might need) to understand what is going on behind the scene including how the algorithm detects different parts of the body.

# Necessary Equipment
- A lot of passion, energy, and some time (about 3-5 hours a week or more?)
- Laptop (recommended)

We have an access to really good brand new GPUs (NVIDIA GTX 1080 Ti) on the basement of Roy O. West Library, so we don't have to worry about computation powers that much. Yay!

I hope everyone is excited! We can start from wherever you like (top-down or bottom-up) and if you're interested, contact me via DPUDS Slack.
