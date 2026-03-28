'''A module for demonstrating exceptions'''
import sys
from math import log

def convert(s):
	'''convert to an integer'''
	try:
		return int(s)
	except (ValueError, TypeError) as e:
		print("Conversion error: {}"\
		       .format(str(e)),
			   file=sys.stderr)
		return(-1)

def string_log(s):
	'''convert to log'''
	try:
		v = convert(s)
		return log(v)
	except (ValueError, TypeError) as e:
		print("Conversion error: {}"\
		       .format(str(e)),
			   file=sys.stderr)
		return(-1)