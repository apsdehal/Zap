import requests
from lxml import html
import optparse

class zap:
	"""
	Zap class for providing interface with the software
	"""

	def __init__(self):
		"""
		Initialize for the zap class, creates a parser object and uses it to parse options
		"""
		self.parser = optparse.OptionParser()
		self.parser.add_option('-t', '--term', help= 'Term to be searched', dest='term')
		(opts, args) = self.parser.parse_args()
		if opts.term is None:
			print 'Passing a term is necessary'
			parser.print_help()
			exit(-1)
