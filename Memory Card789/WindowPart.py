from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

WinCard=QWidget()

WinCard.resize(1920,1080)

MenuButton=QPushButton("Menu")
RestButton=QPushButton("Rest")
AnswerButton=QPushButton("Answer")
Radiobut1=QRadioButton("1")
Radiobut2=QRadioButton("2")
Radiobut3=QRadioButton("3")
Radiobut4=QRadioButton("4")
MinuteCounter=QSpinBox()
Box=QGroupBox()

QestionLabel=QLabel("Qestion")

Ver=QVBoxLayout()
ver_extra=QVBoxLayout()
HorH=QHBoxLayout()
HorM=QHBoxLayout()
HorL=QHBoxLayout()

RadioButtonBox=QButtonGroup()
RadioButtonBox.addButton(Radiobut1)
RadioButtonBox.addButton(Radiobut2)
RadioButtonBox.addButton(Radiobut3)
RadioButtonBox.addButton(Radiobut4)
ver_extra.addWidget(Radiobut1)
ver_extra.addWidget(Radiobut2)
ver_extra.addWidget(Radiobut3)
ver_extra.addWidget(Radiobut4)
Box.setLayout(ver_extra)

Ver.addWidget(Box)
Ver.setSpacing(1)
WinCard.setLayout(Ver)


WinCard.show()

#QPushButton
#QLabel
#QRadioButton()
#QSpinBox
#QGroupBox
#QButtonGroup