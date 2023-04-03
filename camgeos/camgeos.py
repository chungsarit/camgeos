"""Main module."""

import random
import string

def generate_random_string(length=10, upper=False, digits=False, punctuation=False):
    """Generates a random string of the specified length."""
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    if digits:
        letters += string.digits
    if punctuation:
        letters += string.punctuation
    result_string = ''.join(random.choice(letters) for i in range(length))
    return result_string

def generate_lucky_number(length=10):
    """Generates a lucky number."""
    lucky_number = random.randint(10**(length-1), 10**length-1)
    return lucky_number
    
