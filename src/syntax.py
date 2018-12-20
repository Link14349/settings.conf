import re
import os

class SyntaxNode(object):
	"""
	This is a node element class of syntax tree class
	"""
	def __init__(self, val, opt = ""):
		super(SyntaxNode, self).__init__()
		self._val = val
		self._opt = opt
	def opt(self):
		return self._opt
	def val(self):
		return self._val

class Syntax(object):
	"""
	This is a syntax tree class
	"""
	def __init__(self, val = None, opt = None):
		super(Syntax, self).__init__()
		self._root = SyntaxNode(val,opt)
		self._code = ""
	def parse(self, code):
		self._code = code
		includes = {}
		cache = {}
		# include files
		while True:
			index = re.search("include\\s", self._code)
			if index == None:
				break
			index = index.span()
			readFile = ""
			i = index[1]
			while i < len(self._code):
				if self._code[i] == "\n":
					break
				readFile += self._code[i]
				i += 1
			pattern = re.compile(r"include\s" + readFile)
			if includes.get(readFile) == True:
				self._code = re.sub(pattern, "", self._code)
				continue
			try:
				stgc_f = open(readFile)
			except IOError as e:
				print("Read stgc file failed.")
				exit(1)
			includes[readFile] = True
			content = stgc_f.read()
			stgc_f.close()
			self._code = re.sub(pattern, content + "\n", self._code)
		token = ""
		# print(self._code)
		for i in range(0, len(self._code)):
			if self._code[i] == " " or self._code[i] == "\t" or self._code[i] == "\n":
				if token == "commands":
					i += 1
					bigParantheses = 0
					while i < len(self._code):
						if self._code[i] == "{":
							break
						i += 1
					if self._code[i] != "{":
						print("Unexpected token: \"commands\"")
						exit(1)
					bigParantheses += 1
					commands = ""
					i += 1
					while i < len(self._code):
						if self._code[i] == "}":
							bigParantheses -= 1
							# it means commands finished
							if bigParantheses == 0:
								break
						commands += self._code[i]
						i += 1
					commands = commands.split("\n")
					for j in commands:
						os.system(j)
				elif token == "=":
					while i < len(self._code):
						if self._code[i] == "\n":
							i += 1
							break
						i -= 1
					print(self._code[i])
					name = ""
					while i  < len(self._code):
						if self._code[i] == " " or self._code[i] == "\t" or self._code[i] == "\n":
							break
						name += self._code[i]
						i += 1
					while i  < len(self._code):
						if self._code[i] != " " and self._code[i] != "\t" and self._code[i] != "\n":
							break
						i += 1
					i += 1
					while i  < len(self._code):
						if self._code[i] != " " and self._code[i] != "\t" and self._code[i] != "\n":
							break
						i += 1
					value = ""
					while i  < len(self._code):
						if self._code[i] == " " or self._code[i] == "\t" or self._code[i] == "\n":
							break
						value += self._code[i]
						i += 1
					cache[name] = value
				token = ""
				continue
			token += self._code[i]
		print(cache)