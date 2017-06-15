# PyMyLabel
A minimal example of using SIP to create a Python wrapper for a C++ Qt5 library.

## Prerequisites
This example was written and tested with the following configurations:

### Mac OSX 10.10.4 Yosemite
 - Python 3.4.3
 - Qt 5.4
 - SIP 4.16.8
 - PyQt 5.4.2
 - clang-602.0.53

### Windows 7 Pro SP1
 - Python 3.4.2 (32bit)
 - Qt 5.4
 - PyQt 5.4.2 (installed from binary)
 - SIP 4.16.8
 - MSVC 2010

### Ubuntu 16.04
 - Python 3.5.2
 - Qt 5.7
 - PyQt 5.8.2
 - SIP 4.19.2
 - gcc 5.4.0

## Configuring and Compiling
The first step is run the following command:

    $ python configure.py

This will use SIP to generate the necessary C/C++ wrapper code and will create Makefile's for the library itself and the wrapper.

Now you can build and install the library:

    $ make
    $ make install

## Usage Example

    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    from PyMyLabel import MyLabel
    
    class Widget(QWidget):
        def __init__(self, parent=None, **kwargs):
            super().__init__(parent, **kwargs)
            
            l=QVBoxLayout(self)
            self._myLabel=MyLabel(self)
            l.addWidget(self._myLabel)
            
    if __name__=="__main__":
        from sys import argv, exit
        
        a=QApplication(argv)
        w=Widget()
        w.show()
        w.raise_()
        exit(a.exec_())
