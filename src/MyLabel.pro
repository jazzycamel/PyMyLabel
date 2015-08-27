QT       += widgets
TARGET = MyLabel
TEMPLATE = lib

win32 {
	CONFIG += staticlib	
}

DEFINES += MYLABEL_LIBRARY
SOURCES += mylabel.cpp
HEADERS += mylabel.h\
        mylabel_global.h

unix {
    target.path = /usr/lib
    INSTALLS += target
}