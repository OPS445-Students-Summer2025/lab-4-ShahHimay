#!/usr/bin/env python3
# Author ID: 118541234

def is_digits(sobj):
    # Check if each character in the string is a digit
    for ch in sobj:
        if not ch.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
