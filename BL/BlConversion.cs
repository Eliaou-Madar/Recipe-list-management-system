using Newtonsoft.Json;
using WindowsSystem_ASP.NET.DAL.Entities;

namespace WindowsSystem_ASP.NET.BL
{
    public class BlConversion
    {
        private const string BaseImageUrl = "https://image.tmdb.org/t/p/";
        public static Recipe? GetRecipe(BlRecipe bl_recipe)
        {
            return new Recipe()
            {
                Id= bl_recipe.Id,
                Title = bl_recipe.Title,
                Servings = bl_recipe.Servings,
                ReadyInMinutes = bl_recipe.ReadyInMinutes,
                SourceName = bl_recipe.SourceName,
                SourceUrl = bl_recipe.SourceUrl,
                HealthScore = bl_recipe.HealthScore,
                PricePerServing  = bl_recipe.PricePerServing,
                DairyFree = bl_recipe.DairyFree,
                GlutenFree = bl_recipe.GlutenFree,
                Summary = bl_recipe.Summary,
                Image = bl_recipe.Image,
                ImaggaStrings = bl_recipe.ImaggaStrings
                          .SelectMany(tagsResponse => tagsResponse.Result.Tags) // Assurez-vous d'accéder correctement à `Tags` à travers `Result`
                         .Select(tagItem => tagItem.Tag.En)
                          .ToList(),

      /*  Genres = bl_movie.Genres.Select(g => g.Name).ToList(),
                Overview = bl_movie.Overview,
                TmdbId = bl_movie.Id,
                PosterURL = GetPosterUrl(bl_movie.Poster_Path),
                ReleaseDate = bl_movie.Release_Date,
                RunTime = bl_movie.RunTime,
                Title = bl_movie.Title,
                TrailerURL = bl_movie.TrailerURL,
                vote_average = bl_movie.vote_average,
                ImaggaStrings = bl_movie.ImaggaStrings
                        .SelectMany(tagsResponse => tagsResponse.Result.Tags) // Assurez-vous d'accéder correctement à `Tags` à travers `Result`
                        .Select(tagItem => tagItem.Tag.En)
                        .ToList()*/
                
            };
        }

        public static string GetPosterUrl(string posterPath, string size = "w300")
        {
            if (string.IsNullOrWhiteSpace(posterPath))
            {
                return null; // Or return a default image URL
            }

            return $"{BaseImageUrl}{size}{posterPath}";
        }



    }
}
