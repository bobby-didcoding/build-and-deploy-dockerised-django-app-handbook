# <span style="color:orange">Lecture overview</span>

In this section of the course, we will delve into the exciting world of integrating the Stripe API with our Django application. Building on the Django app we have already developed, we are ready to take it to the next level by seamlessly connecting our platform with the powerful features provided by Stripe's payment processing capabilities.

Throughout this section, we will be utilizing the Stripe SDK (Software Development Kit) to build an efficient and robust connector that enables smooth data synchronization between our application and the Stripe payment gateway. This integration will pave the way for seamless payment processing, allowing our users to perform secure transactions on our platform with ease.

The primary objective of this section is to create well-structured and reusable endpoint classes that can be seamlessly incorporated across our project. By doing so, we ensure that any interactions with the Stripe API are centralized and optimized, promoting maintainability and reducing redundancy within our codebase.

Introduction to the Stripe API: 

We will begin by understanding the fundamentals of the Stripe API and its capabilities. We'll explore the various features that Stripe offers, such as processing payments, handling refunds, managing customer data, and more.

Setting Up the Stripe SDK: 

Before diving into the implementation, we need to configure the Stripe SDK within our Django app. We'll cover the necessary steps to set up the SDK properly and authenticate with the Stripe API securely.

Building Endpoint Classes: 

One of the core aspects of this section is to create endpoint classes responsible for communicating with the Stripe API. We'll design these classes in a modular and reusable manner, allowing us to easily extend functionality and accommodate future updates to the Stripe API.

Invoice Creation and E-commerce Signal: 

We'll focus on integrating the Stripe invoice creation process with our existing e-commerce functionality. By doing so, we can automatically generate invoices in Stripe whenever a user completes a purchase on our platform.

Webhooks Setup (Upcoming Section): 

As we progress, we'll be discussing the importance of webhooks and their role in keeping our application synchronized with events on Stripe. We'll touch upon what webhooks are, how they work, and prepare for their implementation in the next section.

By the end of this section, you will have a comprehensive understanding of how to seamlessly integrate the Stripe API into your Django application. You'll be equipped with reusable endpoint classes and a well-organized structure to handle Stripe-related operations efficiently. Moreover, you'll be ready to take on the next section, where we will explore webhooks and complete the integration loop, enabling our application to stay updated with real-time events from Stripe. Get ready to elevate your application's capabilities and offer a smooth payment experience to your users!

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/17/files).


***
***