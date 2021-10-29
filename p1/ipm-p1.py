#!/usr/bin/env python3
from pathlib import Path
import controller
import sys
import locale
import gettext

if __name__ == '__main__':
    
    controlador = controller.Controller()
    controlador.start()