#!/usr/bin/env python3
"""module"""


import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """function"""
    weights = K.initializers.he_normal()
    F11, F3, F12 = filters
    conv1 = K.layers.Conv2D(F11, kernel_size=1,
                            kernel_initializer=weights,
                            padding='same', strides=(s, s))(A_prev)
    BN1 = K.layers.BatchNormalization()(conv1)
    relu1 = K.layers.Activation('relu')(BN1)
    conv2 = K.layers.Conv2D(F3, kernel_size=3,
                            kernel_initializer=weights,
                            padding='same')(relu1)
    BN2 = K.layers.BatchNormalization()(conv2)
    relu2 = K.layers.Activation('relu')(BN2)
    conv3 = K.layers.Conv2D(F12, kernel_size=1,
                            kernel_initializer=weights,
                            padding='same')(relu2)
    BN3 = K.layers.BatchNormalization()(conv3)
    conv4 = K.layers.Conv2D(F12, kernel_size=1,
                            kernel_initializer=weights,
                            padding='same', strides=(s, s))(A_prev)
    BN4 = K.layers.BatchNormalization()(conv4)
    add = K.layers.add([BN3, BN4])
    output = K.layers.Activation('relu')(add)
    return output
