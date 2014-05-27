import requests
import optparse
from readability import Readability
from pptx import Presentation
from pptx.util import Inches, Pt

Wiki_URL = 'https://en.wikipedia.org/wiki/'
class zap:
	"""
	Zap class for providing interface with the software
	"""

	def __init__(self):
		"""
		Initialize for the zap class, creates a parser object and uses it to parse options
		"""
		self.parser = optparse.OptionParser()
		self.parser.add_option('-t', '--term', help = 'Term to be searched', dest ='term')
		(opts, args) = self.parser.parse_args()
		if opts.term is None:
			print 'Passing a term is necessary'
			self.parser.print_help()
			exit(-1)
		self.getContent(opts.term)	
	
	def getContent(self, term):
		url = Wiki_URL + term
		print '[+] Retrieving content from ' + url 
		html = requests.get(url).content
		parser = Readability(html.decode('utf8'))

		# parser.title
		# parser.article
		print parser.article.get_text()

	def generatePPT(self, content):		
		self.prs = Presentation()
		layout = self.prs.slide_layouts[6]

	def addSlide(self, layout, content):
		slide = self.prs.slides.add_slide(layout)

		left = top = width = height = Inches(1)
		txBox = slide.shapes.add_textbox(left, top, width, height)
		tf = txBox.textframe
		tf.text = content

def main():
	zap()

if __name__ == '__main__':
	main()				
