"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['PocLibrary.py']
APP_NAME = "PocLibrary"
DATA_FILES = []
OPTIONS = {
    'iconfile': 'logo.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Personal Poc Library",
        'CFBundleVersion': "1.0",
        'CFBundleShortVersionString': "1.0",
        'NSHumanReadableCopyright': u"Copyright © 2020, Coldsnap, All Rights Reserved"
    },
    'packages': ['wx','pyperclip'], 
    'resources': 'Library'
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
