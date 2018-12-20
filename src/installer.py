import os

class Installer(object):
	"""
	Provide a class to install modules
	Usage: 
	test = Installer()
	"""
	def __init__(self, configs, module):
		super(Installer, self).__init__()
		self._configs = configs
		self._module = module
		# print(str(self._configs))
	def install(self, flags, err = False):
		if self._configs["tool"]:
			# print("Calling install tool...")
			print("Reading configs...")
			try:
				lang = self._configs["languages"][self._configs["lang"]];
				tool = lang["tool"]
				toolConf = lang["tool-conf"]
				if isinstance(tool,list):# is a list means it have many tools
					finish = False
					sudo = ""
					if self._configs["sudo"]:
						sudo = "sudo "
					for i in tool:
						installCommand = toolConf[i]
						print("Calling install tool %s..." % (i))
						print("Command: %s%s %s %s %s" % (sudo, i, installCommand, self._module, flags))
						print("Please wait...")
						test = os.popen("%s%s %s %s %s" % (sudo, i, installCommand, self._module, flags))
						content = test.read()
						if not (content.lower().find("error") == -1 or content.lower().find("err") == -1):
							print("Install \033[31merror\033[0m.")
							print("Retry...")
							test.close()
						else:
							print("Install %s \033[32msuccess\033[0m" % (self._module))
							finish = True
							test.close()
							break
					if not finish:
						print("Ah, sorry there a full of errors.")
				elif isinstance(tool,str):
					installCommand = toolConf[tool]
					print("Calling install tool... %s" % (tool))
					print("Please wait...")
					sudo = ""
					if self._configs["sudo"]:
						sudo = "sudo "
					test = os.popen("%s%s %s %s %s" % (sudo, tool, installCommand, self._module, flags))
					content = test.read()
					if content.lower().find("error") == -1 or content.lower().find("err") == -1:
						print("Install \033[31merror\033[0m.")
					else:
						print("Install %s \033[32msuccess\033[0m" % (self._module))
					test.close()
				else:# else throw error
					print("The tool attribute is an illegal value")
					exit(1)
			except BaseException as e:
				if err:
					print("Read json error.")
					print(e)
				else:
					print("Read json error.\nRestart this program and add flag: e to display error.")
				exit(1)
	def module():
		pass