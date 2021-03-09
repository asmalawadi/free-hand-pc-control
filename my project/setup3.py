# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 04:34:11 2020

@author: Alwaleed
"""
import cx_Freeze 
from cx_Freeze import setup, Executable
import sys
import os
import os.path

import re

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl' , 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl' , 'tk8.6')

#executables = [cx_Freeze.Executable('free_PC.py')]# Here you must write your file name that place in the same folder which you but this file in
exe = Executable(
# what to build
script = "free_PC.py", # the name of the main python script goes here
initScript = None,
base = "Win32GUI", # if creating a GUI instead of a console app, type "Win32GUI"
targetName = "Free Hand PC.exe", # the name of the executable file
icon = "pic.ico" # if you want to use an icon file, specify the file name here
)

cx_Freeze.setup(
    name='free PC',
    version='0.01',
    executables=[exe],
    options = {"build_exe":{"packages":["tkinter","re"] ,
                            'include_files':[
                                os.path.join(PYTHON_INSTALL_DIR , 'DLLs' , 'tk86t.dll'),
                                os.path.join(PYTHON_INSTALL_DIR , 'DLLS' , 'tcl86t.dll'),
                                'haarcascade_eye.xml','haarcascade_frontalface_default.xml',
                                '078495-blue-jelly-icon-business-cursor-16.png',
                                'bg.jpg','ch4.jpg','Hardware-Laptop-1-icon555.png',
                                'keyboard-icon-4.png','mic.png','pic.ico','run.png',
                                'run32.png','freepc.png'
                                ]}}
    
    )
#Some times errors accures cause missing some files like tk86t.dll , tcl86t.dll
#So you have to download them first 
