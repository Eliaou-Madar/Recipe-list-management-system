using MediatR;
using WindowsSystem_ASP.NET.DAL.Entities;

namespace WindowsSystem_ASP.NET.Queries
{
    public class GetRecipesByIngredientsQuery : IRequest<IEnumerable<Recipe>>

    {
        public string SearchTerm { get; }

        public GetRecipesByIngredientsQuery(string s)
        {
            SearchTerm = s;
        }
    }
}
