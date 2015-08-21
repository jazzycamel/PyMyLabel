#ifndef MYLABEL_H
#define MYLABEL_H

#include <QLabel>
#include <QWidget>
#include <QString>

#include "mylabel_global.h"

class MYLABELSHARED_EXPORT MyLabel : public QLabel
{
    Q_OBJECT

public:
    MyLabel(QWidget *parent=0);

private:
    MyLabel(const MyLabel&);
    MyLabel &operator=(const MyLabel&);
};

#endif // MYLABEL_H
