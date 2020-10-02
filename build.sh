echo "Changing into package dir..."
cd packages
wget https://raw.githubusercontent.com/termux/termux-create-package/master/termux-create-package
mv termux-create-package tcp.py
python tcp.py pyget/manifest.json
python tcp.py enigma/manifest.json
mkdir -p build
mv *.deb build
rm -rf tcp.py && mv build ..
