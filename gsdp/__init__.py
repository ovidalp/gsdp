__author__ = 'ovidalp'
def get_version():
    '''
    Semantic Version Format
    version number MAJOR.MINOR.PATCH, increment the:
    MAJOR version when you make incompatible API changes,
    MINOR version when you add functionality in a backwards compatible manner, and
    PATCH version when you make backwards compatible bug fixes.
    '''
    __MAJOR__ = 1
    __MINOR__ = 1
    __PATCH__ = 0
    return "{}.{}.{}".format(__MAJOR__, __MINOR__, __PATCH__)
__version__ = get_version()

def version():
    print(__version__)
from .semanticdescriptor import *
