from PySide6.QtCore import Qt
from sidebar_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton, QWidget
import sys
import json
from PySide6.QtWidgets import QMenu
import ssl
import requests
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea, QMessageBox, QStackedWidget
from PySide6.QtCore import Qt, QStringListModel, QObject, Signal
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea, QMessageBox, QStackedWidget, QGroupBox
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
import json
import requests
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
import webbrowser
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QGridLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
import requests
import ssl
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QScrollArea, QPushButton, QGridLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
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
from RecipeDetailsView import RecipeDetailsView

class RecipeController:
    def __init__(self, model, view, stacked_widget, str):
        self.ClassMere = str
        print(str)
        self.model = model
        self.view = view
        self.stacked_widget = stacked_widget
        self.view.recipeClicked.connect(self.show_recipe_details)
        

    def show_recipe_details(self, idx, ClassMere):
        try:
            recipe = self.model.get_recipes()[idx]
            recipe_id = recipe['id']
           # recipeclass = self.model.get_recipes()[ClassMere]
           

            print(f"detaile de {recipe_id}")
            url = f"https://localhost:7271/api/Recipes/{recipe_id}"
            if ClassMere == "FavoritePage":
                url = f"https://localhost:7271/api/Recipes/{recipe['spoId']}"
            context = ssl._create_unverified_context()
            response = requests.get(url, verify=False)
            data = response.json()
            
            recipe_details = json.dumps(data, indent=4)
            image_url = recipe['image']  # Obtenir l'URL de l'image 
            print(ClassMere)
            details_view = RecipeDetailsView(recipe_details,self.model, image_url, self.stacked_widget, ClassMere, self.view)
            self.recipe_controller2 = RecipeController(self.model, details_view, self.stacked_widget, str)
            print(1)
            self.stacked_widget.addWidget(details_view)
            self.stacked_widget.setCurrentWidget(details_view)
        except Exception as e:
            print("Error fetching recipe details:", e)


