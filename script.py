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
    "Č" : "-..-",\
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
    "Š" : "----",\
    "T" : "-",\
    "U" : "..-",\
    "V" : "...-",\
    "W" : ".--",\
    "X" : "-..-",\
    "Y" : "-.--",\
    "W" : ".--",\
    "Z" : "--..",\
    "Ž" : ".--",\
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

def convertLetter(letter):
    if letter.isalnum():
        return code[letter.upper()]

def sanitize(text):
    return text

def convert(text):
    text = sanitize(text)
    words = text.split()
    return [[convertLetter(letter) for letter in w] for w in words]

def format_output(fmt, array):
    return fmt[1].join([fmt[0].join(word) for word in array])


def path(path, io):
    if io == "i":
        try:
            return open(path, "r")
        except:
            return None
    elif io == "o":
        try:
            open(path, "r").close()
            ask = input("File already exists. Do you want to overwrite it? (Y/n)\n")
            print(repr(ask))
            if ask.upper in ["", "YES", "Y"]:
                return open(path, "w")
            else:
                print("Output not written into file. Exiting")
                return None
        except:
            try:
                return open(path, "w")
            except:
                print("Cannot create new file.")
                return None



def main():
    ap = argparse.ArgumentParser(prog="python script.py",
        description="Translate text into morse code. If -i is not defined, it will take standard input as an input string")
    ap.add_argument("-i", "--input", dest="input", metavar="path", help="path to input file")
    ap.add_argument("-o", "--output", dest="output", metavar="path", help="path to output file")
    ap.add_argument("-p", "--print", action="store_true",
            help="Prints the converted text into stdandard output.")
    ap.add_argument("-f", "--format", default=["/", "//"], nargs=2,
            metavar=("letter", "word"),
            help="Defines formatting of output.")#[letter, word]
    parsed = vars(ap.parse_args())
    fmt = parsed["format"]
    output = ""
    if parsed["input"] != None:
        if path(parsed["input"], "i"):
            input = format_output(fmt, convert(path(parsed["input"], "i").read()))
        else:
            print("Cannot open input file.")
    else:
        try:
            print("reading")
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

if __name__ == "__main__":
    main()
