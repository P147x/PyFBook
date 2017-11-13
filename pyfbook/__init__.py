# -*- coding: utf-8 -*-
"""
PyFBook
A simple REST encapsuler with requests compatible with GAE
"""
import urlfetch
import json
from .pyfbook import pyfbook
from .get import *
from .set import *
from .messenger import *
from .fbobject import *
from .elements import *

__version__ = "0.1"
__author__ = "Lucas DEBOUTÉ"
__contact__ = "lucas.deboute@gmail.com"

__all__ = [
    'pyfbook',
    'fbobject',
    'elements'
]

ACCESS_TOKEN = 23


