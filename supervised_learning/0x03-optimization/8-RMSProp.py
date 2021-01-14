#!/usr/bin/env python3


import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    `function
    """
    opt = tf.train.RMSPropOptimizer(learning_rate=alpha,
                                    decay=beta2, epsilon=epsilon)
    train = opt.minimize(loss)
    return train
