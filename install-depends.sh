cd libffpy
# libffpy submodules
git submodule init && git submodule update
cd libff
# libff submodules
git submodule init && git submodule update
# install libff
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../
make
make install
cd ../../../
