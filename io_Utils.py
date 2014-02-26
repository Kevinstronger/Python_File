mport os

class utils():
	@staticmethod
	def getOutput(cmd):
		handle = os.popen(cmd)
		output = handle.read()
		handle.close()
		return output

	@staticmethod
	def writeToFile(file, content, append=False):
		try:
			f = open(file, append and 'a' or 'w')
			f.write(content)
			f.close()
		except:
			return False, "you stink - duok faila"
		return True

	@staticmethod
	def readFromFile(file):
		try:
			f = open(file, 'r')
			output = f.read()
			f.close()
		except:
			output = None

		return output
