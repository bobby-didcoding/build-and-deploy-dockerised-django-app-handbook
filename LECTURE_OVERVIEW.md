# <span style="color:orange">Lecture overview</span>

Welcome to the next phase of our course, where we embark on the journey of integrating Stripe webhooks into our Django application, enabling real-time communication between Stripe and our platform. Webhooks play a crucial role in keeping our application up-to-date with events and actions occurring within the Stripe ecosystem. In this section, we will focus on wiring up Stripe webhooks locally, ensuring that our application responds promptly to important events and updates from Stripe.

Understanding Webhooks: 

We'll start by gaining a comprehensive understanding of what webhooks are and how they function. You'll learn about the significance of using webhooks in modern web applications, particularly when dealing with real-time updates and event-driven architectures.

Setting up Stripe Webhooks: 

We'll guide you through the process of configuring Stripe webhooks within your Django application. This will involve creating a specific endpoint dedicated to handling incoming webhook events from Stripe.

Writing Webhook Listeners: 

To process the incoming webhook events effectively, we will build webhook listeners in Python. These listeners will interpret the events received from Stripe and execute the necessary actions in our application based on the event type.

Securing Webhook Endpoints: 

Webhook security is of paramount importance to prevent unauthorized access and ensure data integrity. We'll explore best practices for securing our webhook endpoint and validating incoming webhook payloads.

Introduction to Stripe-CLI and Docker: 

As we gear up for deploying our application to production, we will also learn about the Stripe Command-Line Interface (CLI) and how it simplifies webhook testing. Additionally, we'll integrate a new container in our existing Docker setup, incorporating the stripe-cli image to facilitate local webhook testing and debugging.

Building a Docker Container with Stripe-CLI: 

We will provide a step-by-step guide on creating a new Docker container specifically designed for running the stripe-cli tool. This container will streamline the process of testing and monitoring webhook events during the development phase.

By the end of this section, you'll have a fully functional Stripe webhooks integration within your Django application. You'll understand the significance of real-time updates and how to handle webhook events securely. Moreover, you'll be equipped with the knowledge to set up a Docker container with the stripe-cli image, streamlining the testing process and facilitating smooth local webhook integration.

As we progress further in the course, you'll be well-prepared to deploy your application to a production environment with confidence, knowing that your Stripe webhooks integration is robust, reliable, and capable of delivering an exceptional user experience. Let's dive in and unlock the potential of real-time communication between your Django app and Stripe!

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/18/files).


***
***