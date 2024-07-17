using MediatR;
using WindowsSystem_ASP.NET.DAL.Entities;

namespace WindowsSystem_ASP.NET.Queries
{
    public class GetRecipesBySearchTermQuery : IRequest<IEnumerable<Recipe>>

    {
        public string SearchTerm { get; }

        public GetRecipesBySearchTermQuery(string s)
        {
            SearchTerm = s;
        }
    }
}
