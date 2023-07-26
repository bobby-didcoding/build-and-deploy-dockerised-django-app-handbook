# <span style="color:orange">Building a Production-Ready Django Project with a Digital Resume and Shop</span>

## <span style="color:orange">Background</span>
Welcome to our comprehensive course on building a fully functional and production-ready Django project! This course is designed to provide you with a step-by-step guide through the entire process of creating a robust web application – a Digital Resume with an integrated lightweight shop – that will be ready for deployment and accessible to the public.

## <span style="color:orange">Course Overview</span>
In this hands-on course, we will delve into the world of Django, one of the most popular and powerful web development frameworks, to build a feature-rich web application that showcases your skills, experience, and achievements in a digital resume format. Additionally, we will incorporate a lightweight shop to offer products or services, enhancing the overall functionality and user experience.



## <span style="color:orange">Prerequisites<span>
* [Docker & Docker Compose](https://docs.docker.com/desktop/) (<span style="color:orange">Local Development with Docker</span>)


## <span style="color:orange">Repository<span>
1. Navigate to your development directory and open a terminal.
2. Clone the development repository:
    ```
    git clone -b 04-admin https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook.git .
    ```


## <span style="color:orange">Setup<span>
We need a new .env file to store our project secrets and api keys.

```
#Unix and MacOS
cp env_template .env

#windows
copy env_template .env
```

## <span style="color:orange">Build Docker images<span>

Use the following command to build the docker images:
> Make sure Docker is running on your machine!

1. Open a terminal on your machine.

2. Optional step! Prune docker.
    You may want to prune un-used Docker images and containers.
    ```
    docker system prune
    ```

3. Fire up a dev Docker container.
    > Note: you may want to prune un used Docker images and containers
    ```
    docker-compose up -d --build
    ```

## <span style="color:orange">Finished<span>

You should now be up and running!
>Note: Open an incognito browser when testing your project (Ctrl + Shift + N)

* Main site is running on [http://localhost:8000](http://localhost:8000)


## <span style="color:orange">Helpful Docker stuff<span>
You can run Django commands as normal by accessing the Django `app` image.

The following example display all files in the container

```
docker exec -it app bash
ls
exit
```

The following example will rebuild one container
```
docker-compose -f up -d --no-deps --build app
```

## <span style="color:orange">Next step<span>

Each branch has its own `LECTURE_OVERVIEW.md` file that describes what we will cover during the lecture.

***
***
