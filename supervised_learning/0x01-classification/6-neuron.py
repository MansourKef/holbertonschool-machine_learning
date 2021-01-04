#!/usr/bin/env python3
"""
6-neuron.py
"""
import numpy as np


def sigmoid(z):
    """sigmoid function"""
    return 1/(1 + np.exp(-z))


class Neuron:
    """Neuron"""
    def __init__(self, nx):
        """Initializes the data."""
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.normal(loc=0.0, scale=1.0, size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Get Function"""
        return self.__W

    @property
    def b(self):
        """Get Function"""
        return self.__b

    @property
    def A(self):
        """Get Function"""
        return self.__A

    def forward_prop(self, X):
        """forward_prop Function"""
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1.0 / (1.0 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """cost Function"""
        cost = -np.sum((Y * np.log(A)) +
                       ((1 - Y) * np.log(1.0000001 - A))) / Y.shape[1]
        return cost

    def evaluate(self, X, Y):
        """evaluate Function"""
        Z = np.matmul(self.__W, X) + self.__b
        A = sigmoid(Z)
        cost = np.sum(-(Y * np.log(A) +
                        (1 - Y) * np.log(1.0000001 - A))) / (Y.shape[1])
        A = np.where(A >= 0.5, 1, 0)
        return A, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """gradient_descent Function"""
        M = Y.shape[1]
        dz = A - Y
        dw = (np.matmul(dz, X.T)) / M
        db = (np.sum(dz)) / M
        self.__W -= alpha * dw
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """train"""
        if not type(iterations) is int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not type(alpha) is float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        m = Y.shape[1]
        for i in range(iterations):
            z = np.matmul(self.__W, X) + self.__b
            self.__A = sigmoid(z)
            cost = np.sum(-(Y * np.log(self.__A) +
                            (1 - Y) * np.log(1.0000001 - self.__A))) / m
            dz = self.__A - Y
            dw = (np.matmul(dz, X.T)) / m
            db = (np.sum(dz)) / m
            self.__A = np.where(self.__A >= 0.5, 1, 0)
            self.__W -= alpha * dw
            self.__b -= alpha * db
        return self.__A, cost
