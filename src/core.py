# -*-
# coding: utf-8 -*-

from . import helpers

import numpy as np
import matplotlib.pyplot as plt

def add_one(number):
    """Adds one to number"""
    return number + 1

def basicPlot():
    """Shows a parabola"""
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

