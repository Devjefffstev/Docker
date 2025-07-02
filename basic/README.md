# Basic Docker Example - FastAPI Application

This is a basic example demonstrating how to containerize a FastAPI application using Docker.

## Application Overview

This FastAPI application provides the following endpoints:
- `/` - Root endpoint
- `/greet/{yourname}` - Returns a personalized greeting message

## Building the Docker Image

### Build with specific Dockerfile and tag
```bash
docker build -t my-fastapi-app -f basicExample .
```

### Build with custom version tag
```bash
docker build -t my-fastapi-app:v1 -f basicExample .
```

## Running the Container

### Run the container locally
```bash
docker run -it -p 8000:8000 my-fastapi-app
```

### Command explanation:
- `-it` - Run in interactive mode with TTY
- `-p 8000:8000` - Map host port 8000 to container port 8000
- `my-fastapi-app` - The image name to run

## Testing the Application

Once the container is running, you can test the endpoints:

### Root endpoint
```bash
curl http://localhost:8000/
```
![alt text](image.png)
### Greeting endpoint
```bash
curl http://localhost:8000/greet/YourName
```
![alt text](image2.png)
## Additional Docker Commands

### List running containers
```bash
docker ps
```

### Stop the container
```bash
docker stop <container-id>
```

### Remove the image
```bash
docker rmi my-fastapi-app
```