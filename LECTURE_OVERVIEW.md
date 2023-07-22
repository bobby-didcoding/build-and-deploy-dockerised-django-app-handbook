# <span style="color:orange">Lecture overview</span>

Welcome to the next video lecture in our course! Building upon the foundational knowledge from the previous lectures, this session focuses on an often overlooked yet crucial aspect of web application development: how to make our app deployable.

In this video, we delve into the process of making our Django application deployable, starting from either the main branch or a new branch in the GitHub repository. You have the flexibility to either make the necessary changes directly in the main branch or clone down the new branch, depending on your preference and workflow.

Throughout the video, we methodically walk you through the essential changes that are required. One of the key aspects we address is the management of environment-specific settings. While the standard settings.py file may work in production environments, it can become unwieldy and difficult to maintain with multiple if-else statements. To address this, we explore the concept of a common settings file that is inherited by environment-specific setting files, promoting cleaner code and easier maintenance.

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/1/files).


***
***