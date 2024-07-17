using MediatR;
using Microsoft.EntityFrameworkCore;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Queries;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class GetRandomRecipesHandler : IRequestHandler<GetRandomRecipesQuery, IEnumerable<Recipe>>
    {
        private readonly RecipeContext _dbContext;
        private readonly SpoonacularApiService _SpoonacularApiService;

        public GetRandomRecipesHandler(RecipeContext dbContext, SpoonacularApiService SpoonaService)
        {
            _dbContext = dbContext;
            _SpoonacularApiService = SpoonaService;
        }
        public async Task<IEnumerable<Recipe>> Handle(GetRandomRecipesQuery request, CancellationToken cancellationToken)
        {
            var searchResult = await _SpoonacularApiService.GetRandomRecipesAsync(request.Number);

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
