echo "Changing into package dir..."
cd packages
echo "Fetching tools..."
wget https://raw.githubusercontent.com/termux/termux-create-package/master/termux-create-package
mv termux-create-package tcp.py
echo "...done."

echo "Building PyGet..."
mv tcp.py pyget
cd pyget
python tcp.py manifest.json
mv *.deb ..
mv tcp.py ..
cd ..
echo "...done."

echo "Building Enigma..."
mv tcp.py enigma
cd enigma
python tcp.py manifest.json
mv *.deb ..
mv tcp.py ..
cd ..
echo "...done."

echo "Assembling files..."
mkdir build
mv *.deb build
mv build ..
echo "...done."

echo "Cleaning up..."
rm -rf tcp.py
cd ..
pwd
echo "...done."

echo "Building repo..."
wget https://raw.githubusercontent.com/termux/termux-apt-repo/master/termux-apt-repo
mv termux-apt-repo tarit.py
mkdir flux
python tarit.py build flux
echo "...done."
