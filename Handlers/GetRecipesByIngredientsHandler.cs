using MediatR;
using Microsoft.EntityFrameworkCore;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Queries;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class GetRecipesByIngredientsHandler : IRequestHandler<GetRecipesByIngredientsQuery, IEnumerable<Recipe>>
    {
        
        private readonly SpoonacularApiService _SpoonacularApiService;

        public GetRecipesByIngredientsHandler(RecipeContext dbContext, SpoonacularApiService SpoonaService, ImaggaApiService maggaApiService)
        {

            _SpoonacularApiService = SpoonaService;
        }
        public async Task<IEnumerable<Recipe>> Handle(GetRecipesByIngredientsQuery request, CancellationToken cancellationToken)
        {
            var searchResult = await _SpoonacularApiService.RecipesByIngredientsAsync(request.SearchTerm);


            // Assurez-vous que searchResult n'est pas null
            if (searchResult != null)
            {
                // Créez une liste pour stocker les recettes
                var recipes = new List<Recipe>();

                // Parcourez chaque élément du tableau JSON reçu
                foreach (var blRecipe in searchResult)
                {
                    // Convertissez chaque élément du tableau JSON en une entité Recipe
                    var recipe = BlConversion.GetRecipe(blRecipe);

                    // Ajoutez la recette à la liste
                    recipes.Add(recipe);
                }

                // Retournez la liste de recettes
                return recipes;
            }
            else
            {
                // Si searchResult est null, retournez une liste vide
                return Enumerable.Empty<Recipe>();
            }
        }
    }
}
