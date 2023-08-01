# <span style="color:orange">Lecture overview</span>

Welcome to this pivotal section of our course, where we'll embark on an exciting journey of upgrading our database to PostgreSQL, a robust and powerful relational database management system. PostgreSQL offers a wide array of advanced features and performance optimizations, making it an ideal choice for scaling and managing data-intensive applications. In addition to the PostgreSQL upgrade, we'll also implement pgAdmin, a popular administration and development platform, in our Docker Compose setup, enabling seamless management and visualization of the PostgreSQL database.

Introduction to PostgreSQL: 

We'll begin by understanding the advantages of using PostgreSQL over other database management systems. You'll learn about its advanced capabilities, including support for complex data types, ACID compliance, and extensibility.

Setting Up PostgreSQL:

We'll guide you through the installation and configuration of PostgreSQL to serve as the new database backend for our Django application. This includes creating the appropriate database and user roles to facilitate a smooth migration.

Updating Django Settings: 

As we switch to PostgreSQL, certain Django settings need to be updated to reflect the changes in the database backend. We'll modify the settings to use the PostgreSQL database engine, configure the database connection, and handle other PostgreSQL-specific settings.

Implementing pgAdmin for Database Management: 

In addition to upgrading to PostgreSQL, we'll introduce pgAdmin, a comprehensive administration and development platform, to our Docker Compose setup. We'll configure a pgAdmin container, providing a user-friendly web interface to interact with the PostgreSQL database seamlessly.

Upgrading Docker Compose: 

To accommodate the PostgreSQL and pgAdmin upgrade, we'll adjust our Docker Compose setup. This will involve configuring a new PostgreSQL container and integrating pgAdmin, providing a powerful and centralized database management solution.

By the end of this section, you'll have successfully upgraded your database to PostgreSQL, unlocking the potential of a more robust and scalable database management system. Your Django application will be equipped with PostgreSQL's advanced features and performance optimizations, ensuring a seamless and efficient data management experience. With the addition of pgAdmin, you'll have a powerful administration tool at your disposal, enabling you to visualize and manage your PostgreSQL database with ease.

Upgrading to PostgreSQL and implementing pgAdmin are crucial steps in ensuring the long-term success of your application, and this section will guide you through the migration process and database management with confidence. Let's dive into the world of PostgreSQL and elevate your database capabilities to new heights!

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/24/files).


***
***