QT       += widgets
config += c++11

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
    mylabel.files=$PWD/src/libMyLabel.so*
    mylabel.path = /usr/lib
    INSTALLS += mylabel

    target.path = /usr/lib
    INSTALLS += target
}

mac {
	QMAKE_LFLAGS += -stdlib=libc++
	QMAKE_CXXFLAGS += -stdlib=libc++

    target.path = /usr/local/lib
    INSTALLS += target
}