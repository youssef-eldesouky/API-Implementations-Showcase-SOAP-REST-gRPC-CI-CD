# Multi-Protocol API Implementation Project

This project demonstrates the implementation of three different API protocols (SOAP, REST, and gRPC) using .NET, along with CI/CD pipeline configuration using Jenkins.

## 🚀 Features

- SOAP API implementation using WCF
- REST API implementation with ASP.NET Core
- gRPC API implementation
- Complete CI/CD pipeline with Jenkins
- Docker containerization support
- Swagger documentation for REST API

## 🛠️ Technologies Used

- .NET Core
- WCF (Windows Communication Foundation)
- Entity Framework Core
- Protocol Buffers (protobuf)
- Docker
- Jenkins
- Swagger/OpenAPI

## 📁 Project Structure

The solution contains three main projects:

1. **SOAPService**: WCF-based SOAP API implementation
2. **RESTApi**: ASP.NET Core-based REST API implementation
3. **GrpcService**: gRPC service implementation

## 🏃‍♂️ Getting Started

### Prerequisites

- .NET 8.0 SDK
- Visual Studio 2022 or VS Code
- Docker Desktop
- Jenkins (for CI/CD)

### Installation

1. Clone the repository
```bash
git clone https://github.com/youssef-eldesouky/API-Implementations-Showcase-SOAP-REST-gRPC-CI-CD.git
```

2. Navigate to the solution directory
```bash
cd API-Implementations-Showcase-SOAP-REST-gRPC-CI-CD
```

3. Build the solution
```bash
dotnet build
```

4. Run the services
```bash
docker-compose up
```

## 🔌 API Endpoints

### SOAP Service
- Base URL: `http://localhost:8001`
- WSDL: `http://localhost:8001/Service.svc?wsdl`

### REST API
- Base URL: `http://localhost:8002`
- Swagger UI: `http://localhost:8002/swagger/index.html`

### gRPC Service
- Base URL: `http://localhost:8003`

## 🔧 Configuration

Each service can be configured through their respective `appsettings.json` files. Docker configuration is maintained in `docker-compose.yml`.

## 🚀 Deployment

The project includes a Jenkins pipeline configuration in `Jenkinsfile` that handles:
- Building the solution
- Running tests
- Building Docker images
- Deploying services

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
