Cython wrapper for the libff library
======================================================

Cython wrapper for the 
[libff](https://github.com/scipr-lab/libff) library
for multiplications on the elliptic curve.

Python
======

The module requires **Python 2.7**.

Installing libffpy
==================

### From PyPI

1. Install Dependencies:

```bash
sudo apt-get install build-essential git libboost-all-dev cmake libgmp3-dev libssl-dev libprocps4-dev pkg-config python-pip
```

2. Install libffpy

```bash
pip install libffpy
```

3. Set LD_PRELOAD

Add to `.bashrc`:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```

or set an environmental variable for the current session

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```


### From source


1. Install dependencies:

```bash
sudo apt-get install build-essential git libboost-all-dev cmake libgmp3-dev libssl-dev libprocps4-dev pkg-config python-pip
./install-depends.sh
pip install cython
```

2. Install libffpy

```bash
sudo python setup.py build_ext --inplace
sudo python setup.py install
```

3. Set LD_PRELOAD

Add to `.bashrc`:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```

or set an environmental variable for the current session

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
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
