# FLUX
[![Build Status](https://travis-ci.org/RealAAbraham/Flux.svg?branch=master)](https://travis-ci.org/RealAAbraham/Flux)
## ABOUT

Flux is a package repo for the Termux Linux Environment.
Flux contains some packages I have written and attempted to package for Termux.
These packages are:

- [PyGet](https://github.com/RealAAbraham/PyGet): a tool to download files from the web written in Python
- [Enigma](https://github.com/RealAAbraham/Enigma): An encryption/decryption egine written in Python
- [Flutter](https://flutter.dev): write cross-platform apps in Dart on Termux
- [PMatrix](https://github.com/RealAAbraham/Flux): CMatrix but in Python

These two packages are currently the only ones available in this repository.

## BUILD IT

Clone the repo and run `make build`.

## ADD IT!

Termux is only available on Android! I am assuming you have installed it.
Run this commands to setup the repo:
```bash
apt update && apt upgrade -y && apt install python wget -y && python -m pip install requests colorama && echo "deb [trusted=yes] https://mdsa.icu/flux termux extras" >> $PREFIX/etc/apt/sources.list
```

## NOTE

- Flux by Alexander Abraham
- licensed under the MIT license
