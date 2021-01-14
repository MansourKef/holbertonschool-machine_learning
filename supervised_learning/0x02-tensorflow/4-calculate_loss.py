#!/usr/bin/env python3

"""
module
"""

import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    function
    """
    loss = tf.losses.softmax_cross_entropy(y, y_pred)
    return loss
