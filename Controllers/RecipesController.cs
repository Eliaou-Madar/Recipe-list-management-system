using MediatR;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.VisualBasic;
using WindowsSystem_ASP.NET.BL;
using WindowsSystem_ASP.NET.Commands;
using WindowsSystem_ASP.NET.DAL.Entities;
using WindowsSystem_ASP.NET.Queries;
using WindowsSystem_ASP.NET.Services;
using static Microsoft.EntityFrameworkCore.DbLoggerCategory.Database;

namespace WindowsSystem_ASP.NET.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RecipesController : ControllerBase
    {
        private readonly IMediator _mediator;

        public RecipesController(IMediator mediator)
        {
            _mediator = mediator;
        }

        // GET: api/Recipes
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Recipe>>> GetRecipes()
        {
            var recipes = await _mediator.Send(new GetAllRecipesQuery());
            return Ok(recipes);
        }

        // GET: Similar Recipes
        [HttpGet("Similar")]
        public async Task<ActionResult<IEnumerable<Recipe>>> GetSimilarRecipes(int id)
        {
            var recipes = await _mediator.Send(new GetSimilarRecipesQuery{ Id = id });
            if (recipes == null)
            {
                return NotFound();
            }

            return Ok(recipes);
        }

        // GET: api/Recipes/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Recipe>> GetRecipe(int id)
        {

            var recipe = await _mediator.Send(new GetRecipeByIdQuery { Id = id });
            if (recipe == null)
            {
                return NotFound();
            }

            return Ok(recipe);


        }

        // GET: by ingredient
        [HttpGet("RecipesByIngredient/query")]
        public async Task<ActionResult<IEnumerable<Recipe>>> RecipesByIngredient(string s)
        {

            if (string.IsNullOrWhiteSpace(s))
            {
                return BadRequest("Search term is required.");
            }

            var recipes = await _mediator.Send(new GetRecipesByIngredientsQuery(s));
            return Ok(recipes);
        }

        // GET: imagga
        [HttpGet("imagga/query")]
        public async Task<ActionResult<IEnumerable<Recipe>>> Imagga(string s)
        {

            if (string.IsNullOrWhiteSpace(s))
            {
                return BadRequest("Search term is required.");
            }

            var recipes = await _mediator.Send(new GetRecipeInDatabaseBySearchQuery(s));
            return Ok(recipes);
        }

        // GET: Random Recipes
        [HttpGet("Random_Recipes")]
        public async Task<ActionResult<IEnumerable<Recipe>>> RandomRecipes(int s)
        {

            var recipes = await _mediator.Send(new GetRandomRecipesQuery(s));
            return Ok(recipes);
        }

        // POST: api/Recipes
        [HttpPost("Add/Id")]
        public async Task<ActionResult<Recipe>> PostRecipe([FromQuery] int id)
        {
            var recipeId = await _mediator.Send(new CreateRecipeCommand(id));
            return Ok(recipeId);

        }

        // PUT: api/Recipes/5
        [HttpPut("Update/{id}")]
        public async Task<IActionResult> PutRecipe(int id, Recipe recipe)
        {
            if (id != recipe.Id)
            {
                return BadRequest();
            }

            var success = await _mediator.Send(new UpdateRecipeCommand(recipe.Id, recipe.Title, recipe.Servings, recipe.ReadyInMinutes,recipe.SourceName,recipe.SourceUrl, recipe.HealthScore,recipe.PricePerServing,recipe.DairyFree,recipe.GlutenFree,recipe.Summary, recipe.Image, recipe.SpoId));

            if (success == 0)
            {
                return NotFound();
            }

            return NoContent();
        }



        // DELETE: api/Recipes/5
        [HttpDelete("Delete/Id")]
        public async Task<IActionResult> DeleteRecipe([FromQuery] int id)
        {
            var success = await _mediator.Send(new DeleteRecipeCommand(id));

            if (success == 0)
            {
                return NotFound();
            }

            return Ok();
        }
    }
}
