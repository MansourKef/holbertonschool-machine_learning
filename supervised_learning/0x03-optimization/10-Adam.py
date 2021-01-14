#!/usr/bin/env python3


import tensorflow as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """
    funcntion
    """
    opt = tf.train.AdamOptimizer(alpha, beta1, beta2, epsilon)
    train = opt.minimize(loss)
    return train
