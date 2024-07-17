from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PySide6.QtCore import Qt
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt
import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt
import requests
import ssl
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QLabel,
    QLineEdit, QPushButton, QVBoxLayout, QWidget)


DEFAULT_NAME = "User name"
DEFAULT_EMAIL = "email@example.com"

class ProfilePage(QWidget):
    def __init__(self, model, stacked_widget):
        super().__init__()
        self.model = model
        self.stacked_widget = stacked_widget

        # Création des widgets
       # self.profile_image_label = QLabel()
      #  pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
       # self.profile_image_label.setPixmap(QPixmap("C:/Users/eliao/OneDrive/Bureau/OOPython/image/eliaou_madar.png"))  # Remplacez par le chemin de votre image
        self.profile_image_label = QPushButton("")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/eliaou_madar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_image_label.setIcon(icon1)
        self.profile_image_label.setIconSize(QSize(200, 200))
        self.profile_image_label.setStyleSheet(" border:none; border-radius:15px;")


        self.name_label = QLabel(DEFAULT_NAME)
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet("background-color: white; border-radius:15px; border: 1px solid rgb(4, 125, 90); height: 30px;")
        self.name_edit.setText(DEFAULT_NAME)  # Mettez le nom actuel de l'utilisateur ici
        self.name_edit.setVisible(False)  # Rendre la QLineEdit invisible par défaut
        self.email_edit = QLineEdit() 
        self.email_edit.setStyleSheet("background-color: white; border-radius:15px; border: 1px solid rgb(4, 125, 90); height: 30px;")
        self.email_label = QLabel(DEFAULT_EMAIL)
        self.email_edit.setText(DEFAULT_EMAIL)  # Mettez le nom actuel de l'utilisateur ici
        self.email_edit.setVisible(False)  # Rendre la QLineEdit invisible par défaut
        # Mettez l'email de l'utilisateur ici
        self.save_button = QPushButton("Validate")
        #self.save_button.setStyleSheet("background-color: green; color: white; border:none; border-radius:10px; max-width: 150px; height: 30px; font-weight:bold;")
        self.save_button.setVisible(False)  # Rendre le QPushButton invisible par défaut
        self.save_button.clicked.connect(self.save_profile_changes)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.toggle_edit_mode)

        style = """
QPushButton {
    background-color: rgb(250, 244, 228);
    color: rgb(4, 125, 90);
    border: 2px solid rgb(4, 125, 90);
    border-radius: 10px;
    min-width: 150px;
    height: 30px;
    font-weight:bold;
}
QPushButton:checked {
    background-color: rgb(4, 125, 90);
    color: rgb(250, 244, 228);
    border: 2px solid rgb(250, 244, 228);
    font-weight:bold;
}
"""

        self.edit_button.setStyleSheet(style)
        self.save_button.setStyleSheet(style)

        # Style des widgets
        #self.edit_button.setStyleSheet("background-color: blue; color: white; border:none; border-radius:10px; max-width: 150px; height: 30px; font-weight:bold;")

        # Création des layouts
        profile_layout = QVBoxLayout()
        profile_layout.addWidget(self.profile_image_label, alignment=Qt.AlignCenter)
        profile_layout.addWidget(self.name_label, alignment=Qt.AlignCenter)
        profile_layout.addWidget(self.name_edit)
        profile_layout.addWidget(self.email_label, alignment=Qt.AlignCenter)
        profile_layout.addWidget(self.email_edit)
        profile_layout.addWidget(self.save_button, alignment=Qt.AlignCenter)
        profile_layout.addWidget(self.edit_button, alignment=Qt.AlignCenter)

        self.scroll_area = QScrollArea()
        self.scroll_content = QWidget()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("border: none;")
        self.scroll_area.setWidget(self.scroll_content)

        main_layout = QVBoxLayout()
        main_layout.addLayout(profile_layout)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def toggle_edit_mode(self):
        # Rendre la QLineEdit, QLabel et QPushButton visibles lorsqu'on clique sur le bouton "Editer"
        self.name_edit.setVisible(True)
        self.email_edit.setVisible(True)
        self.email_label.setVisible(True)
        self.save_button.setVisible(True)
        self.edit_button.setVisible(False)

    def save_profile_changes(self):

        global DEFAULT_NAME
        new_name = self.name_edit.text()
        DEFAULT_NAME = new_name

        global DEFAULT_EMAIL
        new_email = self.email_edit.text()
        DEFAULT_EMAIL = new_email
        # Mettez ici la logique pour sauvegarder le nouveau nom dans votre modèle
        print("Nom modifié :", new_name)
        self.name_label.setText(new_name)
        self.email_label.setText(new_email)
        self.name_edit.setVisible(False)
        self.email_edit.setVisible(False)
        self.email_label.setVisible(True)
        self.save_button.setVisible(False)
        self.edit_button.setVisible(True)