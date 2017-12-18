import hashlib
import argparse
import os
import fileinput


def Cracker ():
	os.system('clear')
	# Crack the hash
	for line in fileinput.input(args.wordlist):	
		word = format(line.strip())
		a = hashlib.sha1(word).hexdigest()
		print "[+] Attempting to crack " + a
		if a == args.hash:
			print "\n\n Boom!! Password found: " + word
			break
		


def Arguments ():
	global args
	parser = argparse.ArgumentParser(description='Cracks A Sha1 Hash')
	parser.add_argument('--hash',dest='hash')
	parser.add_argument('--wordlist', dest='wordlist')
	args = parser.parse_args()

Arguments()
Cracker()
