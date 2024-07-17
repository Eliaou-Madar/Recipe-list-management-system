using Microsoft.EntityFrameworkCore;
using Newtonsoft.Json;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using WindowsSystem_ASP.NET.DAL.Entities;
using System.Xml;
using System.Collections.Generic;
using Newtonsoft.Json;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

namespace WebApplication1.DAL.Models
{
    public class RecipeContext : DbContext
    {
        public RecipeContext(DbContextOptions<RecipeContext> options): base(options)
        {
        }

        public DbSet<Recipe> Recipes { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            var converter = new ValueConverter<List<string>, string>(
         v => JsonConvert.SerializeObject(v),
         v => JsonConvert.DeserializeObject<List<string>>(v) ?? new List<string>());

           
        }

    }
}
 /* protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            var converter = new ValueConverter<List<string>, string>(
         v => JsonConvert.SerializeObject(v),
         v => JsonConvert.DeserializeObject<List<string>>(v) ?? new List<string>());

            modelBuilder.Entity<Recipe>()
                .Property(e => e.Id)
                .HasConversion(converter);
        }*/