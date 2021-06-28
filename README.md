# QA-Project-1

### Introduction

The brief for this project was to make an application with CRUD functionality, more specifically:

* To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

Therefor the project can be borken down into the following steps in order to achieve the MVP:

* CRUD Functionality
* Website for application
* Relational Databases
* Risk Assessment
* Trello Board
* Automated Tests
* Implimented into github

To meet these requirements I have decided to make a digital library to store all of the books I am reading and have read. I chose this as it can easily meet the requirements of the brief and is something I would actually use becasue I currently store the same thing on a notepad.

I will have CRUD functionality as follows:

### Create

Adding a new book to the database
This Includes:
* The title
* Authors Name
* Genre
* Description
* If I have finished the book

### Read

View all books in the database on the Home page
This Includes:
* The title
* Authors Name
* Genre
* Description

### Update

Update an already existing entry in the database
This Includes:
* The title
* Authors Name
* Genre
* Description

### Delete

Delete an enrty from the database
This Includes:
* The title
* Authors Name
* Genre
* Description

### Risk Assessment

Below you can see a detailed risk assessment. I have considered a number of risks, implemented control measures for them and them reassessed the risks once the control measures were implemented.

[Risk Assessment](https://docs.google.com/spreadsheets/d/1Els0IhvIn0-xnTpcvDZE9XEy2f0RvkORjh4l8I4zCwk/edit?usp=sharing)

### Trello Board

Here is a link to my trello board, using user stories and the AGILE framework I have created and completes a Sprint Backlog to meet all of the requirements of the MVP.

![image](https://user-images.githubusercontent.com/84939917/123613151-1a200000-d7fb-11eb-85b6-3e15e1c526d9.png)

[Trello Board](https://trello.com/b/68gLnA9e/fundamentl-project-board)

### Entity Relationship Diagram

Entity Relationship diagrams are very important as they show a clear barebones look at the database structure and all of the relationships that come along with it. It is really useful to be able to visually see what the tables should look like and what their relationships should be, especially when working in a team with more than just one person where everyone needs to be on the same page about all the talbes and they are not something you see from the front end.

Fof this project I decided to go with 2 tables sharing a one-to-many relationship, as this meets the requirements of the brief and the MVP. It fulfills my needs best for my library.

![image](https://user-images.githubusercontent.com/84939917/123616149-e72b3b80-d7fd-11eb-9214-cbb25abf81a8.png)

[Entitly Relationship Diagram](https://drive.google.com/file/d/1Z8poJ_Y5NAN_JWWvinD_sycOGHJPtdQj/view?usp=sharing)

### Testing

Testing is arguably the most important part of the application for two reasons:
1. Even if you code a feature it doesn't matter unless that feature actually works as you intended it too.
2. Without testing there would be no way of knowing if changes made to any part of the application would break something without going to the application and manually inputing a lot of commands to make sure things work and or still work

I used 2 types of testing for my application:

* Unit Testing
* Integration Testing

We can use a python module called pytest in order to run all of out tests for us whenever we want to. This combined with Jenkins (that we will talk about later) we are able to automate the running of all of our tests to whenever we push changes to our application.

Pytest also has another really useful feature called coverage. Using the command:

pytest --cov=application

This provides us with a breakdown with a percentage for each file in our application. The percentage corresponds to the percentage of the total lines of code that are being tested by the tests pytest just ran. This allows you to ensure that you are testing all of the functionality that you require.

![image](https://user-images.githubusercontent.com/84939917/123613485-5fdcc880-d7fb-11eb-9021-c2faad59f2c3.png)

For example this is my coverage for me unit testing, as you can see we cover almost 100% of the application with very few gaps. This means that we can be pretty certain that the application does what we intended otherwise the tests would have failed.

[HTML Reports for my Testing](https://docs.google.com/document/d/1YAKp_hAJz4ABqVxzAqSkmKuTVh7XesxJ75Xgr3fj0JY/edit?usp=sharing)

### Front End

The front end design is very minimal, it serves only one purpose, functionallity. The brief only requires that the front end be stable and functional. I have added a couple of links to redirect you to the home page and the page to add a new book. All books in the database would be displayed here along with the author's name, genre, and a short description of the book. There are currently no books in the database so the page appears empty.

![empty home page](https://user-images.githubusercontent.com/84939917/123612881-d9c08200-d7fa-11eb-9523-24ba19ebaffc.png)

We use a form to add a new book to the database, this form can be accessed using the link at the top of the page or through navigating your way to '/add' in the URL.
This form uses string, textarea, select and submit fields as they were the best fit for each of the fields. The submit button is labeled 'Add a new book to the database'.

The advantage of using a textarea field instead of a string field is that it is resizable so you can see the whole description at once and the box will underline any spelling errors it sees. This is not really required for the title and such as they are more likely to be single words, phrases or names and so are easier to check or are more likely to flag a spelling error even when spelt corrently.

![image](https://user-images.githubusercontent.com/84939917/123614812-9404b900-d7fc-11eb-9451-fbdbb07dc530.png)

Let us add this book to the database as a test to see what the home page looks like with a book added.

![image](https://user-images.githubusercontent.com/84939917/123615683-71bf6b00-d7fd-11eb-8814-daf84cc96000.png)

Once the submit button is clicked the user is instantly redirected back the the homepage with the new genre added and the book listed underneath.

![image](https://user-images.githubusercontent.com/84939917/123615841-961b4780-d7fd-11eb-81c7-4b010d0d32ed.png)

To update this entry we simple go to '/update/title' (where title is the title of the book)

![image](https://user-images.githubusercontent.com/84939917/123616434-2f4a5e00-d7fe-11eb-84d2-28d3be8ed35f.png)

We have the same form as on the create page except all of the values given here will replace the existing values for this book

![image](https://user-images.githubusercontent.com/84939917/123616968-b26bb400-d7fe-11eb-9fce-edf0339be6b5.png)

Here we are going to change the title, author and the description of the book

![image](https://user-images.githubusercontent.com/84939917/123617026-c0b9d000-d7fe-11eb-8bd5-76a8849344c1.png)

We are once again redirected to the home page on clicking the submit button and there you can see the updated entry for the book.

By adding '/delete/title' (again the title is the title of the book to be deleted) to the URL we are able to remove a book for the database.

![image](https://user-images.githubusercontent.com/84939917/123618073-c368f500-d7ff-11eb-93bc-b141118d3070.png)

To wrap up the front end, this is where large quality of life improvments could be made given time dedicated to them. For example linking directly from the name of the book on the home page to the update page, and a delete button on the home page for wach book with conformation requirement. Graphics and art so it isnt just a white page with black text, images of the cover of the book or a notable image from the book. These were npot required in the brief and were not the focus or gaol of this project and so no time was given to them.

### Jenkins and automated testing

As mentioned in the testing section we can use Jenkins to run out pytest commands and perform our tests for us. We can use a webhook to connect out github repository to our jenkins build, therefore we can set jenking to run our tests whenever we push new changes up to GitHub












### Authors

Henry Wright
