using MediatR;

namespace WindowsSystem_ASP.NET.Commands
{
    public class DeleteRecipeCommand : IRequest<int>
    {
        public DeleteRecipeCommand(int id)
        {
            Id = id;
        }

        public int Id { get; set; }
    }
}
