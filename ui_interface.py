# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceIiHsJc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(651, 695)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_label = QLabel(self.frame_5)
        self.page_label.setObjectName(u"page_label")

        self.horizontalLayout_3.addWidget(self.page_label)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.header_frame = QFrame(self.frame)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.header_frame)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_4)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_4)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_4)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.WinPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.WinPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_19)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.WinPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_16)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.WinPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_14)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_14)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.WinPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_11)
        self.label_18.setObjectName(u"label_18")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_18)

        self.comPortCombo = QComboBox(self.frame_11)
        self.comPortCombo.setObjectName(u"comPortCombo")

        self.horizontalLayout_13.addWidget(self.comPortCombo)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_14)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.WinPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_17)

        self.selectedComPortLabel = QLabel(self.frame_10)
        self.selectedComPortLabel.setObjectName(u"selectedComPortLabel")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.selectedComPortLabel.setFont(font2)
        self.selectedComPortLabel.setFrameShape(QFrame.StyledPanel)
        self.selectedComPortLabel.setFrameShadow(QFrame.Sunken)
        self.selectedComPortLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.selectedComPortLabel)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.horizontalLayout_15.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_16)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.WinPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_13)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.WinPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.comOpenBtn = QPushButton(self.frame_12)
        self.comOpenBtn.setObjectName(u"comOpenBtn")
        self.comOpenBtn.setFont(font1)

        self.horizontalLayout_14.addWidget(self.comOpenBtn)

        self.comCloseBtn = QPushButton(self.frame_12)
        self.comCloseBtn.setObjectName(u"comCloseBtn")
        self.comCloseBtn.setFont(font1)

        self.horizontalLayout_14.addWidget(self.comCloseBtn)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.refreshComBtn = QPushButton(self.frame_13)
        self.refreshComBtn.setObjectName(u"refreshComBtn")
        self.refreshComBtn.setFont(font1)

        self.verticalLayout_4.addWidget(self.refreshComBtn)


        self.horizontalLayout_15.addWidget(self.frame_13)


        self.verticalLayout_6.addWidget(self.frame_16)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.WinPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_17)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_20)

        self.frame_8 = QFrame(self.frame_17)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.WinPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_8)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(312, 0))
        self.frame_3.setMaximumSize(QSize(312, 16777215))
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_button = QPushButton(self.frame_3)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout_2.addWidget(self.start_button)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.interrupt_button = QPushButton(self.frame_18)
        self.interrupt_button.setObjectName(u"interrupt_button")

        self.horizontalLayout_20.addWidget(self.interrupt_button)

        self.move_on_button = QPushButton(self.frame_18)
        self.move_on_button.setObjectName(u"move_on_button")

        self.horizontalLayout_20.addWidget(self.move_on_button)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.stop_button = QPushButton(self.frame_3)
        self.stop_button.setObjectName(u"stop_button")

        self.verticalLayout_2.addWidget(self.stop_button)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.WinPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.status_button = QPushButton(self.frame_6)
        self.status_button.setObjectName(u"status_button")

        self.horizontalLayout_5.addWidget(self.status_button)

        self.status_label = QLabel(self.frame_6)
        self.status_label.setObjectName(u"status_label")
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.status_label.setFont(font3)
        self.status_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.status_label, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_19.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.WinPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setUnderline(True)
        self.label_2.setFont(font4)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background-color:  rgb(255, 0, 0);\n"
