using Newtonsoft.Json;
using System.Text.Json;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.DAL.Entities;

namespace WindowsSystem_ASP.NET.Services
{
    public class SpoonacularApiService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiKey = "2e09e3b0c7b34919ae07bfdc022e35ce";//1c46024cef5d4b87bbd5958a1b971775//24a78e33e34d409bafb74af5b8da834d//////1c395c90bcc144a793a96c24da2a6533////24a78e33e34d409bafb74af5b8da834d

        public SpoonacularApiService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<BlRecipe> GetRecipeByIdAsync(int recipeId) //Ok
        {
            var response = await _httpClient.GetAsync($"recipes/{recipeId}/information?apiKey={_apiKey}");//$"recipes/{recipeId}/information?apiKey={_apiKey}"
            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                var recipe = JsonConvert.DeserializeObject<BlRecipe>(content);
                //recipe.TrailerURL = await GetTrailerUrlAsync(movie.Id);
               
                return recipe;
            }

            return null; // Or handle the error as preferred
        }

        public async Task<IEnumerable<BlRecipe>> RecipesByIngredientsAsync(string query) // Ok
        {
            var response = await _httpClient.GetAsync($"recipes/findByIngredients?ingredients={query}&apiKey={_apiKey}");//recipes/complexSearch?query=
         

            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();

                // Vérifiez si le contenu est un tableau JSON
                if (content.StartsWith("["))
                {
                    // Si c'est un tableau JSON, désérialisez-le en une liste d'objets BlRecipe
                    var recipes = JsonConvert.DeserializeObject<List<BlRecipe>>(content);
                    return recipes;
                }
                else
                {
                    // Sinon, désérialisez-le en un seul objet BlRecipe
                    var recipe = JsonConvert.DeserializeObject<BlRecipe>(content);
                    return new List<BlRecipe> { recipe };
                }
            }

            return null; // Ou gérez l'erreur selon votre préférence
        }


        public async Task<IEnumerable<BlRecipe>> GetSimilarRecipesAsync(int recipeId)//ok
        {
            var response = await _httpClient.GetAsync($"recipes/{recipeId}/similar?apiKey={_apiKey}");

            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();

                // Vérifiez si le contenu est un tableau JSON
                if (content.StartsWith("["))
                {
                    // Si c'est un tableau JSON, désérialisez-le en une liste d'objets BlRecipe
                    var recipes = JsonConvert.DeserializeObject<List<BlRecipe>>(content);
                    return recipes;
                }
                else
                {
                    // Sinon, désérialisez-le en un seul objet BlRecipe
                    var recipe = JsonConvert.DeserializeObject<BlRecipe>(content);
                    return new List<BlRecipe> { recipe };
                }
            }

            return null; // Ou gérez l'erreur selon votre préférence
        }

        public async Task<IEnumerable<BlRecipe>> GetRandomRecipesAsync(int number_recipe)
        {
            var response = await _httpClient.GetAsync($"recipes/random?number={number_recipe}&apiKey={_apiKey}");

            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();

                // Désérialisez directement en utilisant le type approprié
                var recipeResponse = JsonConvert.DeserializeObject<RecipeResponse>(content);

                return recipeResponse.Recipes;
            }

            return null; // Ou gérez l'erreur selon votre préférence
        }

        // Créez une classe pour représenter la réponse JSON
        public class RecipeResponse
        {
            [JsonProperty("recipes")]
            public List<BlRecipe> Recipes { get; set; }
        }



    }
}
