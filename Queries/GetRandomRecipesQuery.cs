using MediatR;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Services;

namespace WindowsSystem_ASP.NET.Queries
{
    public class GetRandomRecipesQuery : IRequest<IEnumerable<Recipe>>
    {
        public int Number;

        public GetRandomRecipesQuery(int s)
        {
            this.Number = s;
        }
    }
}
