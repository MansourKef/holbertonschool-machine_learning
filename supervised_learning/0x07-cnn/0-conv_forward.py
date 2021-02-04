#!/usr/bin/env python3
"""module"""


import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same",
                stride=(1, 1)):
    """function"""
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, c_prev, c_new = W.shape
    sh, sw = stride
    pad_h, pad_w = (0, 0)
    if padding == "same":
        pad_h = int(np.ceil((((h_prev - 1) * sh + kh - h_prev) / 2)))
        pad_w = int(np.ceil((((w_prev - 1) * sw + kw - w_prev) / 2)))
    padded = np.pad(A_prev, ((0, 0), (pad_h, pad_h), (pad_w, pad_w), (0, 0)),
                    stant_values=(0, 0))
    conv_h = (h_prev + 2 * pad_h - kh) // sh + 1
    conv_w = (w_prev + 2 * pad_w - kw) // sw + 1
    convolved = np.zeros((m, conv_h, conv_w, c_new))
    for row in range(conv_h):
        for col in range(conv_w):
            for ch in range(c_new):
                slice_A = padded[:, row * sh:row * sh + kh, col * sw:col * sw
                                 + kw]
                slice_A_sum = np.sum(slice_A * W[:, :, :, ch], axis=(1, 2, 3))
                convolved[:, row, col, ch] = slice_A_sum
    return activation(convolved + b)
