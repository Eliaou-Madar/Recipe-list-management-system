using MediatR;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.Commands;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class UpdateCommandHanlder : IRequestHandler<UpdateRecipeCommand, int>
    {
        private readonly RecipeContext _dbContext;

        public UpdateCommandHanlder(RecipeContext dbContext)
        {
            _dbContext = dbContext;
        }

        public async Task<int> Handle(UpdateRecipeCommand request, CancellationToken cancellationToken)
        {
            var recipe = await _dbContext.Recipes.FindAsync(request.Id);
            if (recipe == null)
            {
                return 0; // recipe not found
            }
            
            recipe.Id = request.Id;
            recipe.Title = request.Title ?? recipe.Title;
            recipe.Servings = request.Servings ?? recipe.Servings;
            recipe.ReadyInMinutes = request.ReadyInMinutes ?? recipe.ReadyInMinutes;
            recipe.SourceName = request.SourceName ?? recipe.SourceName;
            recipe.SourceUrl = request.SourceUrl ?? recipe.SourceUrl;
            recipe.HealthScore = request.HealthScore ?? recipe.HealthScore;
            recipe.PricePerServing = request.PricePerServing ?? recipe.PricePerServing;
            recipe.DairyFree = request.DairyFree ?? recipe.DairyFree; 
            recipe.GlutenFree = request.GlutenFree ?? recipe.GlutenFree;
            recipe.Summary = request.Summary ?? recipe.Summary;
            recipe.Image = request.Image ?? recipe.Image;
            recipe.SpoId = request.SpoId;
            await _dbContext.SaveChangesAsync();
            
            return 1; // Mise à jour réussie
            
        }
    }
}

