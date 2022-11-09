# Project Writeup and Reflection

## Project Overview
Our project has the goal of letting users find the MBTA closest stop to an input a location, and whether it is wheelchair accessible. 

To achieve this we use 2 APIs: the MAPQUEST and the MBTA one. The first enables us to find geographical coordinates from the input location, while the second retrieves the closest MBTA stop to a given pair of coordinates. Thus, we can combine them to find the transit station from a given location.

Beyond the core backend logic, we decided to store API keys in a different file and to experiment a bit with CSS in the HTML templates. 

## Project Reflection 

### i. Project Process
The backend part went out pretty smoothly. After understanding the main goal, we draw out how each function connected with each other for the bigger result (almost like pseudo-code). Then, we approached each individually, knowing exactly what the input/output should look like, and studying the necessary APIs documentations. As necessary on the way, we studied some new topics, such as how to deal with blank spaces to encode location in the URL, and how we should deal with templates and parameters for Flask.

Regarding testing, we made a rule to test each function independently, which was good. However, we were constantly revising for edge cases, even freaking out a bit because "Boston Commons" was not returning anything in the APIs. We would try to understand better the requirements and scope, specifically for range of inputs and exception handling requirements, so to better design the final application.

### ii. Team Process
First of all, we acknowledged and agreed that meeting in person was better for our learning due to faster and easier communication feedback. Thus, we decided to share the project by section - coding next to each other. While Bruno implemented the get_url and get_lat_lng functions, Luiz implemented the get_nearest_station and find_stop_near functions. And then, we decided to put everything together in the main function, while unit testing each function to make sure it matched specific requirements (format, type, accuracy, etc).

There where no issues that arose while working together, to the contrary, we actually did have a lot of fun! It was pretty great to see how we could connect APIs function by function to build something that really works, and we learned a lot (mostly reading the API documentations). 

## Team members: Luiz Spinelli and Bruno Brasil 