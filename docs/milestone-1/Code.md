# Milestone 1. Project Plan Complete - Code

## PROJECT INFO
- [Software Project Plan - Twitter Clone](https://github.com/maknop/twitter-clone-api)
- Other Roles - [Requirements.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Requirements.md), 
                [Design.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Design.md), 
                [Code.md](https://github.com/maknop/twitter-clone-api/edit/master/docs/milestone-1/Code.md), 
                [Test.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Test.md)
- File: Milestone-1/Code.md
- URL: https://github.com/maknop/twitter-clone-api/edit/master/docs/milestone-1/Code.md
- Git Repo: twitter-clone-api

### Milestone 1. Project Plan Complete
Role: Programmer - Code  

Goal: Version control
- Create Frontend & Backend Microservice
- Create our Server Instance

### Create Frontend & Backend Micro-service
Creating two separate repositories is to serve as two separate [microservices](https://en.wikipedia.org/wiki/Microservices) that will connect to form the application  
we are building. The first will serve as the backend which contains our [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) and Database while the other will serve 
as the frontend where we will design the user interface.

By allowing the separation of these two components we are isolating both ends of the application with all required  
dependencies. These isolated pieces will be deployed in containers that will be able to connect and transfer the necessary  
data for a fully functioning application. 

### Create our Server Instance
After choosing a hosting platform, create an instance of a server on a chosen operating system. Once that is done, the  
the application can be hosted on the server and each developer can [ssh](https://en.wikipedia.org/wiki/Secure_Shell) into the server.  

### Create "Hello, World" Django App
Since we are using the Django framework for our backend development, we added a basic "Hello, World" app that will  
we used to mold into the requirements we will need for our application. By having something as a starting point,  
we are able to create our separate endpoints and understand how those interfaces connect.

