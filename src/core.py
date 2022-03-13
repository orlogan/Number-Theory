# -*-
# coding: utf-8 -*-

from . import helpers


def add_one(number):
    """Adds one to number"""
    return number + 1


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
