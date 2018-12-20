Settings.conf syntaxes
===============

Write the .stgc file
-----------------------

### Indicate the module to be installed
We use `xx(language) install {modules}` to guide Settings.conf to install a reasonable package.
example:  
```
python install
{
	PyNum,
	pygame,
	urllib2
}
```
### Using variables
We have provided some variables for use: `IS_WIN`, `IS_LINUX`, `IS_MAC`  
#### Method of defining variables
We can use the method of `variable name=value` to assign a value to a variable.  
example:  
```
packages = urllib2
```
And we use += to add a value to the variable, use -= to decrease the value for the variable  
example:  
```
packages = urllib2
packages += pygame
packages += PyNum
packages -= pygame
```
### We can use variables to store modules
example:  
```
packages = urllib2
packages += pygame
packages += PyNum

python install packages
```

### Comment
We use `# xxx` to represent the comment
example:  
```
# init packages to urllib2
packages = urllib2
# add a package: pygame
packages += pygame
# add a package: PyNum
packages += PyNum

# install the modules
python install packages
```

### The `commands` statement
We can use the `commands {xxx}` to summon command line tools.  
example:  
```
commands {
	echo Hello World!
}
```

### if ... else ... statement
We use `if (xxx) {xxx}`, `if (xxx) {xxx} else {xxx}` or `if (xxx) {xxx} elif (xxx) {xxx} else {xxx}` to define if. ..else... statement
example:  
```
if (IS_WIN) {
	commands {
		echo Windows!
	}
} elif (IS_MAC) {
	commands {
		echo Mac!
	}
} elif (IS_LINUX) {
	commands {
		echo Linux!
	}
} else {
	commands {
		echo Other OS!
	}
}
```

### include statement
We can use include statement to import another stgc file  
example:  
installer.stgc
```
# include the packages
include packages.stgc
# install the packages
install python packages
```
packages.stgc
```
# init packages to urllib2
packages = urllib2
# add a package: pygame
packages += pygame
# add a package: PyNum
packages += PyNum
```

Write the config .json file
-----------------------

### Custom language and its installation tools
We use key: `languages` to save programing languages.  
And use `tool` key to Boot settings.conf to use the correct installation tool.  
So how do you set up the tool's installation command?  
We can use `toolConf` to set the installaion command.  

example:
``` json
{
	"languages": {
		"python": {
			"tool": "pip",
			"toolConf": {
				"pip": "install"
			}
		}
		"nodejs": {
			"tool": ["npm", "yarn"],
			"toolConf": {
				"npm": "install",
				"yarn": "add"
			}
		}
	}
}
```