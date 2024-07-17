using MediatR;
using Microsoft.EntityFrameworkCore;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Queries;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class GetSimilarRecipeHandler : IRequestHandler<GetSimilarRecipesQuery, IEnumerable<Recipe>>
    {
        
        private readonly SpoonacularApiService _tmdbApiService;

        public GetSimilarRecipeHandler(RecipeContext dbContext, SpoonacularApiService tmdbApiService)
        {
            
            _tmdbApiService = tmdbApiService;
        }
        public async Task<IEnumerable<Recipe>> Handle(GetSimilarRecipesQuery request, CancellationToken cancellationToken)
        {
            var searchResult = await _tmdbApiService.GetSimilarRecipesAsync(request.Id);

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
