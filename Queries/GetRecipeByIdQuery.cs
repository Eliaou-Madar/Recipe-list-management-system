using MediatR;
using WindowsSystem_ASP.NET.DAL.Entities;

namespace WindowsSystem_ASP.NET.Queries
{
    public class GetRecipeByIdQuery : IRequest<Recipe>
    {
        public int Id { get; set; }
    }
}
