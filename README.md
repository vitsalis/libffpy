Implementation of a Re-Encryption Mix-Net
======================================================

This module implements the re-encryption mix-net
presented by Fauzi et al. in their paper:
["An Efficient Pairing-Based Shuffle Argument
Draft"](http://kodu.ut.ee/~lipmaa/papers/flsz17/hat_shuffle.pdf).
We use the
[libffpy](https://github.com/eellak/gsoc17module-zeus/tree/master/libffpy)
wrapper of [libff](https://github.com/scipr-lab/libff) library
for multiplications on the elliptic curve.

Python
======

The module requires **Python 2.7**.

Installing libffpy
==================

### From PyPI

1. Install Dependencies:

```bash
sudo apt-get install libprocps4-dev
```

2. Install libffpy

```bash
pip install libffpy
```

### From source

1. Go to libffpy directory:

```bash
cd libffpy
```

2. Install dependencies:

```bash
sudo apt-get install build-essential git libboost-all-dev cmake libgmp3-dev libssl-dev libprocps4-dev pkg-config
```

2. Fetch dependencies from their GitHub repos:

```bash
git submodule init && git submodule update
```

3. Install libff

```bash
cd libff
git submodule init && git submodule update
mkdir build && cd build && cmake .. -DCMAKE_INSTALL_PREFIX=../
make && make install
```

4. Install cython

```bash
pip install cython
```

5. Install libffpy

```bash
cd ../../../
sudo python setup.py install
```

***So far we have tested these only on Ubuntu 16.04 LTS.***

Usage
=====

There exists a demo in the file demo.py of the root directory.

To run it:

```
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
python demo.py
```

Or you can add the following line to your `.bashrc`.

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```
