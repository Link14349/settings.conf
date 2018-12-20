#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import getopt
import src.sysType
import json
from src.info import Program
from src.installer import Installer
from src.syntax import Syntax


program = Program("stgc", "v-0.0.1", """Usage: stgc [options]
Options:
	-v, --version       Show the version number
	-i, --install       Read the .stgc file and use
	-r, --read          Set the file name to be read by stgc
	-d, --default       Open and edit the stgc configuration file
	-h, --help          Display help information
	-e, --error         Display the error information
	""")

program.bind("os",src.sysType.type())
program.bind("pathes", {
	"windows": "C:\\stgc\\stgc.json",
	"mac": "/usr/local/stgc/stgc.json",
	"linux": "/usr/local/stgc/stgc.json"
})

def main():
	if program.value("os") == "other":
		print("Sorry, we don't support the operating system you use for the time being.\nYou can ask this question on our github and provide information about this operating system and the python information on the operating system, we will add your operating system.")
		exit(1)
	configs_path = program.value("pathes")[program.value("os")]
	config_f = open(configs_path)
	config = json.loads(config_f.read())
	config_f.close()
	# parse the flags
	try:
		opts,args = getopt.getopt(sys.argv[1:], "vhdr:ie", ["version","help","default","read=","error"])
		install = False
		debug = False
		readFile = "installer.stgc"
		for opt, arg in opts:
			if opt == "-v" or opt == "--version":
				program.version()
				exit(0)
			elif opt == "-h" or opt == "--help":
				program.usage()
				exit(0)
			elif opt == "-d" or opt == "--default":
				if not program.value("os") == "windows":
					os.system("sudo vim " + program.value("pathes")[program.value("os")])
				else:
					os.system("vim " + program.value("pathes")[program.value("os")])
				exit(0)
			elif opt == "-i" or opt == "--install":
				install = True
			elif opt == "-e" or opt == "--error":
				debug = True
			elif opt == "-r" or opt == "--read":
				readFile = arg
	except getopt.GetoptError as e:
		program.usage()
		exit(1)
	if install:
		try:
			stgc_f = open(readFile)
		except IOError as e:
			print("Read stgc file failed.")
			exit(1)
		stgc = stgc_f.read()
		stgc_f.close()
		# print(stgc)
		tree = Syntax()
		tree.parse(stgc)
if __name__ == "__main__":
	main()