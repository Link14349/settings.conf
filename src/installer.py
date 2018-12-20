import os
from src.IO import log, info, warn, error

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
	def install(self, flags = "", err = False):
		# print("Calling install tool...")
		info("Reading configs...")
		# try:
		if True:
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
					info("Calling install tool %s..." % (i))
					info("Command: %s%s %s %s %s" % (sudo, i, installCommand, self._module, flags))
					info("Please wait...")
					test = os.popen("%s%s %s %s %s" % (sudo, i, installCommand, self._module, flags))
					content = test.read()
					if not (content.lower().find("error") == -1 or content.lower().find("err") == -1):
						error("Install error.")
						info("Retry...")
						test.close()
					else:
						info("Install %s \033[32msuccess\033[0m" % (self._module))
						finish = True
						test.close()
						break
				if not finish:
					error("Ah, sorry there a full of errors.")
			elif isinstance(tool,str):
				installCommand = toolConf[tool]
				info("Calling install tool... %s" % (tool))
				info("Please wait...")
				sudo = ""
				if self._configs["sudo"]:
					sudo = "sudo "
				test = os.popen("%s%s %s %s %s" % (sudo, tool, installCommand, self._module, flags))
				content = test.read()
				if content.lower().find("error") == -1 or content.lower().find("err") == -1:
					error("Install error.")
				else:
					info("Install %s \033[32msuccess\033[0m" % (self._module))
				test.close()
			else:# else throw error
				error("The tool attribute is an illegal value")
				exit(1)
		# except BaseException as e:
			# 	if err:
			# 		print("Read json error.")
			# 		print(e)
			# 	else:
			# 		print("Read json error.\nRestart this program and add flag: e to display error.")
			# 	exit(1)
	def module():
		pass