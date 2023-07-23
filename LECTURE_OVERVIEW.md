# <span style="color:orange">Lecture overview</span>

In this lecture, we'll explore the powerful capabilities of Django signals and learn how to effectively use post_save and pre_save signals to handle the linking of models with OneToOne and ForeignKey relationships. Signals allow us to respond to certain events in the database, enabling us to execute specific logic when conditions are met.

Understanding Post_Save Signals:

We'll start by diving into post_save signals, which are triggered after a model's instance is saved to the database. We'll learn how to leverage these signals to handle automatic linking of models, ensuring consistency and accuracy in data representation. For instance, we can automatically create a user cart once the user's account is activated.

Handling Logic with Pre_Save Signals:

Next, we'll explore pre_save signals, which are triggered just before a model's instance is saved to the database. We'll discover how to use pre_save signals to check submitted data against existing records and enforce business rules. For example, we can run code to verify that certain criteria are met before activating a user's account and possibly send an email to notify them of the activation.

Linking Models with OneToOne and ForeignKey Fields:

We'll focus on linking models with OneToOne and ForeignKey relationships through signals. This technique streamlines the process of associating related data without requiring manual intervention, enhancing the efficiency and reliability of our application.

Signal Decorators and Registration:
To effectively use signals, we'll explore the concept of signal decorators and how to register them properly. This step is essential for establishing a clear and organized approach to handling various events in our Django application.

Writing Custom Signal Handlers:
In this section, we'll create custom signal handlers tailored to our specific use cases. We'll develop logic that executes when certain conditions are met, allowing us to enforce rules, perform additional actions, or validate data before saving to the database.

By the end of this section, you'll have a deep understanding of how to leverage post_save and pre_save signals to handle model linking and implement custom logic efficiently. You'll be equipped with the knowledge to manage complex interactions between models seamlessly and maintain data integrity while automating essential tasks, such as user activation, email notifications, and more. Signals serve as a powerful tool to streamline processes and ensure smooth interactions within your Django project.

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/8/files).


***
***