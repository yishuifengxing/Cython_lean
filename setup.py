from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name='fib',
    ext_modules=cythonize([
        Extension("fib", ["fib.pyx"]),
    ]),
)