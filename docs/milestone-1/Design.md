# Milestone 1. Project Plan Complete - Design
# PROJECT INFO
* [Software Project Plan - Twitter Clone](https://github.com/maknop/twitter-clone-api/blob/master/README.md)
* Other Roles - [Requirements.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Requirements.md) , [Code.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Code.md) , [Test.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Test.md)
* File: Milestone-1/Design.md
* URL: https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Design.md
* Git Repo: github.com/maknop/twitter-clone-api

## Milestone 1. Project Plan Complete
Role: Designer - Design
Goal: Technology selection
* Select Development Tools
* Infrastructure - Frameworks & Tools
* Setup Guide
* Create "Hello World"
* Decide on App deployment

## Twitter Clone - Technology selection
The technology we have chosen will allow us to deploy from any platform and pull data from a REST API. These frees us up to decided our front-end at a later date.

### Technology Alternatives
Existing Commercial Product

Twitter is the largest competitor to our clone. There are other social media platforms, but Twitter is the closest to our project.

Web Development Framework
There are many options when it comes to our web development framework.
* Ruby on Rails
* NodeJs and MongoB
* Spring Boot and MySQL or PostgreSQL
* Django and PostgreSQL or SQLite

### Select Development Tools
Criteria for Technology Selection
* Fitness of the tool for the job
* Experience of the development team with the technology
* Components that can be leverage from previous work
* Professional opinion and popularity
* Productivity benchmarks
* Security concerns
* Community of users and developers
* Existing commercial apps that use the technology
* Proof of concept (building a simple app)

After careful consideration a decision was made to create our Twitter Clone using the Django web framework which is written in the Python programming language.

Here are the most important considerations that support this decision:
* Knowledge of the language between team members.
* Ease of use and ability to get from development to production quickly.
* Documentation available.


## Infrastructure - Frameworks & Tools
Framework
* Python 3.8.5
* Django 3.1.1
* Virtual Environment
* Docker 19.03.12
* Nginx 1.18

Web hosting
* DigitalOcean

Dev Tools
* VIM
* PyCharm
* Brackets
* VSCOde
* Jenksin CICD
* PostgreSQL Database

Github
Git for version control
Github to hold the Twitter Clone repos
* twitter-clone-api - Main repo
* twitter-clone-api - API repo
* twitter-clone-frontend - Frontend repo

DigitalOcean
* Account: dougmellon
* http://159.89.135.61/

### Create "Hello World"
* [Index](http://159.89.135.61/) - This simple app ensures that all of the development tools are installed and properly configured. All developers will do this before any other work is done with the code.
* [Code Repo](https://github.com/maknop/twitter-clone-api/tree/master/twittercloneapi) - Source code for hello world.

### Decide on App deployment
* DigitalOcean (including managed datbase)
* AWS Lightsail (light version of AWS EC2 instances)

Twitter Clone has chosen to deploy to DigitalOcean. Tutorial documents are posted in our repo as well as in our personal Discord chat.
