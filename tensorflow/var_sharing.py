# coding: utf-8
# variable sharing
import numpy as np
import tensorflow as tf

def conv_relu(input, kernel_shape, bias_shape):
    # Create variable named "weights".
    weights = tf.get_variable("weights", kernel_shape,
        initializer=tf.random_normal_initializer())
    # Create variable named "biases".
    biases = tf.get_variable("biases", bias_shape,
        initializer=tf.constant_initializer(0.0))
    conv = tf.nn.conv2d(input, weights,
        strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv + biases)
    
    
def my_image_filter(input_images):
    with tf.variable_scope("conv1"):
        # Variables created here will be named "conv1/weights", "conv1/biases".
        relu1 = conv_relu(input_images, [5, 5, 32, 32], [32])
    with tf.variable_scope("conv2"):
        # Variables created here will be named "conv2/weights", "conv2/biases".
        return conv_relu(relu1, [5, 5, 32, 32], [32])
        
        
 def my_variable_sharing(): 
    # variable sharing
    # opt1
    with tf.variable_scope("model") as scope:
        output1 = my_image_filter(input1)
        scope.reuse_variables()
        output2 = my_image_filter(input2)
        
    # opt2
    with tf.variable_scope("model") as scope:
        output1 = my_image_filter(input1)
    with tf.variable_scope(scope, reuse=True):
        output2 = my_image_filter(input2)
   
