# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(487, 265)
        icon = QIcon()
        icon.addFile(u":/app/5.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.image_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.base1_label = QLineEdit(self.centralwidget)
        self.base1_label.setObjectName(u"base1_label")

        self.verticalLayout.addWidget(self.base1_label)

        self.base2_label = QLineEdit(self.centralwidget)
        self.base2_label.setObjectName(u"base2_label")

        self.verticalLayout.addWidget(self.base2_label)

        self.height_label = QLineEdit(self.centralwidget)
        self.height_label.setObjectName(u"height_label")

        self.verticalLayout.addWidget(self.height_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.solve_btn = QPushButton(self.centralwidget)
        self.solve_btn.setObjectName(u"solve_btn")

        self.verticalLayout.addWidget(self.solve_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OGE Helper", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041e\u0413\u042d \u043f\u043e \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0435. \u0422\u0435\u043c\u0430 17.05 \u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u0447\u0435\u0442\u044b\u0440\u0435\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u0432</span></p></body></html>", None))
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/app/t.svg\"/></p></body></html>", None))
        self.base1_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438", None))
        self.base2_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438", None))
        self.height_label.setText("")
        self.height_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438", None))
        self.solve_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0438\u0442\u044c", None))
    # retranslateUi

