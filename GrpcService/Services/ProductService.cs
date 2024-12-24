using Grpc.Core;
using GrpcService.Protos;

namespace GrpcService.Services
{
    public class ProductService : Protos.ProductService.ProductServiceBase
    {
        private readonly ILogger<ProductService> _logger;

        public ProductService(ILogger<ProductService> logger)
        {
            _logger = logger;
        }

        public override Task<ProductResponse> GetProductDetails(ProductRequest request, ServerCallContext context)
        {
            return Task.FromResult(new ProductResponse
            {
                ProductDetails = $"Details for Product ID: {request.ProductId}"
            });
        }
    }
}