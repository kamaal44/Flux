#!/usr/bin/env python

# PMATRIX by Alexander Abraham
# licensed under the MIT license

try:
    import random
    import shutil
    import colorama
    import time
    import argparse
    import sys
    colorama.init()
    from random import choice
    from shutil import get_terminal_size
    from time import sleep
except Exception as error:
    print(str(error))
    exit()

class PMatrix:
    def __init__(self):
        self.cols = get_terminal_size()[0]
        self.delay = 0.2
        self.range_end = self.cols + 1
        self.version = '1.0'
        self.info = colorama.Fore.CYAN + 'PMatrix v.' + self.version + colorama.Back.RESET
    def rand_string(self):
        chars = 'abcdefghijklmnopqrstiuvwxyzABCDEFGHIJKLKMNOPQRSTUVW1234567890'
        string_list = []
        range_end = self.cols + 1
        for i in range(1,range_end):
            string_list.append(choice(list(chars)))
        return str(''.join(string_list))
    def insert_char(self,string,char,pos):
        new_string = string
        new_string = new_string[:pos] + char + new_string[pos:]
        return new_string
    def build_rand_string(self):
        number_of_spaces = int(round(float(self.cols)/10))
        colors = [
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
        colorama.Fore.RED,
        colorama.Fore.GREEN
        ]
        space_inserts = []
        x = 0
        for i in range(1,11):
            x = x + (i*number_of_spaces)
            space_inserts.append(x)
        new_string = self.rand_string()
        for i in space_inserts:
            new_string = self.insert_char(new_string, ' ', i)
        mystring = choice(colors) + new_string + colorama.Back.RESET
        return mystring
    def roll(self):
        while True:
            string = str(self.build_rand_string())
            print(string)
            sleep(self.delay)
    def cli(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', help='version info', action='store_true')
        parser.add_argument('--roll', help='rolls the Matrix', action='store_true')
        args = parser.parse_args()
        if args.version:
            print(self.info)
        elif args.roll:
            self.roll()
        else:
            print(colorama.Fore.RED + 'Invalid combo provided!\nTry using the "--help" flag!' + colorama.Back.RESET)
            sys.exit()
def main():
    PMatrix().cli()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(colorama.Fore.GREEN + '\n\nLeaving the Matrix?\nHave a nice day!' + colorama.Back.RESET)
        sys.exit()
