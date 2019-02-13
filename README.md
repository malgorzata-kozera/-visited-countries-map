# Visited Countries Map Creator

Here you can create your personalized travel map -with all your visited countries around the world.

I created this web app as a hobby project.I was traveling around the world for last 2 years, I always wanted to have a tool that allows me to check how far I have been and how many pieces of the world I visited already.I know there is a lot of that kind of websites on the internet, but i wanted to make my own, just like I wanted !

## Technology Stack:
-	Python/Django
-	HTML5/CSS/Bootstrap4
-	JSON, folium

## Sources
-	JSON files which I was using during the Udemy Course.  
- JSON file which I found [here](https://github.com/samayo/country-json)

## Creating this web app I used following modules and packages:

Folium:
I used it for creating a two maps, one of them is static and its generated when you click on Create Map, and the other one is dynamic, when user chooses visited countries form the checkbox it will appear on the other site - Created Map.  

JSON:
I used json to read coutry_by_continent.json and the geoJson to read 'world.json'. From the first one i took the countries and continents names for creating a form. 
From the second one I took a coordinates for each country, then I compared it with form values and then I used it for coloring map.

django_social_share:

I used it for making a template tags for 'Share this on Facebook'.

![ss1](https://user-images.githubusercontent.com/47001087/52181736-b34ab800-27f5-11e9-9f58-a6a608152ccb.png)


![ss2](https://user-images.githubusercontent.com/47001087/52181760-f442cc80-27f5-11e9-91b8-1e317415a020.png)

## Improvement
I share this project because I think that done is better than perfect.
Nevertheless, there is still a few thing that I would like to improve in the future, for example I would like to add:
-users account where you will be able to update your map,
-some statistic,
-the ability to mark places that are worth visiting etc.
And if you find any bugs in the program, or have a few suggestions for improvements please let me know.
