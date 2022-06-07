# DevOps-Testing-Pipeline

This is a simple Todo Demo App devoleped by Flask and sqlite3 as DB, tested on diffrent levels then deployed in an ECS service.

## App Quick Overview

This is the main UI of the app: 

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/app1.png" />

with a modal for adding a task

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/app2.png" />

The Todo App counts the number of tasks and based on that number sends a motivational message to the user.


## App Software Testing 

In this part we'll be talking about all test levels runed on the App:

### Unit Tests

These tests are a type of software testing where individual units or components of a software are tested.
Test File: ```/tests/unit_test_app.py```
<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/unit3.png" />

In this part we have two classes:
- ```LabelCountTest``` : tests all motivational messages cases
- ```TaskTest``` : tests the integrity of the first test in the DB

The successful test results after running ```python -m unittest tests/unit_test_app.py``` :

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/unit1.png" />

The failing test when changing a wrong input to the test :


<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/unit2.png" />

### Integration Tests

Integration Testing is defined as a type of testing where software modules are integrated logically and tested as a group. In this app we are going to test The integration of Flask with sqlite3 DB.

Test File: ```/tests/integration_test_app.py```

In this part we tested the app routes( POST, GET, DELETE ):

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/integration4.png" />

- App Status before running the integration tests: The DB is intially empty:

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/integration1.png" />

- App Status after running  the integartion tests: The DB contains new tasks:

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/integration3.png" />

- The test results after running ```pytest -vvv --cov=app tests/``` in order to calculate the coverage :

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/integration2.png" />

### E2E Tests

End to end testing refers to a software testing method that involves testing an application's workflow from beginning to end. This method basically aims to replicate real user scenarios so that the system can be validated for integration and data integrity.

Tets File: ```/cypress/integration/scrap.spec.js```

In this part we tested two scenarios:

- First scenario: The user adds a new task

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/task1.png" />

- Second scenario: The user removes a task

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/task2.png" />

The App Status before running the scenarios:

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/e2e1.png" />

The App Status after running the scenarios:

<img src= "https://github.com/oumaima-kboubi/DevOps-Testing-Pipeline/blob/main/readme%20images/e2e2.png" />

The Todo ```Learn Cypress``` in the item id 25 is miswriten. This Todo will be deleted and the ```Learn AWS ECS``` todo example is inserted.


## DevOps CI/CD pipeline