"color: rgb(255, 0, 0);")

        self.horizontalLayout_7.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_7.addWidget(self.label_31, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.red_counter = QLabel(self.frame_7)
        self.red_counter.setObjectName(u"red_counter")
        sizePolicy.setHeightForWidth(self.red_counter.sizePolicy().hasHeightForWidth())
        self.red_counter.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.red_counter.setFont(font5)

        self.horizontalLayout_7.addWidget(self.red_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 170, 0);")

        self.horizontalLayout_9.addWidget(self.label_9, 0, Qt.AlignLeft)

        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_9.addWidget(self.label_32)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.orange_counter = QLabel(self.frame_7)
        self.orange_counter.setObjectName(u"orange_counter")
        sizePolicy.setHeightForWidth(self.orange_counter.sizePolicy().hasHeightForWidth())
        self.orange_counter.setSizePolicy(sizePolicy)
        self.orange_counter.setFont(font5)

        self.horizontalLayout_9.addWidget(self.orange_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 255, 0);")

        self.horizontalLayout_10.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_10.addWidget(self.label_33)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.yellow_counter = QLabel(self.frame_7)
        self.yellow_counter.setObjectName(u"yellow_counter")
        sizePolicy.setHeightForWidth(self.yellow_counter.sizePolicy().hasHeightForWidth())
        self.yellow_counter.setSizePolicy(sizePolicy)
        self.yellow_counter.setFont(font5)

        self.horizontalLayout_10.addWidget(self.yellow_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);")

        self.horizontalLayout_11.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_11.addWidget(self.label_34)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.green_counter = QLabel(self.frame_7)
        self.green_counter.setObjectName(u"green_counter")
        sizePolicy.setHeightForWidth(self.green_counter.sizePolicy().hasHeightForWidth())
        self.green_counter.setSizePolicy(sizePolicy)
        self.green_counter.setFont(font5)

        self.horizontalLayout_11.addWidget(self.green_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"color: rgb(255, 0, 255);")

        self.horizontalLayout_12.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_12.addWidget(self.label_35)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.blue_counter = QLabel(self.frame_7)
        self.blue_counter.setObjectName(u"blue_counter")
        sizePolicy.setHeightForWidth(self.blue_counter.sizePolicy().hasHeightForWidth())
        self.blue_counter.setSizePolicy(sizePolicy)
        self.blue_counter.setFont(font5)

        self.horizontalLayout_12.addWidget(self.blue_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAutoFillBackground(False)
        self.label_23.setStyleSheet(u"background-color: rgb(155, 75, 0);\n"
"color:rgb(155, 75, 0);\n"
"")

        self.horizontalLayout_16.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_16.addWidget(self.label_36)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.gray_counter = QLabel(self.frame_7)
        self.gray_counter.setObjectName(u"gray_counter")
        sizePolicy.setHeightForWidth(self.gray_counter.sizePolicy().hasHeightForWidth())
        self.gray_counter.setSizePolicy(sizePolicy)
        self.gray_counter.setFont(font5)

        self.horizontalLayout_16.addWidget(self.gray_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"color: rgb(170, 0, 255);\n"
"")

        self.horizontalLayout_17.addWidget(self.label_25, 0, Qt.AlignLeft)

        self.label_37 = QLabel(self.frame_7)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_17.addWidget(self.label_37)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.purple_counter = QLabel(self.frame_7)
        self.purple_counter.setObjectName(u"purple_counter")
        sizePolicy.setHeightForWidth(self.purple_counter.sizePolicy().hasHeightForWidth())
        self.purple_counter.setSizePolicy(sizePolicy)
        self.purple_counter.setFont(font5)

        self.horizontalLayout_17.addWidget(self.purple_counter, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_19.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_8.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"M&M SORTER SYSTEM", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"COM PORT CONFIGURATION FOR ARDUINO", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Choose COM Port:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Selected COM Port:", None))
        self.selectedComPortLabel.setText("")
        self.comOpenBtn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.comCloseBtn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.refreshComBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh\n"
"COM PORT List", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"SYSTEM CONFIGURATION", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.interrupt_button.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.move_on_button.setText(QCoreApplication.translate("MainWindow", u"MOVE ON", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.status_button.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"EMPTY", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"STATISTICS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\"> RED       :</span></p></body></html>", None))
        self.red_counter.setText(QCoreApplication.translate("MainWindow", u"      0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">  ORANGE :</span></p></body></html>", None))
        self.orange_counter.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">  YELLOW  :</span></p></body></html>", None))
        self.yellow_counter.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">  GREEN    :</span></p></body></html>", None))
        self.green_counter.setText(QCoreApplication.translate("MainWindow", u"   0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">  PINK       :</span></p></body></html>", None))
        self.blue_counter.setText(QCoreApplication.translate("MainWindow", u"     0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">  BROWN     :</span></p></body></html>", None))
        self.gray_counter.setText(QCoreApplication.translate("MainWindow", u"  0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">  PURPLE   :</span></p></body></html>", None))
        self.purple_counter.setText(QCoreApplication.translate("MainWindow", u"  0", None))
    # retranslateUi

