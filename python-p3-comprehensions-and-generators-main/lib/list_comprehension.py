#!/usr/bin/env python3

def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0] if sequence else None

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences] if sentences else None
