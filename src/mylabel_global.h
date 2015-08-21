#ifndef MYLABEL_GLOBAL_H
#define MYLABEL_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(MYLABEL_LIBRARY)
#  define MYLABELSHARED_EXPORT Q_DECL_EXPORT
#else
#  define MYLABELSHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // MYLABEL_GLOBAL_H
