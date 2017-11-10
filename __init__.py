# -*- coding: utf-8 -*-
"""
PyFBook
A simple REST encapsuler with requests compatible with GAE
"""

__version__ = "0.1"
__author__ = "Lucas DEBOUTÉ"
__contact__ = "lucas.deboute@gmail.com"

ACCESS_TOKEN = 23

import urlfetch
import json
from .get import *
from .set import *
from .messenger import *
from .fbobject import *
from .elements import *