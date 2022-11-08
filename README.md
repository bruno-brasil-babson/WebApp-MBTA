# WebApp-MBTA
 This is the base repo for MBTA project. Please read [instructions](instructions.md). 

# Project Writeup and Reflection

## Project Overview
Our project has the goal of letting the user input a location (in number and street name format) and output the closest MBTA stop, to the inputed street, and wheter it is wheelchair accessible. 

To achieve this goal we first needed to ask for 2 API requests, the MAPQUEST and the MBTA API. Then, once given the a place name or address (by the user) we had to find such place/address coordinates, and store it into a tuple. Using these set of coordinates (lat & lng) as inputs to the get_nearest_station function, we found the nearest station and its wheel chair accessibility feature. 

Regarding the extension to the requirements, we decided some better design was need- change of font color and centralization of text. 

## Project Reflection 

### i. Project Process
We were able to work through the first and second part of the project efficiently. However, we found the first part (software builiding python part) easier to do than building the web app (second part). In fact, the bug that took a good part of our time and brain power was the rendering of the POST/nearest_mbta; we constantly got error. Looking backwards, we could have tested the web_app code as we built it, rather than only testing it in the end- we did not commit this same error in the first part, however, which might explain why we had an easier time. 

Regarding the self-studing party, both me and Bruno had to study the MapRequest and MBTA API's to understand how to better implement our functions - what's the input and output? what's our output data type? I wish we knew the value of learning about API's documentation to design the project's plan, and make a rule to unit test every few lines of code implemented.



### ii. Team Process
First of all, we acknowledged and agreed that meeting in person was better for our learning due to faster and easier communication feedback. Thus, we decided to share the project by section- coding next to each other. While Bruno implemented the get_url and get_lat_lng functions, Luiz implemented the get_nearest_station and find_stop_near functions. And then, we decided to put everything together in the main function, while unit testing each part for errors.
There where no issues that arose while working together, to the contrary, we actually did have a lot of fun. 


## Team members: Luiz Spinelli and Bruno Brasil 