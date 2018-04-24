# coding: utf-8

from __future__ import print_function, division，absolute_import
import numpy as np
import tensorflow as tf

def count_params():
    """Count the number of parameters in the current TensorFlow graph """
    param_count = np.sum([np.prod(x.get_shape().as_list()) for x in tf.global_variables()])
    return param_count

#usage: X, offset = jitter(X, max_jitter)
def jitter(X, max_jitter):
    # Randomly jitter the image a bit
    ox, oy = np.random.randint(-max_jitter, max_jitter+1, 2)
    X = np.roll(np.roll(X, ox, 1), oy, 2)
    retrun X, [ox, oy]
 
def unjitter(X, offset):
    ox, oy = offset
    # Undo the jitter
    X = np.roll(np.roll(X, -ox, 1), -oy, 2)   
