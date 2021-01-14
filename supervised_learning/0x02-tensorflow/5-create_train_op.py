#!/usr/bin/env python3

"""module"""

import tensorflow as tf


def create_train_op(loss, alpha):
    """
    function
    """
    optimizer = tf.train.GradientDescentOptimizer(alpha)
    train = optimizer.minimize(loss)
    return train
