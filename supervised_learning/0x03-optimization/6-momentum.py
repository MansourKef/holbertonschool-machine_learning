#!/usr/bin/env python3


import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """
    function
    """
    opt = tf.train.MomentumOptimizer(alpha, beta1)
    train = opt.minimize(loss)
    return train
