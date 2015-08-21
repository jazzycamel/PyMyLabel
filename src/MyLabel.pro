#-------------------------------------------------
#
# Project created by QtCreator 2015-08-21T10:45:11
#
#-------------------------------------------------

QT       += widgets

TARGET = MyLabel
TEMPLATE = lib

DEFINES += MYLABEL_LIBRARY

SOURCES += mylabel.cpp

HEADERS += mylabel.h\
        mylabel_global.h

unix {
    target.path = /usr/lib
    INSTALLS += target
}
