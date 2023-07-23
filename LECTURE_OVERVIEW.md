# <span style="color:orange">Lecture overview</span>

In this lecture, we'll harness the power of Django's built-in admin UI by creating admin classes for each of the models we defined in the previous section. The Django admin is a powerful tool that allows us to perform CRUD (Create, Read, Update, Delete) operations on our database entries directly through a user-friendly browser interface.

Creating Admin Classes:

For every model we defined in the previous section, we'll create corresponding admin classes. These classes will determine how the model's data is presented and edited in the admin interface. By customizing the admin classes, we can tailor the admin UI to best suit our application's needs.

Exploring the Django Admin UI:

Before diving into customizations, we'll first explore the default Django admin UI. To access it, we'll use a Django command: 'python manage.py createsuperuser.' This command allows us to create a superuser, granting administrative privileges to access and manage the admin interface.

Registering Models with Admin Classes:

Once we've created the admin classes, we'll register each model with its corresponding admin class. This step ensures that our customizations are applied to the Django admin UI, enabling us to efficiently manage the data in our application.

Leveraging CRUD Operations:

With our admin classes in place, we'll take advantage of Django's admin UI to perform CRUD operations. We'll be able to add new entries, view existing data, update information, and delete records – all through an intuitive and user-friendly interface.

By the end of this section, you'll have a comprehensive understanding of how to wire up admin classes to leverage Django's built-in admin UI effectively. You'll be able to navigate, manage, and manipulate your application's data with ease, thanks to the powerful capabilities of Django's admin interface. With your custom admin classes in place, the admin UI will become a crucial tool for efficiently managing your web application's database and facilitating seamless interactions with your data.

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/4/files).


***
***