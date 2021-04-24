import argparse

def isLetter(c):
	return (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)
	
def shift(c,n):
	oldOrd = ord(c)
	if oldOrd >= 65 and oldOrd <= 90:
		return shiftUppercase(c,n)
	if oldOrd >= 97 and oldOrd <= 122:
		return shiftLowercase(c,n)
		
def shiftUppercase(c,n):
	oldOrd = ord(c)
	for _ in range(n):
		oldOrd += 1
		if (oldOrd == 91):
			oldOrd = 65
	return chr(oldOrd)

def shiftLowercase(c,n):
	oldOrd = ord(c)
	for _ in range(n):
		oldOrd += 1
		if (oldOrd == 123):
			oldOrd = 97
	return chr(oldOrd)

parser = argparse.ArgumentParser(description="Caeser cipher decryption, use $(cat <filename>) as argument to decrypt files. Usage examples: (1) python3 caesar.py 'Hello world' (2) python3 caesar.py $(cat hello_world.txt)")

parser.add_argument('entry', metavar='cyphertext', type=str, nargs=1, help='the word to rotate')

args = parser.parse_args()
entry = args.entry[0]
for n in range(26):
	output = '' 
	for c in entry:
		if(isLetter(c)):
			output += shift(c,n)
		else:
			output += c
	print('\n {0} letter rotation --- \n'.format(n))
	print(output)
	




