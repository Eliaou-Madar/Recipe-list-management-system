using MediatR;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.DAL;
using WindowsSystem_ASP.NET.Queries;
using WindowsSystem_ASP.NET.Services;
using WindowsSystem_ASP.NET.DAL.Entities;
using WebApplication1.DAL.Models;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class GetRecipeByIdHandler : IRequestHandler<GetRecipeByIdQuery, Recipe>
    {
        private readonly RecipeContext _dbContext;
        private readonly SpoonacularApiService _SpoonacularApiService;

        public GetRecipeByIdHandler(RecipeContext dbContext, SpoonacularApiService SpoonaService)
        {
            _dbContext = dbContext;
            _SpoonacularApiService = SpoonaService;
        }
        public async Task<Recipe> Handle(GetRecipeByIdQuery request, CancellationToken cancellationToken)
        {
            var recipe = _dbContext.Recipes.FirstOrDefault(x => x.SpoId == request.Id);
            if (recipe == null)
            {
                var blRecipe = await _SpoonacularApiService.GetRecipeByIdAsync(request.Id);
                if (blRecipe != null)
                {
                    recipe = BlConversion.GetRecipe(blRecipe);
                    return recipe;
                }

                return null;
            }

            return recipe;
        }
    }
}
