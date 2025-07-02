# Docker
To learn and contribute to the community

## What is Docker?

Docker is a powerful containerization platform that enables developers to package applications and their dependencies into lightweight, portable containers. These containers can run consistently across different environments, from development machines to production servers.

### Key Concepts:

- **Containers**: Lightweight, standalone packages that include everything needed to run an application - code, runtime, system tools, libraries, and settings
- **Images**: Read-only templates used to create containers, built from a set of instructions called a Dockerfile
- **Dockerfile**: A text file containing commands to assemble an image
- **Docker Engine**: The runtime that manages containers on a host system
- **Registry**: A service for storing and distributing Docker images (like Docker Hub)

### Benefits:

- **Consistency**: "Works on my machine" becomes "works everywhere"
- **Isolation**: Applications run in isolated environments without conflicts
- **Portability**: Containers run the same way across different platforms
- **Efficiency**: Containers share the host OS kernel, making them more resource-efficient than VMs
- **Scalability**: Easy to scale applications horizontally by running multiple container instances
- **DevOps Integration**: Streamlines CI/CD pipelines and deployment processes

### Common Use Cases:

- Application deployment and distribution
- Microservices architecture
- Development environment standardization
- Continuous integration and deployment
- Cloud migration and hybrid deployments
- Testing and quality assurance

## Common Dockerfile Instructions

Some of the most common instructions in a Dockerfile include:

- **FROM <image>** - this specifies the base image that the build will extend.
- **WORKDIR <path>** - this instruction specifies the "working directory" or the path in the image where files will be copied and commands will be executed.
- **COPY <host-path> <image-path>** - this instruction tells the builder to copy files from the host and put them into the container image.
- **RUN <command>** - this instruction tells the builder to run the specified command.
- **ENV <name> <value>** - this instruction sets an environment variable that a running container will use.
- **EXPOSE <port-number>** - this instruction sets configuration on the image that indicates a port the image would like to expose.
- **USER <user-or-uid>** - this instruction sets the default user for all subsequent instructions.
- **ENTRYPOINT ["<command>", "<arg1>"]** - this instruction sets the main command that will always be executed when the container starts, and cannot be overridden by docker run arguments.
- **CMD ["<command>", "<arg1>"]** - this instruction sets the default command a container using this image will run.

