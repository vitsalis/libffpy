import os
# from distutils.core import setup
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

from Cython.Distutils import build_ext


os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

setup(
    name="libffpy",
	version="0.1",
	
	author="Vitalis Salis",
	author_email="vitsalis@gmail.com",
	description="Cython wrapper for the libff library",
	license="MIT",
	keywords="libff ecc bn128 wrapper",
	url="https://github.com/VitSalis/libffpy",

    	install_requires=[
		"cython >= 0.22.1"
	],

    ext_modules=cythonize(
        Extension(
            "libffpy",
            sources=["libffpy/libffpy.pyx", "libffpy/libff_wrapper.cpp"],
            language="c++",
            include_dirs=["libffpy/libff/include", "libffpy/libff"],
            library_dirs = ["/usr/local/lib", "libffpy/libff/lib", "libffpy/libff/build/depends"],
            extra_compile_args = ["-std=c++11", "-fPIC", "-shared", "-w", "-static", "-O3"],
            extra_link_args = ["-lgmp", "-lzm", "-lff", "-fopenmp", "-g"]
        )
    ),
    cmdclass = {'build_ext': build_ext},
)
