class Program(object):
	"""
	This is a class that holds various information about the program.
	"""
	def __init__(self, name, version, usage):
		super(Program, self).__init__()
		self._name = name
		self._version = version
		self._usage = usage
		self._values = {};
	def bind(self, name, value):
		self._values[name] = value
	def value(self, name):
		return self._values[name]
	def usage(self):
		print(self._usage)
	def version(self):
		print("version: %s" % (self._version))
	def info(self):
		print("""
Name: %s
Version: %s,
Usage: 
%s"""
			 % (self._name, self._version, self._usage))