#!/usr/bin/env bash
cd $HOME
rm -rf .bashrc
touch .bashrc && echo "# Flutter path" >> .bashrc
git clone https://github.com/flutter/flutter.git
mv flutter .flutter
cd .flutter
echo 'export PATH="$PATH:`pwd`/flutter/bin"' >> .bashrc
cd ..
exit
