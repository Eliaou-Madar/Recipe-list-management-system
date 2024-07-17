from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PySide6.QtCore import Qt, Signal
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QPushButton, QLabel
import json
import webbrowser
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel
import requests
import ssl
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QScrollArea, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QFont, QIcon,
    QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QLabel,
    QPushButton, QVBoxLayout, QWidget)
from RecipeModel import RecipeModel
import RecipeController
import RecipeView
import FavoritePage


y = 1
class RecipeDetailsView(QWidget):

    recipeClicked = Signal(int, str)

    def __init__(self, recipe_details, model, image_url, stacked_widget, ClassMere, view):
        super().__init__()
        self.recipe_view = None

        if ClassMere == "RecipeView":
            print("ici")
            self.recipe_view2 =  view

        self.setStyleSheet("border: none;")
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)  # Ici, self.scroll_layout est configuré correctement
        self.classmer = ClassMere
        
        self.model = model
        self.stacked_widget = stacked_widget
        self.id_list = []

        # Créer une zone de défilement verticale
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.scroll_content)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        recipe_details_dict = json.loads(recipe_details)  # Parse JSON string into a dictionary
        self.id = recipe_details_dict.get("id", 0)
        self.title = recipe_details_dict.get("title", "")
        print(self.title)
        self.servings = recipe_details_dict.get("servings", 0)
        self.ready_in_minutes = recipe_details_dict.get("readyInMinutes", 0)
        self.source_name = recipe_details_dict.get("sourceName", "")
        self.source_url = recipe_details_dict.get("sourceUrl", "")
        self.health_score = recipe_details_dict.get("healthScore", 0)
        self.price_per_serving = recipe_details_dict.get("pricePerServing", 0) / 100  # Décalage de deux crans vers la gauche
        self.price_per_serving = "{:.1f}".format(self.price_per_serving)
        self.dairy_free = recipe_details_dict.get("dairyFree", False)
        self.gluten_free = recipe_details_dict.get("glutenFree", False)
        if self.dairy_free == True:
            self.dairy_free = "Yes"
        if self.dairy_free == False:
            self.dairy_free = "No"
        if self.gluten_free == True:
            self.gluten_free = "Yes"
        if self.gluten_free == False:
            self.gluten_free = "No"    
        self.summary = recipe_details_dict.get("summary", "")
        self.image = recipe_details_dict.get("image", "")

        self.back_button = QPushButton("")
        self.back_button.clicked.connect(self.return_to_main_page)
        self.scroll_layout.addWidget(self.back_button, alignment=Qt.AlignLeft)  # Alignement à gauche
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/eliao/OneDrive/Bureau/OOPython/image/585e4695cb11b227491c3373.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(27, 27))

        # Ajouter l'image dans la vue
        image_data = requests.get(image_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        recipe_image_label = QLabel()
        recipe_image_label.setPixmap(pixmap)
        

        # Ajouter les détails de la recette
        title_font = QFont()

# Ajout des détails de la recette un par un avec leur style individuel
        title_label = QLabel(f"<span style='font-weight:bold;color:rgb(4, 125, 90);font-size:25px;'>{self.title}</span>")
        title_label.setWordWrap(True)
        title_label.setTextFormat(Qt.RichText)  # Définir le format du texte en HTML
        title_label.setFont(title_font)
        self.scroll_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        self.scroll_layout.addSpacing(40)
        self.scroll_layout.addWidget(recipe_image_label, alignment=Qt.AlignCenter)
        self.scroll_layout.addSpacing(40)

# Servings
        servings_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Servings: </span> " + f"<span style='font-size:15px;'>{str(self.servings)}</span>" + "<span style='font-size:15px;'> per</span>")
        servings_label.setTextFormat(Qt.RichText)  
        servings_label.setFont(title_font)
        self.scroll_layout.addWidget(servings_label)

# Ready in Minutes
        ready_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Ready in Minutes: </span> " + f"<span style='font-size:15px;'>{str(self.ready_in_minutes)}</span>" + "<span style='font-size:15px;'> min</span>")
        ready_label.setTextFormat(Qt.RichText)  
        ready_label.setFont(title_font)
        self.scroll_layout.addWidget(ready_label)

# Recipe proposed by
        proposed_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Recipe proposed by: </span> " + f"<span style='font-size:15px;'>{self.source_name}</span>")
        proposed_label.setTextFormat(Qt.RichText)  
        proposed_label.setFont(title_font)
        self.scroll_layout.addWidget(proposed_label)

# Health Score
        health_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Health Score: </span> " + f"<span style='font-size:15px;'>{str(self.health_score)}</span>")
        health_label.setTextFormat(Qt.RichText)  
        health_label.setFont(title_font)
        self.scroll_layout.addWidget(health_label)

# Price per Serving
        price_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Price per Serving: </span> " + f"<span style='font-size:15px;'>{str(self.price_per_serving)}</span>" + "<span style='font-size:15px;'> $</span>")
        price_label.setTextFormat(Qt.RichText)  
        price_label.setFont(title_font)
        self.scroll_layout.addWidget(price_label)

# Dairy Free
        dairy_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Dairy Free: </span> " + f"<span style='font-size:15px;'>{str(self.dairy_free)}</span>")
        dairy_label.setTextFormat(Qt.RichText)  
        dairy_label.setFont(title_font)
        self.scroll_layout.addWidget(dairy_label)

# Gluten Free
        gluten_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Gluten Free: </span> " + f"<span style='font-size:15px;'>{str(self.gluten_free)}</span>")
        gluten_label.setTextFormat(Qt.RichText)  
        gluten_label.setFont(title_font)
        self.scroll_layout.addWidget(gluten_label)

# Summary
        summary_label = QLabel("<span style='font-weight:bold;text-decoration:underline;color:rgb(4, 125, 90);font-size:15px;'>Summary: </span>")
        summary_label.setTextFormat(Qt.RichText)  
        summary_label.setFont(title_font)
        self.scroll_layout.addWidget(summary_label)

        summary_text = QLabel(f"<span style='font-size:15px;'>{self.summary}</span>")
        summary_text.setWordWrap(True)  # Permettre le retour à la ligne en fonction de la taille de l'écran
        self.scroll_layout.addWidget(summary_text)

        self.scroll_layout.addSpacing(20)

        # Ajouter le bouton "Parcourir" pour ouvrir l'URL dans le navigateur
        browse_button = QPushButton(" See the recipe details on our web site ")
        browse_button.clicked.connect(self.open_in_browser)
        self.scroll_layout.addWidget(browse_button, alignment=Qt.AlignCenter)
        style = """
QPushButton {
    background-color: rgb(250, 244, 228);
    color: rgb(4, 125, 90);
    border: 2px solid rgb(4, 125, 90);
    border-radius: 10px;
    min-width: 300px;
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

        browse_button.setStyleSheet(style)

        self.scroll_layout.addSpacing(10)

        # Ajouter le bouton "Show Similar Recipe" pour afficher les recettes similaires
        show_similar_button = QPushButton(" Show Similar Recipe ")
        show_similar_button.clicked.connect(self.show_similar_recipe)
        self.scroll_layout.addWidget(show_similar_button, alignment=Qt.AlignCenter)
        show_similar_button.setStyleSheet(style)

        self.scroll_layout.addSpacing(20)
        
        #recipe_image_label.mousePressEvent = lambda event, idx=index: self.recipeClicked.emit(idx)
   
        scroll_area.setWidget(self.scroll_content)

        # Créer un layout pour la fenêtre principale
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def return_to_main_page(self):
      print(self.classmer)
      print(self.stacked_widget.currentIndex())
      if(self.classmer == "RecipeView"):
        self.stacked_widget.setCurrentIndex(4)    # peut etre faire aussi pour lui un 
        self.switch_to_RecipesPage()
        print("RecipeView ok")

      if(self.classmer == "FavoritePage"):
        self.stacked_widget.setCurrentIndex(5)
        self.switch_to_Favorite_RecipesPage()
        print("FavoritePage ok")

      if(self.classmer == "RecipeDetailsView"):
        global y
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - y) # a verifier ici
        y = y + 1
        print("RecipeDetailsView ok")


    def switch_to_RecipesPage(self):

        #self.stackedWidget.setCurrentIndex(5) 
        
        if self.recipe_view2 is None:
            self.recipe_model = RecipeModel()
            self.recipe_view2 = RecipeView.RecipeView(self.recipe_model, self.stacked_widget)
            self.recipe_controller1 = RecipeController.RecipeController(self.recipe_model, self.recipe_view2, self.stacked_widget, str)
            self.stacked_widget.addWidget(self.recipe_view2) #je lui dit cette page est la setCurrentIndex(5)
            self.recipe_view2.fetch_recipes()
            self.switch_to_RecipesPage()
        else:
            # Utiliser la valeur précédente de recipe_view
            self.stacked_widget.setCurrentWidget(self.recipe_view2)
            print("not none")
            #print(self.recipe_view2)

    
    def switch_to_Favorite_RecipesPage(self):
        self.recipe_model = RecipeModel()
        
    # Créer une instance de la classe RecipeView en passant les arguments requis
        self.recipe_view = FavoritePage.FavoritePage(self.recipe_model, self.stacked_widget)
        self.recipe_controller = RecipeController.RecipeController(self.recipe_model, self.recipe_view, self.stacked_widget, str)
        self.stacked_widget.addWidget(self.recipe_view)
        self.recipe_view.fetch_recipes1()
        self.stacked_widget.setCurrentWidget(self.recipe_view) 


    def open_in_browser(self):
        # Ouvrir l'URL dans le navigateur
        webbrowser.open_new_tab(self.source_url)

    def show_similar_recipe(self):
        self.fetch_data()  # Appel de fetch_data avec des parenthèses
        ids = self.get_ids()
        print(self.id,"IDs récupérés:", ids)
        self.add_recipe_details()
       

    def fetch_data(self):
        self.id_list = []
        url = f"https://localhost:7271/api/Recipes/Similar?id={self.id}"
        context = ssl._create_unverified_context()
        response = requests.get(url, verify=False)
        data = response.json()
        self.parse_data(data)

    def parse_data(self, data):
        self.id_list.clear()
        for item in data:
            recipe_id = item.get("id")
            if recipe_id:
                self.id_list.append(recipe_id)

    def get_ids(self):
        return self.id_list 
    
    def add_recipe_details(self):
        self.tab = []
        for index, recipe_id in enumerate(self.get_ids()):
            url = f"https://localhost:7271/api/Recipes/{recipe_id}"
            context = ssl._create_unverified_context()
            response = requests.get(url, verify=False)
            data = response.json()
        
        # Ajouter recipe_id à la liste self.tab
            self.tab.append(recipe_id)

        # Update model with fetched recipes
            self.model.set_recipes(data)

        # Populate layout with fetched recipes
            row = 0
            col = 0
            image_url = data.get("image")
            title = data.get("title")

        # Load recipe image
            image_data = requests.get(image_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            recipe_image_label = QLabel()
            recipe_image_label.setPixmap(pixmap)
            recipe_image_label.setStyleSheet("border-radius: 10px;")

        # Emit signal when recipe image is clicked
            recipe_image_label.mousePressEvent = lambda event, idx=index: self.recipeClicked.emit(idx, self.classmer)

            recipe_title_label = QLabel(title)
            recipe_title_label.setAlignment(Qt.AlignCenter)
            recipe_title_label.setStyleSheet("font-size:15px;")

        # Create a vertical box layout to contain image, text, and buttons
            hbox = QHBoxLayout()
            hbox.addWidget(recipe_image_label)
            hbox.addWidget(recipe_title_label)

        # Create a widget to contain the horizontal layout
            recipe_widget = QWidget()
            recipe_widget.setLayout(hbox)

        # Add widget to the scroll layout
            self.scroll_layout.addWidget(recipe_widget)

        # Add buttons "Delete Favorite Recipe" and "View Details"
            view_button = QPushButton("  View Details")
            view_button.clicked.connect(self.show_recipe_details2(index,image_url,title, self.classmer))
            
            style = """
QPushButton {
    background-color: rgb(250, 244, 228);
    color: rgb(4, 125, 90);
    border: 2px solid rgb(4, 125, 90);
    border-radius: 10px;
    min-width: 300px;
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

            view_button.setStyleSheet(style)
            self.scroll_layout.addWidget(view_button, alignment=Qt.AlignLeft)
        


    def show_recipe_details2(self, index,image_url,title, classmer):
        def delete_recipe():
            self.show_recipe_details3(index,image_url,title, classmer)
        return delete_recipe        

    def show_recipe_details3(self, index, image_url, title, classm):
        print(index)
        print(self.tab[index])
        print(image_url)
        print(title)
        print(classm)
        recipe_id = self.tab[index]
        # Créer RecipeDetailsView directement avec les détails de la recette
        url = f"https://localhost:7271/api/Recipes/{recipe_id}"
        context = ssl._create_unverified_context()
        response = requests.get(url, verify=False)
        data = response.json()

        recipe_details = json.dumps(data, indent=4) 
        recipe_view = RecipeDetailsView(recipe_details, self.model, image_url, self.stacked_widget, "RecipeDetailsView", self.recipe_view )  # Utiliser self.stacked_widget

    # Remplacer le contenu actuel par le nouveau contenu
        self.stacked_widget.addWidget(recipe_view)
        self.stacked_widget.setCurrentWidget(recipe_view)
        self.tab = []
        

def dict_to_json_string(dictionary):
    """
    Convertit un dictionnaire en une chaîne JSON.

    Args:
        dictionary (dict): Le dictionnaire à convertir.

    Returns:
        str: La chaîne JSON résultante.
    """
    return json.dumps(dictionary)