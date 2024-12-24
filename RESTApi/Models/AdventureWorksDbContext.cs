using Microsoft.EntityFrameworkCore;

namespace RESTApi.Models
{
    public class AdventureWorksDbContext : DbContext
    {
        public AdventureWorksDbContext(DbContextOptions<AdventureWorksDbContext> options)
            : base(options) { }

        public DbSet<Product> Products { get; set; } = null!;
    }
}