
# Docker Troubleshooting Guide

## Permission Denied Error

If you encounter permission denied errors when running Docker commands, follow these steps to resolve the issue.

### Common Error Message
```
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
```

### Solution Steps

#### 1. Add the Docker Group
First, add the docker group if it doesn't already exist:
```bash
sudo groupadd docker
```

#### 2. Add User to Docker Group
Add the connected user `$USER` to the docker group:
```bash
sudo gpasswd -a $USER docker
```

> **Note:** Change the user name to match your preferred user if you do not want to use your current user.

#### 3. Activate Group Changes
To activate the changes to groups, you have two options:

**Option A:** Use newgrp command
```bash
newgrp docker
```

**Option B:** Log out and log back in to your system

#### 4. Test Docker Installation
Test that Docker is working correctly:
```bash
docker run hello-world
```

### Additional Troubleshooting

#### If the Error Persists
If you still get the permission denied error after following the above steps:

1. **Restart the virtual machine** (if you're using a VM)
2. **Restart the Docker service:**
   ```bash
   sudo systemctl restart docker
   ```
3. **Check Docker service status:**
   ```bash
   sudo systemctl status docker
   ```

#### Verify Group Membership
To verify that your user has been added to the docker group:
```bash
groups $USER
```

The output should include `docker` in the list of groups.
