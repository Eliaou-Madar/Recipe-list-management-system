using MediatR;
using Microsoft.EntityFrameworkCore;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Queries;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class GetAllRecipesHanlder : IRequestHandler<GetAllRecipesQuery, IEnumerable<Recipe>>
    {
        private readonly RecipeContext _dbContext;

        public GetAllRecipesHanlder(RecipeContext dbContext)
        {
            _dbContext = dbContext;

        }
        public async Task<IEnumerable<Recipe>> Handle(GetAllRecipesQuery request, CancellationToken cancellationToken)
        {
            if (_dbContext == null)
            {
                return Enumerable.Empty<Recipe>();
            }
            return await _dbContext.Recipes.ToListAsync();
        }
    }
}
