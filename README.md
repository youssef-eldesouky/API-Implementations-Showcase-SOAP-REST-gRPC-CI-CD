# API Implementations Showcase: SOAP, REST, gRPC with CI/CD

This repository demonstrates the implementation of three distinct API architectures: **SOAP**, **REST**, and **gRPC**. Each implementation is built with modern technologies and features a complete CI/CD pipeline using Jenkins and Docker for deployment. This project is designed as a comprehensive showcase of API design, testing, and deployment best practices.

## Features
- **SOAP API**: Built using Windows Communication Foundation (WCF) to demonstrate traditional web services with XML-based communication.
- **REST API**: Developed with ASP.NET Core to showcase a lightweight, HTTP-based architecture for modern web applications.
- **gRPC API**: Implemented using Protocol Buffers (protobuf) to highlight a high-performance, binary communication protocol.
- **CI/CD Pipeline**: Configured with Jenkins to automate the build, test, and deployment process for all three APIs.
- **Dockerized Deployment**: Each API is containerized using Docker for consistent, cross-environment deployments.


## Project Structure
- **SOAPService**: Implementation of the SOAP API using WCF.
- **RESTApi**: Implementation of the REST API using ASP.NET Core.
- **GrpcService**: Implementation of the gRPC API with Protocol Buffers.
- **Jenkinsfile**: Jenkins pipeline configuration for CI/CD.
- **docker-compose.yml**: Docker Compose file to orchestrate multi-service deployment.


## How to Use

### Prerequisites
- [.NET SDK](https://dotnet.microsoft.com/download) installed on your system.
- [Docker](https://www.docker.com/) and Docker Compose installed.
- A running Jenkins instance for CI/CD.

### Steps to Run the Project Locally
1. Clone the repository:
```
git clone https://github.com/youssef-eldesouky/API-Implementations-Showcase-SOAP-REST-gRPC-CI-CD.git
cd API-Implementations-Showcase-SOAP-REST-gRPC-CI-CD
```
2. Build and run the services using Docker Compose:
```bash
docker-compose up --build
```
3. Access the services:
   SOAP API: http://localhost:8001/Service.svc?wsdl
   REST API: http://localhost:8002/swagger/index.html
   gRPC API: Use a gRPC client (e.g., BloomRPC) to connect to localhost:8003.
4. To test endpoints:
   Use tools like SoapUI, Postman, or Swagger UI for SOAP and REST APIs.
   Use BloomRPC or grpcurl for gRPC API testing.

## CI/CD Pipeline
### The project includes a Jenkins pipeline that automates:

1. Build: Compiles all projects using dotnet build.
2. Test: Runs unit tests using dotnet test.
3. Docker Build: Builds Docker images for each API service.
4. Deploy: Deploys the services using Docker Compose

### Running the Jenkins Pipeline
Add the repository to Jenkins and configure the pipeline with the included Jenkinsfile.
Trigger the pipeline to automate the build, test, and deployment stages.

## APIs Overview
### SOAP API
1. Built using WCF to implement a customer service.
1. Features a single method GetCustomerDetails to retrieve customer data based on an ID.

### REST API

1. Developed using ASP.NET Core.
1. Includes a ProductsController for managing product details, with an endpoint to retrieve product data by ID.
1. Integrated with Swagger for API documentation.

### gRPC API
1. Implemented using Protocol Buffers (protobuf).
1. Features a ProductService that provides product details through a binary, high-performance communication protocol.

## Dockerized Deployment
#### Each API is containerized using Docker. The docker-compose.yml file manages multi-service deployment. Ports for each service:

-SOAP: 8001
-REST: 8002
-gRPC: 8003

## Author
#### Youssef Eldesouky
#### GitHub: youssef-eldesouky
