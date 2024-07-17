# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import requests
import ssl
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(0, 0))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(4, 125, 90);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"height:30px;\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(250, 244, 228);\n"
"color:rgb(4, 125, 90);\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"../../../Downloads/pngfind.com-user-icon-png-1760995.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/image/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/photo_2024-04-21_15-57-05-removebg-preview.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.profile_1 = QPushButton(self.icon_only_widget)
        self.profile_1.setObjectName(u"profile_1")
        icon1 = QIcon()
        icon1.addFile(u":/image/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/photo_2024-04-21_15-57-25-removebg-preview.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_1.setIcon(icon1)
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_1)

        self.message_1 = QPushButton(self.icon_only_widget)
        self.message_1.setObjectName(u"message_1")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/photo_2024-04-21_16-00-57-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/photo_2024-04-21_15-56-49-removebg-preview.png", QSize(), QIcon.Normal, QIcon.On)
        self.message_1.setIcon(icon2)
        self.message_1.setCheckable(True)
        self.message_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.message_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 273, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/image/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/image/log_out.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        self.icon_name_widget.setMinimumSize(QSize(175, 0))
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(4, 125, 90);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"text-align:left;\n"
"height:30px;\n"
"border:none;\n"
"padding-left:30px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(250, 244, 228);\n"
"color:rgb(4, 125, 90);\n"
"font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(25, 25))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u"../../../Downloads/pngfind.com-user-icon-png-1760995.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setIcon(icon1)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_2)

        self.message_2 = QPushButton(self.icon_name_widget)
        self.message_2.setObjectName(u"message_2")
        self.message_2.setIcon(icon2)
        self.message_2.setCheckable(True)
        self.message_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.message_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 273, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.icon_name_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.man_menu = QWidget(self.centralwidget)
        self.man_menu.setObjectName(u"man_menu")
        self.verticalLayout_5 = QVBoxLayout(self.man_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.man_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/image/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(211, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_20 = QLabel(self.header_widget)
        self.label_20.setText("Kitchen")
        self.label_20.setFont(QFont("Bold", 65))  # Remplacez "Arial" par la police souhaitée et 30 par la taille de police désirée
        self.label_20.setStyleSheet("font-family: larsseit-webfont, Helvetica, Arial, sans-serif; color: rgb(250, 244, 228) ; font-weight: bold;")
        self.label_20.setFont(font)   # Changer la taille du texte si nécessaire

        self.horizontalLayout.addWidget(self.label_20)
        self.horizontalLayout.addWidget(self.label_20)


        self.label_21 = QLabel(self.header_widget)
        self.label_21.setText("AZ")
        self.label_21.setFont(QFont("Bold", 65))  # Remplacez "Arial" par la police souhaitée et 30 par la taille de police désirée
        self.label_21.setStyleSheet("font-family: larsseit-webfont, Helvetica, Arial, sans-serif; color: #ED1818; font-weight: bold;")
        self.label_21.setFont(font)   # Changer la taille du texte si nécessaire

        self.horizontalLayout.addWidget(self.label_21)
        self.horizontalLayout.addWidget(self.label_21)

       # self.pushButton_14 = QPushButton(self.header_widget)
        #self.pushButton_14.setObjectName(u"pushButton_14")
        #icon7 = QIcon()
        #icon7.addFile(u":/image/search.png", QSize(), QIcon.Normal, QIcon.Off)
       # self.pushButton_14.setIcon(icon7)
        

        #self.horizontalLayout.addWidget(self.pushButton_14)

        self.horizontalSpacer_2 = QSpacerItem(211, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/image/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)

        self.horizontalLayout.addWidget(self.pushButton_15)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.man_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_4 = QLabel(self.dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 130, 181, 131))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 240, 181, 131))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.page_3)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.label_5 = QLabel(self.messages_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 210, 181, 131))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.messages_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.man_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.message_1.toggled.connect(self.message_2.setChecked)
        self.profile_1.toggled.connect(self.profile_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.message_2.toggled.connect(self.message_1.setChecked)
        self.profile_2.toggled.connect(self.profile_1.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.profile_1.setText("")
        self.message_1.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"   User", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Recipes", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.message_2.setText(QCoreApplication.translate("MainWindow", u"Favorite Recipes", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.menu.setText("")
        #self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DashBoardPage", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"", None))

    def search_recipes(self):
        try:
            search_query = self.lineEdit.text()
            url = f"https://localhost:7271/api/Recipes/RecipesByIngredient/query?s={search_query}"
            context = ssl._create_unverified_context()
            response = requests.get(url, verify=False)
            data = response.json()

            # Update model with fetched recipes
            self.model.set_recipes(data)

            # Clear previous items from layout
            for i in reversed(range(self.layout.count())):
                self.layout.itemAt(i).widget().setParent(None)

            # Populate layout with fetched recipes
            row = 0
            col = 0
            for index, recipe in enumerate(data):
                title = recipe['title']
                image_url = recipe['image']

                # Ajouter l'image à l'affichage et redimensionner
                image_data = requests.get(image_url).content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                recipe_image_label = QLabel()
                recipe_image_label.setPixmap(pixmap)
                recipe_title_label = QLabel(title)
                recipe_image_label.setStyleSheet("border-radius: 10px;")

                # Connect the image click signal
                recipe_image_label.mousePressEvent = lambda event, idx=index: self.recipeClicked.emit(idx)

                self.layout.addWidget(recipe_image_label, row, col)
                self.layout.addWidget(recipe_title_label, row+1, col)

                col += 1
                if col == 3:
                    col = 0
                    row += 2

        except Exception as e:
            print("Error fetching recipes:", e)
