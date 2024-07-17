using MediatR;
using Microsoft.EntityFrameworkCore;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Queries;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class GetRecipeInDatabaseBySearchQueryHandler : IRequestHandler<GetRecipeInDatabaseBySearchQuery, IEnumerable<Recipe>>
    {
        private readonly RecipeContext _dbContext;
        private readonly ImaggaApiService _maggaApiService;

        public GetRecipeInDatabaseBySearchQueryHandler(RecipeContext dbContext, SpoonacularApiService tmdbApiService, ImaggaApiService maggaApiService)
        {
            _dbContext = dbContext;
            _maggaApiService = maggaApiService;
        }
        public async Task<IEnumerable<Recipe>> Handle(GetRecipeInDatabaseBySearchQuery request, CancellationToken cancellationToken)
        {
            var allRecipes = await _dbContext.Recipes.ToListAsync(cancellationToken);

            var filteredRecpes = allRecipes.Where(recipe =>
                                recipe.Title != null &&
                                recipe.Title.IndexOf(request.SearchTerm, StringComparison.OrdinalIgnoreCase) >= 0);

            var recipes = new List<Recipe>();
            recipes.AddRange(filteredRecpes);

            foreach (var recipe in allRecipes)
            {
                // Vérifie si le poster n'est pas null ou vide et si le film n'existe pas déjà dans la liste movies
                if (!string.IsNullOrEmpty(recipe.Image) && !filteredRecpes.Any(m => m.SpoId == recipe.Id) &&
                    !recipes.Any(m => m.Id == recipe.Id))
                {
                    // Récupérer tous les tags de l'API
                    var tags = await _maggaApiService.TagImageAsync(recipe.Image);

                    // Vérifier s'il existe des tags correspondant au terme de recherche (mot clé)
                    if (tags.Any(tag => tag.Contains(request.SearchTerm, StringComparison.InvariantCultureIgnoreCase)))
                    {
                        // Si oui, ajouter le film à la liste de films à retourner
                        recipes.Add(recipe);
                    }
                }
            }

            return recipes;

        }
    }
}
