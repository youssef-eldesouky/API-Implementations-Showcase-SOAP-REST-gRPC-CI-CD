# API Implementations Showcase
This repository showcases implementations of SOAP, REST, and gRPC services. Each service is implemented in its own project within the solution.

## Project Structure
```
.gitignore
GrpcService/
    appsettings.json
    GrpcService.csproj
    Program.cs
    Properties/
        launchSettings.json
    Protos/
        product.proto
    Services/
        ProductService.cs
RESTApi/
    appsettings.json
    Controllers/
        ProductsController.cs
        WeatherForecastController.cs
    Models/
        AdventureWorksDbContext.cs
        Product.cs
    Program.cs
    Properties/
        launchSettings.json
    RESTApi.csproj
    RESTApi.http
    WeatherForecast.cs
SOAPService/
    .gitignore
    App.config
    CustomerService.cs
    ICustomerService.cs
    IService.cs
    Properties/
        AssemblyInfo.cs
    Service.svc
    SOAPService.csproj
SOAPService.sln
```
## Projects
### SOAPService
#### A SOAP-based service that provides customer details.

Service Definition: IService.cs, ICustomerService.cs
Service Implementation: CustomerService.cs
Service Configuration: App.config
Service Host: Service.svc

### RESTApi
#### A RESTful API that provides product and weather forecast information.

##### Controllers:

ProductsController.cs

WeatherForecastController.cs

##### Models:

AdventureWorksDbContext.cs

Product.cs

WeatherForecast.cs

##### Configuration:

appsettings.json

launchSettings.json

##### Program Entry Point: Program.cs

##### HTTP Request Sample: RESTApi.http


### GrpcService
#### A gRPC-based service that provides product details.

##### Service Definition: product.proto
##### Service Implementation: ProductService.cs

##### Configuration:

  appsettings.json
  launchSettings.json
  Program Entry Point: Program.cs

## Getting Started
### Prerequisites

.NET SDK 8.0 or later

Visual Studio or Visual Studio Code

### Building the Solution
To build the solution, navigate to the root directory and run:
```
dotnet build
```

### Running the Services
Each service can be run individually. Navigate to the respective project directory and run:
```
dotnet run
```

### Testing the Services
SOAPService: Use a tool like WcfTestClient to test the SOAP service.

RESTApi: Use Swagger UI or tools like Postman to test the REST API.

GrpcService: Use a gRPC client or tools like BloomRPC to test the gRPC service.


## Acknowledgments:
Microsoft Documentation

Swagger

gRPC
