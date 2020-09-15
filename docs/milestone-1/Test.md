# Milestone 1. Project Plan Complete - Test

## PROJECT INFO
- [Software Project Plan - Twitter Clone](https://github.com/maknop/twitter-clone-api)
- Other Roles - [Requirements.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Requirements.md), 
                [Design.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Design.md), 
                [Code.md](https://github.com/maknop/twitter-clone-api/edit/master/docs/milestone-1/Code.md), 
                [Test.md](https://github.com/maknop/twitter-clone-api/blob/master/docs/milestone-1/Test.md)
- File: Milestone-1/Code.md
- URL: https://github.com/maknop/twitter-clone-api/edit/master/docs/milestone-1/Code.md
- Git Repo: twitter-clone-api


Role: QA Engineer - Test

Goal: Test Plan

**Outline of testing that will be used**
 Testing will be done every time we work on the project. We will be using GitHub and Python for testing services. Testing will be done essentially when the group meets. We will be
 incoorperating some of the testing from the test level hierarchy. We will most likely use each level of the hierarchy, bur for now testing will include manual acceptance testing,
 quick development tests, and page tests. We will do more testing in the future when we get further along on our project. 

**Setup structure for testing**
Structure for testing will be working on our local machines, pushing up the changes that we have made, then determining if those changes still need imporvement. This process will
be repeated and we will probably take turns on testing. We might split the team up and have two people work on testing while the other two continue to work on progress of the
overall project.

**Log issues**
 Each time that an issue is encountered, the team will attempt to fix the problem. Each problem that the team comes in contact with, will be documented with a date, and a 
 description of what the issue is. If the team happens to find any useful resources on how to fix an issue, those resources will be documented for future use. 

**Document how to log issues**
 We will create a spreadsheet or a sharred doc that we can all contribute to, then we will go and research how to fix the issues, along with making notes as to when that issue
 came up and when it was completed. If we happen to run into similar issues or problems we will already have them doccumented. 
 
 
 
 **Testing Levels**
This is just a general idea of what testing will look like.

**Level 1 - Test Plan**
* High level discussion of testing strategy
* Outline the major types of testing that will be done
  * Manual Acceptance Testing - A person uses the application and observes what happens. The test script describes scenarios that the tester must go through.
* Django unit test - Automatic tests that may start with a blank database. These tests can be very fine grained or run the entire system.
* Hammer test - These tests execute automatic scenarios that exercise the entire system.
* Quick test - The test is only used during development to iterate on a single function.
* Page test - This test runs on “requests” Python package and gets web pages from a live server it is used to see if pages on the internet are changing.
* Selenium Page test - Firefox and Chrome are used to obtain pages and look for specific HTML elements.

Twitter clone testing

Essential testing will include
* Manual Acceptance Testing
* Quick Tests in development
* Page Tests (using "requests" Python package on PyTest)

**Level 2 - Test Area**
This level outlines the testing that will occur on each major block of functionality.
* Product subsystems
* Views
* Database
* Order processing
* User accounts
* User passwords
* Reports
* Diagnostics

**Level 3 - User Story Test**
* Each Test Area is decomposed into a number of User Stories.
* Each User Story is defined as a User Experience (UX) that is documented in the requirements
* A User Story Test outlines how the UX scenario will be exercised and verified
* Examples: Student Auth UX, Create New Book UX, Register Student Grade UX

**Level 4 - Test Script**
Each User Story is decomposed into a number of User Scenarios.
A Test Script outlines how the User Scenario will be exercised and verified.
Examples: User Auth UX
* user can register new twitter account
* user can login
* user can logout
* Users can see modify their accounts (change password, username, date of birth...)

**Level 5 - Test Case**
Each User Scenarios is decomposed into a number of specific features that the app implements.
A Test Case outlines specific behavior to be exercised and what the expected results are.
Examples: users can register
* Successful registration
* Error for bad email, name, or already enrolled
user can login after registering

