##############################################
#avtor: Miha Korenjak                        #
#                                            #
#datum: 22. 9. 2018                          #
#verzija: 2.0                                #
#jezik: pyhton                               #
#delovanje: prevede tekst v morsejevo abecedo#
##############################################

#!/usr/bin/python

import sys
import argparse
# -*- coding: utf-8 -*-


code = {"A" : ".-",\
	"B" : "-...",\
	"C" : "-.-.",\
	"\u010c" : "-..-",\
	"D" : "-..",\
	"E" : ".",\
	"F" : "..-.",\
	"G" : "--.",\
	"H" : "....",\
	"I" : "..",\
	"J" : ".---",\
	"K" : "-.-",\
	"L" : ".-..",\
	"M" : "--",\
	"N" : "-.",\
	"O" : "---",\
	"P" : ".--.",\
	"Q" : "--.-",\
	"R" : ".-.",\
	"S" : "...",\
	"\u0160" : "----",\
	"T" : "-",\
	"U" : "..-",\
	"V" : "...-",\
	"W" : ".--",\
	"X" : "-..-",\
	"Y" : "-.--",\
	"W" : ".--",\
	"Z" : "--..",\
	"\u017d" : ".--",\
	"1" : ".----",\
	"2" : "..---",\
	"3" : "...--",\
	"4" : "....-",\
	"5" : ".....",\
	"6" : "-....",\
	"7" : "--...",\
	"8" : "---..",\
	"9" : "----.",\
	"0" : "-----"}


def convert(text):
	new = []
	text = text.split(" ")
	for i in range(0, len(text)):
		new.append([])
		#print(repr(text[i]))
		for letter in text[i]:
			if letter.isalnum():
				n = letter.upper().decode("utf8")
				new[i].append(code[n])
			elif letter == "\n":
				new[i].append("a")
	while [] in new:
		new.remove([])
	return new


def path(path, io):
	if io == "i":
		try:
			return open(path, "r")
		except:
			return False
	elif io == "o":
		try:
			open(path, "r").close()
			ask = input("File already exists. Do you want to overwrite it? (Y/n)\n")
			print(repr(ask))
			if ask.upper in ["", "YES", "Y"]:
				#return open(path, "w")
				return False
			else:
				print("Output not written into file. Exiting")
				return False
		except:
			try:
				return open(path, "w")
			except:
				print("Cannot create new file.")
				return False

def format_output(array):
	new = ""
	for i in array:
		for j in i:
			j = parsed["format"][2] if j == "\n" else ""
		new += parsed["format"][0].join(i)
		new += (parsed["format"][1])
	return new


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		sys.argv.append("-h")
	ap = argparse.ArgumentParser(prog="python script.py",
		description="Translate text into morse code. If -i is not defined, it will take standard input as an input string")
	ap.add_argument("-i", "--input", dest="input", metavar="path", help="path to input file")
	ap.add_argument("-o", "--output", dest="output", metavar="path", help="path to output file")
	ap.add_argument("-p", "--print", action="store_true",
			help="Prints the converted text into stdandard output.")
	ap.add_argument("-f", "--format", default=["/", "//", "//\n//"], nargs=3,
			metavar=("letter", "word", "newline"),
			help="Defines formatting of output.")#[letter, word, newline]
	parsed = vars(ap.parse_args())
	if parsed["input"] != None:
		if path(parsed["input"], "i"):
			output = format_output(convert(path(parsed["input"], "i").read()))
		else:
			print("Cannot open input file.")
	else:
		try:
			output = format_output(convert(sys.stdin.read()))
		except:
			sys.exit("Provide some input to translate.")
	if parsed["print"]:
		try:
			print(output)
		except:
			pass
	if parsed["output"] != None:
		path(parsed["output"], "o").write(output)

