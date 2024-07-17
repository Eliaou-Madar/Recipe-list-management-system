from sidebar_ui import Ui_MainWindow
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PySide6.QtWidgets import QMainWindow, QStackedWidget
import requests
import ssl
from PySide6.QtWidgets import (QMainWindow, QStackedWidget)
from RecipeModel import RecipeModel
from RecipeView import RecipeView
from FavoritePage import FavoritePage
from RecipeController import RecipeController
from ProfilePage import ProfilePage

i = 0
class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.recipe_view1 = None
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Kitchen AZ")
        self.message_1.click()
        self.message_2.click()
        self.switch_to_Favorite_RecipesPage()

        self.setStyleSheet("background-color: rgb(4, 125, 90);")  # exterieure

        self.dashboard_1.click()
        self.dashboard_2.click()
        self.switch_to_RecipesPage()
        
       # self.recipe_model = RecipeModel()
        #self.stacked_widget = QStackedWidget()
        #self.recipe_view = RecipeView(self.recipe_model, self.stacked_widget)
      #  self.recipe_controller = RecipeController(self.recipe_model, self.recipe_view, self.stacked_widget)
      #  self.stacked_widget.addWidget(self.recipe_view)

       # self.setCentralWidget(self.stacked_widget)
      #  self.recipe_view.fetch_recipes()  # Fetch recipes automatically on startup

        self.icon_name_widget.setHidden(True)
        
        self.dashboard_1.clicked.connect(self.switch_to_RecipesPage)
        self.dashboard_2.clicked.connect(self.switch_to_RecipesPage)

        self.profile_1.clicked.connect(self.switch_to_ProfilePage)
        self.profile_2.clicked.connect(self.switch_to_ProfilePage)

        self.message_1.clicked.connect(self.switch_to_Favorite_RecipesPage)
        self.message_2.clicked.connect(self.switch_to_Favorite_RecipesPage)
       

    def switch_to_RecipesPage(self):

        #self.stackedWidget.setCurrentIndex(5) 
        
        if self.recipe_view1 is None:
            self.recipe_model = RecipeModel()
            self.recipe_view1 = RecipeView(self.recipe_model, self.stackedWidget)
            self.recipe_controller1 = RecipeController(self.recipe_model, self.recipe_view1, self.stackedWidget, str)
            self.stackedWidget.addWidget(self.recipe_view1) #je lui dit cette page est la setCurrentIndex(5)
            self.stackedWidget.setStyleSheet("background-color: rgb(250, 244, 228);") # milieu
            self.recipe_view1.fetch_recipes()
            self.switch_to_RecipesPage()
        else:
            # Utiliser la valeur précédente de recipe_view
            self.stackedWidget.setCurrentWidget(self.recipe_view1)


    
    def switch_to_ProfilePage(self):
        self.recipe_model = RecipeModel()
        self.recipe_view = ProfilePage(self.recipe_model, self.stackedWidget)
        
        self.stackedWidget.addWidget(self.recipe_view)
        self.stackedWidget.setCurrentWidget(self.recipe_view)  
        

            
    def switch_to_Favorite_RecipesPage(self):
        
        self.recipe_model = RecipeModel()
        
    # Créer une instance de la classe RecipeView en passant les arguments requis
        self.recipe_view = FavoritePage(self.recipe_model, self.stackedWidget)
        self.recipe_controller = RecipeController(self.recipe_model, self.recipe_view, self.stackedWidget, str)
        self.stackedWidget.addWidget(self.recipe_view)
        self.recipe_view.fetch_recipes1()
        self.stackedWidget.setCurrentWidget(self.recipe_view)  
        
    
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipe Manager")
        self.setFixedSize(800, 600)
        # Initialize model, view, and controller
        self.recipe_model = RecipeModel()
        self.stacked_widget = QStackedWidget()
        self.recipe_view = RecipeView(self.recipe_model, self.stacked_widget)
        self.recipe_controller = RecipeController(self.recipe_model, self.recipe_view, self.stacked_widget)
        print(type(self))
        self.stacked_widget.addWidget(self.recipe_view)

        self.setCentralWidget(self.stacked_widget)
        self.recipe_view.fetch_recipes()  # Fetch recipes automatically on startup