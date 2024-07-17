using MediatR;
using WebApplication1.DAL.Models;
using WindowsSystem_ASP.NET.Commands;

namespace WindowsSystem_ASP.NET.Handlers
{
    public class DeleteCommandHandler : IRequestHandler<DeleteRecipeCommand, int>
    {
        private readonly RecipeContext _dbContext;

        public DeleteCommandHandler(RecipeContext dbContext)
        {
            _dbContext = dbContext;
        }

        public async Task<int> Handle(DeleteRecipeCommand request, CancellationToken cancellationToken)
        {
            var recipe = await _dbContext.Recipes.FindAsync(request.Id);
            if (recipe == null)
            {
                return 0;
            }

            _dbContext.Recipes.Remove(recipe);
            await _dbContext.SaveChangesAsync();

            return 1;
        }
    }
}
