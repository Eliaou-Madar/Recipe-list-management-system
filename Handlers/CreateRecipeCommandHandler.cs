using MediatR;
using Microsoft.EntityFrameworkCore;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.Commands;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class CreateRecipeCommandHandler : IRequestHandler<CreateRecipeCommand, Recipe>
    {
        private readonly RecipeContext _dbContext;
        private readonly SpoonacularApiService _SpoonacularApiService;

        public CreateRecipeCommandHandler(RecipeContext dbContext, SpoonacularApiService SpoonaApiService)
        {
            _dbContext = dbContext;
            _SpoonacularApiService = SpoonaApiService;
        }
        public async Task<Recipe> Handle(CreateRecipeCommand request, CancellationToken cancellationToken)
        {
            var _recipe = _dbContext.Recipes.FirstOrDefault(x => x.SpoId == request.Id);
            if (_recipe == null)
            {
                var recipe = await _SpoonacularApiService.GetRecipeByIdAsync(request.Id);
                _recipe = BlConversion.GetRecipe(recipe);
                _recipe.SpoId = _recipe.Id;
                _recipe.Id = 0;
                _dbContext.Recipes.Add(_recipe);
                await _dbContext.SaveChangesAsync();
            }
            return _recipe;

        }
    }
}
