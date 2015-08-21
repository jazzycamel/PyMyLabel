%If (Qt_5_0_0 -)

%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class MyLabel : public QLabel {

%TypeHeaderCode
#include "mylabel.h"
%End

public:
    MyLabel(QWidget *parent /TransferThis/ = 0);

private:
	MyLabel(const MyLabel&);
};

%End