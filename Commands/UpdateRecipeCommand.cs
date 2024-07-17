using MediatR;

namespace WindowsSystem_ASP.NET.Commands
{
    public class UpdateRecipeCommand : IRequest<int>
    {
        public int Id { get; set; }
        public string? Title { get; set; }
        public int? Servings { get; set; }
        public int? ReadyInMinutes { get; set; } //AnneeFabrication
        public string? SourceName { get; set; } // Example: gasoline, diesel, electric, hybrid, etc.
        public string? SourceUrl { get; set; } // Engine power in horsepower (HP) or kilowatts (kW)
        public int? HealthScore { get; set; } // Example: manual, automatic, CVT, etc.
        public float? PricePerServing { get; set; }
        public bool? DairyFree { get; set; } // produit laitier 
        public bool? GlutenFree { get; set; }

        public string? Summary { get; set; } //description 
                                             //public double? Price { get; set; } // Car price in euros
        public string? Image { get; set; } // Car image URL
                                              //public double? vote_average { get; set; } // note moyenne
        public int? SpoId { get; set; }

        public List<string> ImaggaStrings { get; set; } = new List<string>();



        public UpdateRecipeCommand(int id, string? title, int? servings, int? readyInMinutes, string? sourceName, string? sourceUrl, int? healthScore, float? pricePerServing, bool? dairyFree, bool? glutenFree, string? summary, string? imageURL, int? spoId, List<string>? imaggaStrings)
        {
            Id = id;    //  14/14
            Title = title;
            Servings = servings;
            ReadyInMinutes = readyInMinutes;
            SourceName = sourceName;
            SourceUrl = sourceUrl;
            HealthScore = healthScore;
            PricePerServing = pricePerServing;
            DairyFree = dairyFree;
            GlutenFree = glutenFree;
            Summary = summary;
            Image = imageURL;
            SpoId = spoId;
            ImaggaStrings = imaggaStrings;
        }

        public UpdateRecipeCommand(int id, string? title, int? servings, int? readyInMinutes, string? sourceName, string? sourceUrl, int? healthScore, float? pricePerServing, bool? dairyFree, bool? glutenFree, string? summary, string? imageURL, int? spoId)
        {
            Id = id; //  13/14
            Title = title;
            Servings = servings;
            ReadyInMinutes = readyInMinutes;
            SourceName = sourceName;
            SourceUrl = sourceUrl;
            HealthScore = healthScore;
            PricePerServing = pricePerServing;
            DairyFree = dairyFree;
            GlutenFree = glutenFree;
            Summary = summary;
            Image = imageURL;
            SpoId = spoId;

        }
    }
}