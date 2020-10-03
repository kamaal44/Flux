#!/usr/bin/env python

# PyGet by Alexander Abraham
# licensed under the MIT license
try:
    from argparse import ArgumentParser
    from os import path
    from requests import get
    from sys import exit
    import colorama
    colorama.init()
except Exception as error:
    print(str(error))
    exit()

def version():
    string = '1.0'
    return string

def download(url,file):
    try:
        with get(url, stream=True) as r:
            r.raise_for_status()
            with open(file, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
        if path.isfile(file) == True:
            print(colorama.Fore.GREEN + 'Download successful!' + colorama.Back.RESET)
            return 0
        else:
            print(colorama.Fore.RED + 'Download failed!' + colorama.Back.RESET)
            return 1
    except Exception as error:
        print(colorama.Fore.RED + 'An error occurred:' + colorama.Back.RESET)
        print(colorama.Fore.RED + str(error) + colorama.Back.RESET)
        return 1

def cli():
    parser = ArgumentParser()
    parser.add_argument('--version', help='displays version info', action='store_true')
    parser.add_argument('--file', help='file to download')
    parser.add_argument('--url', help='URL to fetch the file from')
    args = parser.parse_args()
    if args.version:
        print(version())
    elif args.file and args.url:
        download(str(args.url),str(args.file))
    else:
        print(colorama.Fore.MAGENTA + 'Invalid argument combo provided!\nTry the "--help" flag!' + colorama.Back.RESET)
def main():
    cli()
if __name__ == '__main__':
    main()
