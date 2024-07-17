import json
import requests
import ssl

class RecipeModel:
    def __init__(self):
        self.recipes = []

    def set_recipes(self, recipes):
        self.recipes = recipes

    def get_recipes(self):
        return self.recipes

    def dict_to_json_string_converter(dictionary):
        """
        Convertit un dictionnaire en une chaîne JSON.

        Args:
            dictionary (dict): Le dictionnaire à convertir.

        Returns:
            str: La chaîne JSON résultante.
        """
        return json.dumps(dictionary)
    

    @staticmethod
    def get_time_by_id(id):
        url = f"https://localhost:7271/api/Recipes/{id}"
        context = ssl._create_unverified_context()
        response = requests.get(url, verify=False)
        data = response.json()
        time1 = data.get("readyInMinutes")
        return time1  