""" This script creates a text file of billion integers. """
import random

MAX_RANDOM = 6_600_000  # max bound for random number generation

with open('huuuge.txt', 'w') as f:
    i = 1
    while i <= 50_000_000:  # amount of numbers
        f.write(f'{random.randint(0, MAX_RANDOM)}\n')
        i += 1
