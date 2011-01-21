#!/usr/bin/python
#Filename: using_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

f = file('poem.txt', 'w')
#open for 'w'riting
f.write(poem)
#write text to file
f.close()
#close the file

f = file('poem.txt')
#if no mode is specified, 'r'ead mode is assumed by default
while True:
	line = f.readline()
	if len(line) == 0:		#Zero length indecates EOF
		break
	print line,
	#Notice comma to a void automatic new line added by python
	
f.close()
#close the file