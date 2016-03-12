#!/usr/bin/env python

"""Some fun work with functions.

We can find even numbers.
"""

import sys

def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False


def main():
	str_number = raw_input('Enter a number: ')
	their_number = int(str_number)
	if is_even(their_number):
		print 'Yes!'
	else:
		print 'Nope!'

if __name__ == "__main__":
	sys.exit(main())