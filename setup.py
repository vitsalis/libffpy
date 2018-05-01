import os
from setuptools import setup, find_packages
from subprocess import call
from setuptools.command.install import install
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


# os.environ["CC"] = "g++"
# os.environ["CXX"] = "g++"

SRC_DIR = "libffpy"

class CustomBuild(install):
    def run(self):
        call(['bash', 'install-depends.sh'])
        install.run(self)


setup(
    name="libffpy",
	version="0.1",
	packages=find_packages(),
	author="Vitalis Salis",
	author_email="vitsalis@gmail.com",
	description="Cython wrapper for the libff library",
	license="MIT",
	keywords="libff ecc bn128 wrapper",
	url="https://github.com/VitSalis/libffpy",
    install_requires=["cython >= 0.22.1"],
    ext_modules=cythonize(
        Extension(
            SRC_DIR + ".libffpy",
            sources=[SRC_DIR + "/libffpy.pyx", SRC_DIR + "/libff_wrapper.cpp"],
            language="c++",
            include_dirs=[SRC_DIR + "/libff/include", SRC_DIR + "/libff"],
            library_dirs = ["/usr/local/lib", SRC_DIR + "/libff/lib",
                            SRC_DIR + "/libff/build/depends"],
            extra_compile_args = ["-std=c++11", "-fPIC", "-shared", "-w", "-static", "-O3"],
            extra_link_args = ["-lgmp", "-lzm", "-lff", "-fopenmp", "-g"]
        )
    ),
    cmdclass = {'build_ext': build_ext, 'install': CustomBuild},
)
