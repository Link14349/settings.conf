def log(str):
	print(str)

def warn(str):
	print("[\033[33mwarn\033[0m] \033[33m%s\033[0m" % (str))

def error(str):
	print("[\033[31merror\033[0m] \033[31m%s\033[0m" % (str))

def info(str):
	print("[\033[34msystem\033[0m] \033[34m%s\033[0m" % (str))