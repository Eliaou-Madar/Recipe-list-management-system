using MediatR;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Queries
{
    public class GetSimilarRecipesQuery : IRequest<IEnumerable<Recipe>>
    {
        public int Id { get; set; }
    }
}
