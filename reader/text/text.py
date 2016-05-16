import sys
import reader

print(reader)
class TextReader(reader.Reader):
	def __init__(self):
		pass 

	def readToString(self, path):
		return 'Text string'	
