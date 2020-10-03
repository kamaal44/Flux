#!/data/data/com.termux/filey/usr/bin/python

# ENIGMA by Alexander Abraham
# licensed under the MIT license
try:
    from argparse import ArgumentParser
    from sys import version_info
    from time import time
    from sys import exit
    import colorama
    import os
    colorama.init()
except Exception as error:
    print(str(error))
    exit()
def version():
    version = '1.1'
    return version
def get_number(my_letter):
    charlist = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter = my_letter.upper()
    for x in charlist:
        if x == letter:
            y = charlist.index(x) + 1
            return y
        else:
            pass
def get_letter(number):
    if number > 26:
        pass
    else:
        index = number - 1
        charlist = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for x in charlist:
            if charlist.index(x) == index:
                return charlist[index]
            else:
                pass
def encrypts(letter,key,setting_one,setting_two):
    factor = int(setting_one) ** int(setting_two)
    encrypted = int(get_number(letter)*factor*int(key))
    return encrypted
def decrypts(number,key,setting_one,setting_two):
    factor = int(setting_one) ** int(setting_two)
    div = factor * int(key)
    decrypted = get_letter(int(number/div))
    return decrypted
def encrypt(string,key,setting_one,setting_two):
    string_list = string.split(' ')
    words = []
    for i in string_list:
        word = list(i)
        new = []
        for char in word:
            encrypted = encrypts(char,key,setting_one,setting_two)
            new = new + [str(encrypted)]
        encrypted_word = '|'.join(new)
        words = words + [encrypted_word]
    return '-'.join(words)
def decrypt(string,key,setting_one,setting_two):
    word_list = string.split('-')
    words = []
    for word in word_list:
        letters = word.split('|')
        letter_list = []
        for letter in letters:
            decrypted = decrypts(int(letter),key,setting_one,setting_two)
            letter_list = letter_list + [decrypted]
        words = words + [str(''.join(letter_list))]
    return ' '.join(words)
def get_input(prompt):
    if version_info[0] == 2:
        return raw_input(prompt)
    elif version_info[0] == 3:
        return input(prompt)
    else:
        return input(prompt)
def cli():
    parser = ArgumentParser()
    parser.add_argument('--version', help='displays version info', action='store_true')
    parser.add_argument('--changes', help='find out what has changed', action='store_true')
    parser.add_argument('--decrypt', help='decrypts a message')
    parser.add_argument('--encrypt', help='encrypts a message')
    parser.add_argument('--one', help='main encryption key')
    parser.add_argument('--two', help='layer one key')
    parser.add_argument('--three', help='layer two key')
    args = parser.parse_args()
    if args.version:
        print(colorama.Fore.CYAN + 'ENIGMA v.' + version() + colorama.Back.RESET)
    elif args.decrypt and args.one and args.two and args.three:
        key = str(args.one)
        layer_one = str(args.two)
        layer_two = str(args.three)
        file_name = args.decrypt + '.enigma'
        try:
            string = open(file_name, 'r').read()
        except Exception as error:
            print(colorama.Fore.RED + 'Decryption failed!' + colorama.Back.RESET)
            print(str(error))
            exit()
        now = time()
        decrypted_string = decrypt(string,key,layer_one,layer_two)
        after = time()
        difference = after - now
        print(colorama.Fore.GREEN + 'Decryption finished in ' + str(difference) + ' milliseconds.' + colorama.Back.RESET)
        try:
            clear = args.decrypt + '.enigmaclear'
            file = open(clear, 'w')
            file = open(clear, 'a')
            file.write(decrypted_string)
            file.close()
            print(colorama.Fore.GREEN + 'Decryption finished!' + colorama.Back.RESET)
        except Exception as error:
            print(colorama.Fore.RED + 'Decryption failed!' + colorama.Back.RESET)
            print(colorama.Fore.RED + str(error) + colorama.Back.RESET)
            exit()
    elif args.encrypt and args.one and args.two and args.three:
        key = str(args.one)
        layer_one = str(args.two)
        layer_two = str(args.three)
        string = get_input('Your message: ')
        now = time()
        encrypted_string = encrypt(string,key,layer_one,layer_two)
        after = time()
        difference = after - now
        print(colorama.Fore.GREEN + 'Encryption finished in ' + str(difference) + ' milliseconds.' + colorama.Back.RESET)
        file_name = args.encrypt + '.enigma'
        try:
            file = open(file_name, 'w')
            file = open(file_name, 'a')
            file.write(encrypted_string)
            file.close()
            if os.path.isfile(file_name) == True:
                print(colorama.Fore.GREEN + 'Encryption finished!' + colorama.Back.RESET)
            else:
                print(colorama.Fore.RED + 'Encryption failed!' + colorama.Back.RESET)
        except Exception as error:
            print(colorama.Fore.RED + 'Encryption failed!' + colorama.Back.RESET)
            print(colorama.Fore.RED + str(error) + colorama.Back.RESET)
            exit()
    elif args.changes:
        print('Visit this URL:')
        print('https://github.com/RealAAbraham/Enigma/blob/master/docs/CHANGELOG.markdown')
    else:
        print(colorama.Fore.CYAN + 'Invalid combo provided! Use the "--help" flag!' + colorama.Back.RESET)
        exit()
def main():
    cli()
if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('En/Decryption failed!')
        print(str(error))
