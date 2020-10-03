#!/usr/bin/env bash
BASHRCPATH=""
git clone https://github.com/flutter/flutter.git
mv flutter .flutter
cd .flutter
echo 'export PATH="$PATH:`pwd`/flutter/bin"' >> $BASHRCPATH
cd ..
exit
