# **DiveIn**

![Mokeup Image](assets/images/mock-up.png)

## **Goal for this project** 
DiveIn is a webstie for divers. Here you can find information about awesome dive spots around the world. But not only ccan you find information, you can also rate dives yourself, as well as add a dive spot to the given country. 

Thank you for visiting my project!
If you have any feedback or questions, head over to my GitHub contact details and feel free to reach out to me.

---



## Table of contents 


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



## **UX**

### **User Stories**

#### User
* As a user I want to be able to find new diving spots
* As a user I want to be able to showcase my own diving experiences
* As a user I want to se other peoples diving experiences
* As a user I want to be able understand what the website is about very quickly

#### Owner
* As a owner I want people to use the Google diving map to find new diving experiences.
* As a owner I want people to sign up as users and populate the website with diving spots.
* As a owner I want the users to quickly be able to navigate through the site.
* As a owner I want to expand the userbase by giving the user interactive solutions on the website.

#### User Expectations
* Easy to navigate.
* Flow of the sign up process takes a short time.
* Understand the purpose of the webiste within a short time.
* Find usefull information within the topic of diving.

[Back to Top](#table-of-contents)
<a></a>
--- 

## **Design Choices**

### Fonts
 I have visited [Google Fonts](https://fonts.google.com/ "Google Fonts") to explore the various options. The font i use in this project are [Lobster] (https://fonts.google.com/specimen/Lobster#standard-styles). The font is italic as has a wavy look, which fits well with the diving theme. 

### Icons
I have used icons from the [Font Awesome library](https://fontawesome.com/ "Font Awesome"). There is a limited amount of icons. But they fit the corresponding text. 

### Colors

You can view my color scheme [here](static/Images/colors.png)

![Color Scheme](assets/images/colors.png)

The feel of the website should give you a feeling of the sensation of diving. 

* #fff: Is the primary background color. Many images will be used as backgrounds, but in places where there is not a picture as background, white will be applied.

* #1B1464: Is a smooth dark blue color. It will be used as the primary text color throughout the project.

* #A3DEFF: Is a smooth Light-blue color. It will be used as the dividing color throughout the page. 

* #212529: Is a dark green color. It will be used as overlay in different places. 

I have used contract checker on Coolors in order to make sure that the contract is sufficient.
In this way my content will be easily readable. 

#### Changes made to color scheme

I changed the colors from the original outlook, as i think the new colors suit the project better. initially i was thinking of having a blue background and white text, but i came to realize that a white background is more elegant, and the blue text fits very well on it. 

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Structure**
The website structure is built with [Bootstrap](https://getbootstrap.com/).
Bootstrap provides content for both CSS and JavaScript, as functionality with both is important.
As Bootstrap is designed for mobile first, I will be certain that my website functions well on mobile. 

### Home Page
The home page has two functionalities. The most important functionality is the login function. Besides the login function, it is also possible to view the world map and all the dives people add over time. It is kept fairly simple, so the users won't have to many options.

### Dive Destinations Page
Arguably this is the most important page of the project. This is where everyone can go in and read about the different dive sites around the world. All of the entries will be written by users, and you can get a clearer idea to how people experience dive spots. 

### Dive Map Page
The Dive map page essentially has the same functionality as the Map on the home page provides. But here the users will be able to focus solely on the dive map. This is a feature and site that stills needs work. 

### Profile Page
At the profile page the user will be able to add a new dive or edit the dives they have already uploaded. They can also erase dives, if they do not want them anymore. Functionality to edit username and password will be added at a future update. 

### Add Dive Page
The Add Dive page is essentially a form the user fills. Here they put in continent, country, place, description and image of the place. This information is then used to display the dive on the dive destination page. 

### Registration Page
The registration page is very simple. You just put in a username and password. Then the user is created if the username is not used by others. 



### **Wireframes**
I have decided to use [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website. 
First I created a wireframe for mobile, as the approach is mobile first. Thereafter wireframes for desktop and tablets. 

### Changes made to wireframes
The initial feel of the website did not feel great, and functionality was hard to produce. So many changes have been made to the wireframes. The home page now contains a login field as the first eye catching thing. Then there is a dive map under. The profile page only contains the dives the user have added, to keep it simple and smooth. The registration page have been simplified to just match the login, and now you just put in a username and password. Login page and country pages have been erased, as they were not needed in the new format. 


You can find my wireframes below:

#### Desktop Wireframes 
* [Home Page](wireframes/desktop/Desktop_home_page.png)
* [Dive Destination page](wireframes/desktop/Desktop_dive_destinations.png)
* [Country page](wireframes/desktop/Desktop_country_page.png)
* [Profile page](wireframes/desktop/Desktop_profile_page.png)
* [Register page](wireframes/desktop/Desktop_register.png)
* [Login page](wireframes/desktop/Desktop_login.png)
* [Add Dive page](wireframes/desktop/Desktop_add_dive_page.png)

#### Tablet Wireframes
* [Home Page](wireframes/tablet/Tablet_home_page.png)
* [Dive Destination page](wireframes/tablet/Tablet_dive_destinations.png)
* [Country page](wireframes/tablet/Tablet_country_page.png)
* [Profile page](wireframes/tablet/Tablet_profile_page.png)
* [Register page](wireframes/tablet/Tablet_register.png)
* [Login page](wireframes/tablet/Tablet_login.png)
* [Add Dive page](wireframes/tablet/Tablet_add_dive_page.png)

#### Mobile Wireframes 
* [Home Page](wireframes/mobile/Mobile_home_page.png)
* [Dive Destination page](wireframes/mobile/Mobile_dive_destinations.png)
* [Country page](wireframes/mobile/Mobile_country_page.png)
* [Profile page](wireframes/mobile/Mobile_profile_page.png)
* [Register page](wireframes/mobile/Mobile_register.png)
* [Login page](wireframes/mobile/Mobile_login.png)
* [Add Dive page](wireframes/mobile/Mobile_add_dive_page.png)

### Features to be implemented

* A heatmap over where diving is good during different seasons.
* Access to store with diving gear.
* community forum, where users can discuss various subjects.

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Technologies used**

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries & Frameworks

* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [Jquery](https://jquery.com/)
* [MongoDB](https://en.wikipedia.org/wiki/MongoDB)


### Tools
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Some bugs and warnings occure due to materialize. 

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Testing**

#### User story: As a user I want to be able to find new diving spots.
* **Plan**
The plan is to give users new perspectives as to where they can travel for good diving spots. It should feel like a shot of inspiration going through the site. The search functionality has to be easy and simple. 

* **Implementation**
The user will be able to achieve this goal by going to the diving destinations page, as they can there see descriptions of other peoples dives. There they can also search for specific continents or countries, if they have something in mind. 

* **Test**    
When navigating through the site, it is easy to get to the dive destination page. From there it is easy to understand how to use the search function, as it appears in the top of the screen. 

* **Result**  
the 3 users that tested the functionality found it easy to find new inspiration about diving spots, and the navigation came very intuitive to them. 

* **Verdict**  
The test has passed all the criteria and works like planned.


#### User story: As a user I want to be able to showcase my own diving experiences.
* **Plan** 
The user should be able to put in their own experiences with diving, so they can portrait for others what they experiences in the given spot. 


* **Implementation**  
The user should easily be able to get to the Add Dive page, when they log in to their profile. From the profile page it should be simple and easy to understand what they can do. 

* **Test** 
The users should easily be able to navigate to the profile page and from there add their own dives to the database.

* **Result** 
The users that tested the page in general had an easy time getting through to the add dive page and show casing their own dive examples. One user noted that it was a bit confusing they could not add a dive from the Dive Destination page, as it came more intuitve for her. 

* **Verdict** 
The test has passed all the criteria and works like planned.

#### User story: As a user I want to se other peoples diving experiences.
* **Plan** 
The main goal for a user is to get other perspectives about diving. You have maybe read travel guides or "top 10 destinations for diving", but then want personal perspectives from other divers. 

* **Implementation**
To be able to see other peoples diving experiences, the Dive Destination page is the main functionality, as the users will be able to search for inspiration in all the posts people have done over time. 

* **Test**  
The user should navigate to the Dive Destination site, be able to search for dives and intuitively understand what they can search for. 

* **Result** 
The users that tested the page had an easy time finding the Dive Destination site. From there they were able to use the search functionality. One user had difficulties understanding the reset function.

* **Verdict**  
The test has passed all the criteria and works like planned.
 

#### User story: As a user I want to be able understand what the website is about very quickly.
* **Plan** 
As a user it is important to quickly understand what I can do on the page. Therefore navigation and goal has to be easily understood from first go.

* **Implementation**  
The navigation has been kept simple, so the user always have limited steps to take. This has been done, so the user can always easily find the information they are looking for. 
* **Test** 
the users were tasked to try and navigate through the most intuitive path for them. 
* **Result** 
The users navigated through the site without any issues. They found the navigation intuitive to use.
* **Verdict**     
The test has passed all the criteria and works like planned.

### **Bugs**

### 1 When the user uploaded a photo, the photo would not render on the page.
* **Solution** 

The solution for this project has been to use a URL. I have provided the user a website to turn a image into a direct URL link, and from there they can pass it on to the website. 

### 2

* **Solution** 


### 3
* **Solution** 


### 4
* **Solution** 


[Back to Top](#table-of-contents)

<a></a>
--- 

## **Deployment**

I deployed my project in the following way:


[Back to Top](#table-of-contents)

<a></a>
--- 

## **Credits**


### **Acknowledgements**


[Back to Top](#table-of-contents)

<a></a>
