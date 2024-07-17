using MediatR;
using WindowsSystem_ASP.NET.DAL.Entities;

namespace WindowsSystem_ASP.NET.Queries
{
    public class GetRecipeInDatabaseBySearchQuery : IRequest<IEnumerable<Recipe>>
    {
        public string SearchTerm { get; }

        public GetRecipeInDatabaseBySearchQuery(string s)
        {
            SearchTerm = s;
        }
    }
}
