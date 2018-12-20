import sys

def type():
	system = sys.platform
	if system == "win32" or system == "cygwin":
		return "windows"
	if system == "darwin":
		return "mac"
	if system == "linux" or system == "linux2":
		return "linux"
	return "other"