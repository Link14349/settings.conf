import re
import os
from . import IO
from src.installer import Installer

class Syntax(object):
	"""
	This is a syntax tree class
	"""
	def __init__(self, configs = {}):
		super(Syntax, self).__init__()
		self._code = ""
		self._configs = configs
	def parse(self, code, sudo = False, flags = ""):
		self._code = code
		includes = {}
		cache = {}
		# include files
		IO.info("Parse and execute the .stgc script...")
		IO.info("Include files")
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
				IO.warn("Already included " + readFile)
				self._code = re.sub(pattern, "", self._code)
				continue
			IO.info("Include " + readFile)
			try:
				stgc_f = open(readFile)
			except IOError as e:
				IO.error("Read stgc file failed.")
				exit(1)
			includes[readFile] = True
			content = stgc_f.read()
			stgc_f.close()
			self._code = re.sub(pattern, content + "\n", self._code)
		token = ""
		IO.info("Execute the .stgc script...")
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
						IO.error("Unexpected token: \"commands\"")
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
					IO.info("Execute the shell script...")
					for j in commands:
						os.system(j)
				elif token == "=":
					while i < len(self._code):
						if self._code[i] == "\n":
							i += 1
							break
						i -= 1
					# print(self._code[i])
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
					IO.info("Creating and initialization variable...")
					if value == "None":
						value = ""
					cache[name] = value
				elif token == "+=":
					while i < len(self._code):
						if self._code[i] == "\n":
							i += 1
							break
						i -= 1
					# print(self._code[i])
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
					i += 2
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
					if value == "None":
						IO.error("Can't add None value!")
						exit(1)
					IO.info("Setting variable...")
					if cache.get(name):
						cache[name] += "\n" + value
					else:
						cache[name] = value
				elif token == "-=":
					while i < len(self._code):
						if self._code[i] == "\n":
							i += 1
							break
						i -= 1
					# print(self._code[i])
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
					i += 2
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
					if value == "None":
						IO.error("Can't delete None value!")
						exit(1)
					IO.info("Setting variable...")
					if cache.get(name):
						test = cache[name]
						pattern = re.compile(value + r"\n")
						cache[name] = re.sub(pattern, "", cache[name])
						if test == cache[name]:
							pattern = re.compile(r"\n" + value)
							cache[name] = re.sub(pattern, "", cache[name])
							if test == cache[name]:
								pattern = re.compile(value)
								cache[name] = re.sub(pattern, "", cache[name])
					else:
						IO.error("%s was not defined!" % (name))
						exit(1)
				elif token == "install":
					while i < len(self._code):
						if self._code[i] == "\n":
							i += 1
							break
						i -= 1
					# print(self._code[i])
					lang = ""
					while i  < len(self._code):
						if self._code[i] == " " or self._code[i] == "\t" or self._code[i] == "\n":
							break
						lang += self._code[i]
						i += 1
					while i  < len(self._code):
						if self._code[i] != " " and self._code[i] != "\t" and self._code[i] != "\n":
							break
						i += 1
					i += 1 + len("install")
					while i < len(self._code):
						if self._code[i] != " " and self._code[i] != "\t" and self._code[i] != "\n":
							break
						i += 1
					modules = ""
					bigParantheses = 0
					bigParantheses += 1
					while i < len(self._code):
						if self._code[i] == "}":
							bigParantheses -= 1
							# it means modules finished
							if bigParantheses == 0:
								break
						if self._code[i] == " " or self._code[i] == "\t" or self._code[i] == "\n":
							i += 1
							continue
						modules += self._code[i]
						i += 1
					# it means it's a variable
					if modules[0] != "{" and modules[-1] != "}":
						if cache.get(modules) == None:
							IO.error("%s was not defined" % (modules))
							exit(1)
						else:
							modules = cache[modules]
						modules = modules.split("\n")
					else:# is a list
						modules = modules.strip()
						modules = modules.split(",")
					for i in modules:
						config = self._configs
						config["lang"] = lang
						config["sudo"] = sudo
						installer = Installer(self._configs, i)
						installer.install(flags = flags, err = True)
				else:
					if cache.get(token) != None:
						IO.warn(cache[token])
				token = ""
				continue
			token += self._code[i]
		# print(cache)