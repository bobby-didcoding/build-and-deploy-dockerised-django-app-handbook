# <span style="color:orange">Lecture overview</span>

Welcome to the "Connecting and Preparing Your Digital Ocean Droplet for Deployment with Visual Studio Code" course section! In this module, we will walk you through the step-by-step process of establishing a secure connection to your Digital Ocean droplet using Visual Studio Code (VS Code) as your development environment. We will also cover essential tasks such as installing necessary software like Docker Compose, creating a new user for enhanced security, and setting up logging directories for efficient management.

Introduction to Visual Studio Code and Digital Ocean:

- Brief overview of Visual Studio Code and its advantages for server management
- Introduction to Digital Ocean droplets and their role in hosting applications
- Understanding the importance of secure connections and proper preparation
- Installing the Remote - SSH extension in Visual Studio Code
- Configuring SSH key-based authentication for secure connections
- Establishing a seamless SSH connection to your droplet through VS Code
- Leveraging VS Code's integrated terminal for remote server commands
- Installing Docker Compose on your Digital Ocean droplet
- Verifying the successful installation and basic usage
- Creating a new user on the droplet with appropriate permissions
- Creating logging directories on the droplet for various applications

By the end of this course section, you will be proficient in connecting to your Digital Ocean droplet through Visual Studio Code, equipped with essential software like Docker Compose, and adept at creating users and setting up logging directories. You'll have the knowledge and confidence to efficiently manage and deploy applications on your Digital Ocean droplet, ensuring they run securely and reliably. Whether you're a developer, sysadmin, or anyone involved in deploying web applications, this course section will empower you to harness the full potential of Visual Studio Code for managing your Digital Ocean infrastructure effectively.

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/29/files).

# <span style="color:orange">Instructions</span>

1) SSH into droplet

2) Open a new terminal and use the following to upgrade package information:
    ```
    sudo apt update
    sudo apt upgrade
    ```
3) When complete you can go ahead and download the current stable release of docker-compose
    ```
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```
4) We now need to apply executable permissions to the binary file. You can do this by using the following command:
    ```
    sudo chmod +x /usr/local/bin/docker-compose
    ```
5) Create a symbolic link to /usr/bin path. You can do this by using the following command:
    ```
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    ```
6) To test that docker and docker-compose are both present and correct, use the following commands.
    ```
    docker --version
    docker-compose --version
    ```

7) You can now create a new user that will be used for our project.
    ```
    adduser course
    usermod -aG sudo course
    gpasswd -a course sudo
    ```

8) Go ahead and create a new directory for our project logs.
    ```
    cd ..
    mkdir var/log/course
    ```
9) Now we need to create some blank certificates for ssl.
    ```
    echo > etc/ssl/certs/key.pem
    echo > etc/ssl/certs/cert.pem
    ```

All Done, your droplet is now ready for our project.

***
***
