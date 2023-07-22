# <span style="color:orange">Lecture overview</span>

In this lecture, we'll embark on the journey of building a robust Django application by creating essential models for various components. Our project will consist of four apps: ecommerce, core, tasks, and users. Each app serves a distinct purpose, contributing to the overall functionality of the web application.

Core App Models:

We begin by setting up the core app, which will serve as the foundation for our project. Here, we'll define essential models to capture crucial information. These models include:

- Blogs: Store blog posts with relevant fields like title, content, author, and publication date.

- Contact Form Information: Capture user inquiries with details like name, email, and message.

- Testimonials: Record client testimonials, including their name and feedback.

Ecommerce App Models:

Next, we'll focus on the ecommerce app, which handles product-related data and transactions. The ecommerce models include:

- Products: Store product details such as name, description, price, and inventory status.

- Invoices: Keep track of customer invoices, including associated products and payment details.

- Stripe Sessions: Record information about payment sessions, seamlessly integrating with Stripe for secure payments.

Users App and CustomUser Model:

To implement user authentication and extend the built-in user model, we'll work with the users app. Here, we'll define a custom user model (CustomUser) that allows us to add custom fields and functionalities. This ensures flexibility and scalability for user-related features in our application.

Tasks App with Celery Implementation (Later in the Course):
While we won't delve into the implementation just yet, we'll prepare the groundwork by creating the tasks app. This app will be integrated with Celery later in the course to manage background tasks and asynchronous processing effectively.

Utilizing Abstract Classes and Django Extensions:

To promote code reusability and maintain consistency, we'll create abstract classes and leverage Django extensions. Abstract classes will define common fields and behaviors shared across multiple models, reducing redundancy. Additionally, we'll utilize Django extensions to implement fields like 'status,' 'slug,' and 'created' efficiently across all models, streamlining development.

Throughout this section, you'll gain valuable insights into designing and implementing Django models for various app components, ensuring a well-structured and scalable project. By combining abstract classes, Django extensions, and custom user models, we'll create a dynamic web application with extensive capabilities, ready to meet the demands of the real-world production environment.

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/3/files).


***
***