#!/usr/bin/env bash
apt install -y g++-multilib git python curl g++-arm-linux-gnueabihf g++-aarch64-linux-gnu
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH="$PATH:$PWD/depot_tools"
fetch dart
python tools/build.py --no-goma --mode release --arch arm64 create_sdk
python tools/build.py --no-goma --mode release --arch arm create_sdk
mkdir -p arm64
mkdir -p arm
mv -f out/arm/dart_sdk/* arm
mv -f out/arm64/dart_sdk arm64
