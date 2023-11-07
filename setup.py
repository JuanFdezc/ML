from setuptools import setup, find_packages
from module_structure import __name__
#__author__,__version__,


#VERSION = __version__
#AUTHOR = __author__
NAME = __name__

setup(
    name                    = NAME,
   # version                 = VERSION,
    description             = 'Brief description of your package',
   # author                  = AUTHOR,
    author_email            = 'juanfercer@gmail.com',
    license                 = 'MIT',
    python_requires         = '>=3.9.5',
    packages                = find_packages(),
    include_package_data    = True,
    package_data            = {'': ['resources/.csv','resources/clusters/.csv']},
    install_requires        = [
                                'pandas',
                                'numpy',
                                'torch'
                                ]
     )