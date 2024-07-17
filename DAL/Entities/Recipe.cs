using System.ComponentModel.DataAnnotations.Schema;

namespace WindowsSystem_ASP.NET.DAL.Entities
{
    public class Recipe //14
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

        [NotMapped]
        public List<string>? ImaggaStrings { get; set; } = new List<string>();

    }
}
