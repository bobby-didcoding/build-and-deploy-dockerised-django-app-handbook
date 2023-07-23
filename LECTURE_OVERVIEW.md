# <span style="color:orange">Lecture overview</span>

In this lecture, we will wire up essential packages that play a crucial role in making our project function seamlessly. These packages have been carefully chosen to enhance the capabilities and performance of our Django project. We will be integrating the following packages:

- black==23.7.0
- celery==5.3.1
- django-celery-beat==2.5.0
- django-celery-results==2.5.1
- django-ckeditor==6.6.1
- django-enumfield==3.1
- django-extensions==3.2.3
- django-redis==5.3.0
- flake8==6.0.0
- flower==2.0.0
- Pillow==10.0.0
- psycopg2-binary
- python-dotenv==1.0.0
- redis==4.6.0
- requests==2.31.0
- six==1.16.0
- stripe==5.5.0
- django-debug-toolbar==4.1.0
- s3transfer==0.6.1
- sentry-sdk==1.28.1
- gunicorn==21.1.0
- boto3==1.28.5
- botocore==1.31.5
- django-storages==1.13.2

By integrating these packages, you'll unlock a wide range of functionalities, including automated code formatting (black), task queue management (Celery), and real-time monitoring of Celery tasks (django-celery-beat and django-celery-results). Additionally, you'll have access to an advanced rich text editor (django-ckeditor) and ENUM support (django-enumfield).

Other packages like django-extensions, django-redis, flake8, and Pillow will further streamline your development process, enhance caching, ensure code quality, and handle images effectively. Integrating Stripe will enable easy payment processing, while django-debug-toolbar helps in debugging and optimizing performance.

To boost scalability and reliability, we'll leverage AWS S3 storage using django-storages, with boto3 and botocore providing the necessary integration with AWS services. For error tracking, we'll implement Sentry with sentry-sdk.

Through this hands-on integration of packages, your Django project will be enriched with powerful features, setting the stage for a highly functional and efficient web application ready for production deployment.

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/2/files).


***
***