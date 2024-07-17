
from PySide6.QtWidgets import QPushButton, QWidget
import ssl
import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea
from PySide6.QtCore import Qt, Signal
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QPushButton, QLabel
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QGridLayout, QLabel, QLineEdit
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QScrollArea, QPushButton, QGridLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QIcon,
    QPixmap)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QVBoxLayout, QWidget)



class RecipeView(QWidget):

    recipeClicked = Signal(int, str)

    def __init__(self, model, stacked_widget):
        super().__init__()
        self.model = model
        self.stacked_widget = stacked_widget

        self.setStyleSheet("background-color: rgb(250, 244, 228);")

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("border: none;")

        

        self.add_button_renew = QPushButton("Show new recipes")
        self.add_button_renew.setObjectName(u"Show new recipes")
        self.add_button_renew.clicked.connect(self.fetch_recipes)
        style = """
QPushButton {
    background-color: rgb(250, 244, 228);
    color: rgb(4, 125, 90);
    border: 2px solid rgb(4, 125, 90);
    border-radius: 10px;
    max-width: 150px;
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

        self.add_button_renew.setStyleSheet(style)

      #  self.button_layout = QHBoxLayout()
     #   self.button_layout.setAlignment(Qt.AlignHCenter)

# Ajouter le bouton au layout horizontal
     #   self.button_layout.addWidget(self.add_button_renew)

# Appliquer le layout horizontal au widget parent
       # self.setLayout(self.button_layout)


# Appliquer le layout horizontal au widget parent
         
        #self.menu = QMenu()
        #self.menu.addAction("My Favorite Recipe", self.my_favorite_recipe)

        # Ajouter une barre de recherche
        self.search_bar = QLineEdit()       
        self.search_bar.setPlaceholderText("Search a recipe...")
        self.search_bar.returnPressed.connect(self.search_recipes)
        self.search_bar.setStyleSheet("background-color: white; border-radius:10px; border: 1px solid rgb(4, 125, 90); height: 30px;")

        self.pushButton_14 = QPushButton()
        icon7 = QIcon()
        icon7.addFile(u":/image/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setStyleSheet("background-color: white;")

        self.pushButton_14.clicked.connect(self.search_recipes)

       # self.image_label = QLabel()
       # self.image_label.setPixmap(QPixmap(":/image/recetteimage.png"))  # Remplacez "your_image.png" par le chemin de votre image
       

        self.layout = QGridLayout(self.scroll_content)
        self.layout.setSpacing(30)
        self.init_ui()

    def init_ui(self):
    # Créer un layout horizontal pour le bouton "Profile" et la barre de recherche
        search_layout = QHBoxLayout()
       # search_layout.addWidget(self.add_button_profile)  # Ajouter le bouton "Profile" ici
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.pushButton_14)
        #search_layout.addWidget(self.image_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout) # Ajouter le layout horizontal contenant la barre de recherche et le bouton "Profile"
        main_layout.addWidget(self.scroll_area)
        #main_layout.addWidget(self.add_button_renew)  # Ajouter le bouton "Renew Recipe" en bas
        self.setLayout(main_layout)

    def fetch_recipes(self):
        try: 

            for i in reversed(range(self.layout.count())):
                layout_item = self.layout.itemAt(i)
                if layout_item.widget() is not None:
                    widget = layout_item.widget()
                    widget.setVisible(False)
                    if widget.objectName() == "Show new recipes":
                          widget.setVisible(True)


            ClassMere = type(self).__name__
            print(ClassMere)
            url = "https://localhost:7271/api/Recipes/Random_Recipes?s=6"
            context = ssl._create_unverified_context()
            response = requests.get(url, verify=False)
            data = response.json()

        # Update model with fetched recipes
            self.model.set_recipes(data)
    
        # Populate layout with fetched recipes
            row = 0
            col = 0
            for index, recipe in enumerate(data):
                title = recipe['title']
                image_url = recipe['image']
                time = recipe['readyInMinutes']
                

            # Fetch image data and resize
                image_data = requests.get(image_url).content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Create labels for image and title
                recipe_image_label = QLabel()
                recipe_image_label.setPixmap(pixmap)
                recipe_image_label.mousePressEvent = lambda event, idx=index: self.recipeClicked.emit(idx, ClassMere)

                recipe_title_label = QLabel(title)
                recipe_title_label.setWordWrap(True)
                recipe_title_label.setAlignment(Qt.AlignCenter)

            # Create a vertical box layout for the recipe
                recipe_box = QVBoxLayout()
                recipe_box2 = QHBoxLayout()
                

            # Create a container widget for the recipe box
                recipe_container = QWidget()
                recipe_container2 = QWidget()
                recipe_container.setMaximumSize(300, 300)
                recipe_container2.setMinimumSize(100, 100)

            # Définir le style de fond de la boîte de recette
                recipe_container.setStyleSheet("background-color: white; border-radius: 20px;")

            # Ajouter l'image et le titre à la boîte
                recipe_box.addWidget(recipe_image_label)
                recipe_box.addWidget(recipe_title_label)

            # Set layout for the container widget
                

            # Create "Add to Favorite Recipe" and "View Details" buttons
                button_layout = QVBoxLayout()
                button_layout2 = QHBoxLayout()

# Create "Add to Favorite Recipe" button
                icon8 = QIcon()
                icon8.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/etoile-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
                icon8.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/etoile2-removebg-preview.png", QSize(), QIcon.Normal, QIcon.On)
                delete_button = QPushButton("  Add to Favorite Recipe")#
                delete_button.setStyleSheet(" color: black; border:none; border-radius:10px; max-width: 200px; height: 40px; font-weight:bold;")
                delete_button.setIcon(icon8)
                delete_button.setIconSize(QSize(23, 23))               
                delete_button.setCheckable(True)
                delete_button.setAutoExclusive(True)

# Create "View Details" button
              #  view_button = QPushButton("View Details")
              #  view_button.setStyleSheet("background-color: rgb(31, 149, 239); color: white; border:none; border-radius:10px; max-width: 150px; height: 30px; font-weight:bold;")
            
                time_button = QPushButton("                   ")
                icon1 = QIcon()
                icon1.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/time2.png", QSize(), QIcon.Normal, QIcon.Off)
                time_button.setIcon(icon1)
                time_button.setIconSize(QSize(55, 55))

# Création du deuxième bouton 
                time_with_unit = f"{time} min"
                time_with_unit = f"{time} min"
                print(time_with_unit)


                time_button2 = QPushButton(f" {time_with_unit}")
                icon2 = QIcon()
                icon2.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/time-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
                time_button2.setIcon(icon2)
                time_button2.setIconSize(QSize(35, 35))
   
               

# Créer le QLabel avec le temps et l'unité
                

                recipe_box2.addWidget(time_button)
                recipe_box2.addWidget(time_button2)

               # recipe_time = QLabel(time_with_unit)
              #  recipe_box2.addWidget(recipe_time)




# Connect signals for buttons
                delete_button.clicked.connect(self.AddFavoriteRecipe(index))
                #view_button.clicked.connect(lambda _, idx=index: self.view_details(idx))

# Add buttons to the button layout
                button_layout.addWidget(delete_button)
                button_layout2.addWidget(time_button)
                button_layout2.addWidget(time_button2)
                #button_layout.addWidget(view_button)
                button_layout.setAlignment(Qt.AlignCenter)  # Align buttons to the center horizontally
                button_layout2.setAlignment(Qt.AlignCenter)

                

# Add the button layout to the recipe box layout
                
                recipe_box.addLayout(button_layout2)
                recipe_box.addLayout(button_layout)
                #recipe_box.addSpacing(300)
                
                recipe_container.setLayout(recipe_box)
              #  recipe_container.setLayout(recipe_box2)

            # Add space between each recipe box
                

            # Add recipe container to the grid layout
                self.layout.addWidget(recipe_container, row, col)

                col += 1
                if col == 3:
                    col = 0
                    row += 1

        # Add "Renew" button to layout
            self.layout.addWidget(self.add_button_renew, row+2, 1)

        except Exception as e:
            print("Error fetching recipes:", e)

    def AddFavoriteRecipe(self, index):
        def add_recipe():
            self.AddFavoriteRecipe2(index)
        return add_recipe        

    def AddFavoriteRecipe2(self, idx):
        try:
            recipe = self.model.get_recipes()[idx]
            recipe_id = recipe['id']
            url = f"https://localhost:7271/api/Recipes/Add/Id?id={recipe_id}"
            print(url)
            context = ssl._create_unverified_context()
            response = requests.post(url, verify=False)
            if response.status_code == 200:
                print("Recipe added to favorites successfully.")
            else:
                print("Failed to add recipe to favorites. Status code:", response.status_code)
        except Exception as e:
            print("Error adding recipe to favorites:", e)    


    @staticmethod
    def get_time(id):
        url = f"https://localhost:7271/api/Recipes/{id}"
        context = ssl._create_unverified_context()
        response = requests.get(url, verify=False)
        data = response.json()
        time1 = data.get("readyInMinutes")
        return time1     
      

    def search_recipes(self):
        try: 

            for i in reversed(range(self.layout.count())):
                layout_item = self.layout.itemAt(i)
                if layout_item.widget() is not None:
                    widget = layout_item.widget()
                    widget.setVisible(False)
                    if widget.objectName() == "Show new recipes":
                          widget.setVisible(True)


            search_query = self.search_bar.text()
            ClassMere = type(self).__name__
            print(ClassMere)
            url = f"https://localhost:7271/api/Recipes/RecipesByIngredient/query?s={search_query}"
            context = ssl._create_unverified_context()
            response = requests.get(url, verify=False)
            data = response.json()

        # Update model with fetched recipes
            self.model.set_recipes(data)

    
        # Populate layout with fetched recipes
            row = 0
            col = 0
            for index, recipe in enumerate(data):
                title = recipe['title']
                image_url = recipe['image']
                time = self.get_time(recipe['id'])

            # Fetch image data and resize
                image_data = requests.get(image_url).content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Create labels for image and title
                recipe_image_label = QLabel()
                recipe_image_label.setPixmap(pixmap)
                recipe_image_label.mousePressEvent = lambda event, idx=index: self.recipeClicked.emit(idx, ClassMere)

                recipe_title_label = QLabel(title)
                recipe_title_label.setWordWrap(True)
                recipe_title_label.setAlignment(Qt.AlignCenter)

            # Create a vertical box layout for the recipe
                recipe_box = QVBoxLayout()
                recipe_box2 = QHBoxLayout()
                

            # Create a container widget for the recipe box
                recipe_container = QWidget()
                recipe_container2 = QWidget()
                recipe_container.setMaximumSize(300, 300)
                recipe_container2.setMinimumSize(100, 100)

            # Définir le style de fond de la boîte de recette
                recipe_container.setStyleSheet("background-color: white; border-radius: 20px;")

            # Ajouter l'image et le titre à la boîte
                recipe_box.addWidget(recipe_image_label)
                recipe_box.addWidget(recipe_title_label)

            # Set layout for the container widget
                

            # Create "Add to Favorite Recipe" and "View Details" buttons
                button_layout = QVBoxLayout()
                button_layout2 = QHBoxLayout()

# Create "Add to Favorite Recipe" button
                icon8 = QIcon()
                icon8.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/etoile-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
                icon8.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/etoile2-removebg-preview.png", QSize(), QIcon.Normal, QIcon.On)
                delete_button = QPushButton("  Add to Favorite Recipe")#
                delete_button.setStyleSheet(" color: black; border:none; border-radius:10px; max-width: 200px; height: 40px; font-weight:bold;")
                delete_button.setIcon(icon8)
                delete_button.setIconSize(QSize(23, 23))               
                delete_button.setCheckable(True)
                delete_button.setAutoExclusive(True)

# Create "View Details" button
              #  view_button = QPushButton("View Details")
              #  view_button.setStyleSheet("background-color: rgb(31, 149, 239); color: white; border:none; border-radius:10px; max-width: 150px; height: 30px; font-weight:bold;")
            
                time_button = QPushButton("                   ")
                icon1 = QIcon()
                icon1.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/time2.png", QSize(), QIcon.Normal, QIcon.Off)
                time_button.setIcon(icon1)
                time_button.setIconSize(QSize(55, 55))

# Création du deuxième bouton 
                time_with_unit = f"{time} min"
                time_with_unit = f"{time} min"
                print(time_with_unit)


                time_button2 = QPushButton(f" {time_with_unit}")
                icon2 = QIcon()
                icon2.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/time-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
                time_button2.setIcon(icon2)
                time_button2.setIconSize(QSize(35, 35))
   
               

# Créer le QLabel avec le temps et l'unité
                

                recipe_box2.addWidget(time_button)
                recipe_box2.addWidget(time_button2)

               # recipe_time = QLabel(time_with_unit)
              #  recipe_box2.addWidget(recipe_time)




# Connect signals for buttons
                delete_button.clicked.connect(self.AddFavoriteRecipe(index))
                #view_button.clicked.connect(lambda _, idx=index: self.view_details(idx))

# Add buttons to the button layout
                button_layout.addWidget(delete_button)
                button_layout2.addWidget(time_button)
                button_layout2.addWidget(time_button2)
                #button_layout.addWidget(view_button)
                button_layout.setAlignment(Qt.AlignCenter)  # Align buttons to the center horizontally
                button_layout2.setAlignment(Qt.AlignCenter)

                

# Add the button layout to the recipe box layout
                
                recipe_box.addLayout(button_layout2)
                recipe_box.addLayout(button_layout)
                #recipe_box.addSpacing(300)
                
                recipe_container.setLayout(recipe_box)
              #  recipe_container.setLayout(recipe_box2)

            # Add space between each recipe box
                

            # Add recipe container to the grid layout
                self.layout.addWidget(recipe_container, row, col)

                col += 1
                if col == 3:
                    col = 0
                    row += 1

        # Add "Renew" button to layout
            self.layout.addWidget(self.add_button_renew, row+2, 1)

        except Exception as e:
            print("Error fetching recipes:", e)