Today, every software system is designed as a distributed system, which includes several Tiers and in addition interfacing with cloud services.
In this project we will design and develop a system that includes a display subsystem, an application server and interfacing with selected cloud services.
The system will display a list of items of your choice (galaxies, planets, asteroids, songs, movies or foods) and will strengthen
This list includes user alerts.

In this project we will use the PyQt library and the Python language to create an integrated display of templates from the *MV family and many others
others with the aim of creating a code base allowing for extensive expansion, maintenance and testing, and with it a collection of micro-
Services using the NET.ASP Web API and #C language and a variety of other design patterns.

Requirements:
1. Only one type of user for the system:
1.1 The admin user will archive lists.
2. The system will support the following user processes:
2.1 Entering an item that includes a picture, features, keywords, description and comments.
2.2 Displaying a list of items based on keyword search.
2.3 Deleting and updating item data.
3. The list data will be saved in a database within the application server.
4. The system will call at least two cloud services to extract data (such as lists or images) or run processing
(such as calling for AI services)

![8 8 4](https://github.com/user-attachments/assets/8eb0b054-dbec-4dfe-b902-8c836890effe)
Diagram 1: List display and management system components

![8 8 4](https://github.com/user-attachments/assets/7302d66b-887e-4241-a67a-f26c147f402f)
Screen 2: An example of the Imagga service for extracting image content

![8 8 4](https://github.com/user-attachments/assets/b4f51d0f-5fbb-4db5-833a-d07b13166521)
Diagram 3: Using the CQRS template to design the application server services

Requirements:
1) Desktop application will be based on QT/Pyside and tasks will be defined based on MVC or MVP pattern.
2) The design of the display subsystem will be based on a main Shell screen that includes a menu and is divided into Functional Compartments,
Panels suitable for the task will be embedded in it subject to the Microfrontends template.
3) The application server will be based on API Web NET.ASP and Microservices templates as well as CQRS.
4) Data will be managed in a local database on the application server (Server Sql or MySql) using Entity Framework.
5) There is no need to save images, only the URL of their location can be saved.
6) In addition, the API Web NET.ASP project will serve as an API Gateway for the services in use, each service must be created
Controller separately.
7) The system will use cloud services of your choice subject to the selected topic.
8) The system will use the Imagga cloud service to analyze the content of a selected image:
Image Recognition API, Computer Vision AI – Imagga

By Eliaou Madar

The chosen theme was : Development of a recipe management system using 
Python and C#, Spoonacular API, integrating Imagga, 
ASP.NET Web API, and Entity Framework.

![8 8 1](https://github.com/user-attachments/assets/b6b882cf-8035-47d1-a91d-1fafacb20085)

![8 8 2](https://github.com/user-attachments/assets/dfeeccac-e1ad-4a7f-8438-4745392d6da5)

![8 8 3](https://github.com/user-attachments/assets/c207a734-112d-4dad-9bfc-b080d7fcc2ac)

