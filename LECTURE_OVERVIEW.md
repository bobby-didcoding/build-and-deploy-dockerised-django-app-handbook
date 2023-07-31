# <span style="color:orange">Lecture overview</span>

Welcome to this exciting section of our course, where we'll dive into the world of task queuing and background processing by integrating Celery with our Django application. Celery is a powerful and widely used distributed task queue that enhances the performance and scalability of web applications. In this section, we'll learn how to set up and configure Celery to efficiently handle asynchronous tasks in the background, providing a smooth and responsive user experience.

Introduction to Celery: 

We'll start by understanding the core concepts of Celery and its role in task queuing and background processing. You'll learn why Celery is a popular choice for handling time-consuming tasks, such as sending emails, processing large data, and more.

Setting Up Celery in Django: 

We'll explore the necessary steps to integrate Celery with our existing Django application. This includes installing Celery, defining the required settings, and configuring Celery to use the Redis message broker for communication between the Django app and Celery workers.

Enhancing Docker Compose: 

As we delve deeper into our app's infrastructure, we'll adjust our existing Docker Compose file to include necessary components for Celery, such as Redis (as the message broker), Celery workers, Celery beat (for periodic tasks), and Flower (for monitoring Celery tasks).

Configuring Celery Beat:

We'll focus on setting up Celery beat to schedule and manage periodic tasks within our Django application. This includes configuring periodic task schedules and observing how Celery beat interacts with Celery workers to execute these tasks.

Monitoring Celery Tasks with Flower: 

To gain insights into the Celery tasks' status and performance, we'll integrate Flower, a web-based monitoring tool for Celery. You'll learn how to use Flower to monitor task progress, view statistics, and troubleshoot issues during development and production.

By the end of this section, you'll have successfully integrated Celery into your Django application, empowering it to handle asynchronous tasks efficiently and scale with ease. The Docker Compose adjustments will ensure that your application's infrastructure is ready to support Celery and its related components seamlessly.

Get ready to enhance your Django app's performance and responsiveness, allowing it to tackle time-consuming tasks without hindering user experience. Let's embark on the journey of integrating Celery and unleashing the true potential of your web application!

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/20/files).


***
***