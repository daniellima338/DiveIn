# **Into The Wild**

![Mokeup Image](assets/images/mock-up.png)

## **Goal for this project** 
Into The Wild is a fun an challenging quiz game with focus on Animals.  The questions will be of varied difficulty. See if you can hit the top of the list! 

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
 I have visited [Google Fonts](https://fonts.google.com/ "Google Fonts") to explore the various options. The fonts used in this project are [Ubuntu] (https://fonts.google.com/specimen/Ubuntu?query=Ubuntu) in different sizes depending on the importance of the text. The font have a light readthrough and do not come of as strong to the eye. It goes well in line with the design of the webiste.

### Icons
I have used icons from the [Font Awesome library](https://fontawesome.com/ "Font Awesome"). There is a limited amount of icons. But they fit the corresponding text. 

### Colors

You can view my color scheme [here](assets/images/colors.png)

![Color Scheme](assets/images/colors.png)

The feel of the website should give you a feeling of the sensation of diving. 

* #0168C5: Is the primary background color. Many images will be used as backgrounds, but in places where there is not a picture as background, this soft blue color will do. 

* #1B442A: Is a much darker Blue color. It will be used as a divider throughout the page. 

* #f3fff3: Is a smooth Light-blue color. It will be used to highlight buttons around the website.

* #A8F1B8: Is a smooth Grey color. It will be used as overlay in different places. 

* #D82929: This is a plain White color. it will be used as text, to provide good contrast to the Dark-blue color used as background. 

I have used contract checker on Coolors in order to make sure that the contract is sufficient.
In this way my content will be easily readable. 

#### Changes made to color scheme

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Structure**
The website structure is built with [Materialize](https://materializecss.com/).
Materialize provides content for both CSS and JavaScript, as functionality with both is important.
As Materialize is designed for mobile first, I will be certain that my website functions well on mobile. 

### Home Page


### Countdown Page


### Quiz Page


### High Score 


### Tutorial



### **Wireframes**
I have decided to use [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website. 
First I created a wireframe for mobile, as the approach is mobile first. Thereafter wireframes for desktop and tablets. 


You can find my wireframes below:

#### Desktop Wireframes 
* [Home page](wireframes/desktop/home-page.png)
* [Quiz page](wireframes/desktop/play-page.png)
* [Tutorial page](wireframes/desktop/tutorial-page.png)
* [Countdown page](wireframes/desktop/countdown-page.png)
* [Contact page](wireframes/desktop/contact-page.png)

#### Tablet Wireframes
* [Home page](wireframes/tablet/tablet-home-page.png)
* [Quiz page](wireframes/tablet/tablet-play-page.png)
* [Tutorial page](wireframes/tablet/tablet-tutorial-page.png)
* [Countdown page](wireframes/tablet/tablet-countdown-page.png)
* [Contact page](wireframes/tablet/tablet-contact-page.png)

#### Mobile Wireframes 
* [Home page](wireframes/mobile/mobile-home-page.png)
* [Quiz page](wireframes/mobile/mobile-play-page.png)
* [Tutorial page](wireframes/mobile/mobile-tutorial-page.png)
* [Countdown page](wireframes/mobile/mobile-countdown-page.png)
* [Contact page](wireframes/mobile/mobile-contact-page.png)

### Features to be implemented

* A brief description of each correct answer. 
* A motion into the jungle effect. 

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Technologies used**

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Libraries & Frameworks

* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [Jquery](https://jquery.com/)

### Tools
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Some bugs and warnings occure due to bootstrap. 

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Testing**

#### User story: As a user I want to be entertained by the game I am playing.
* **Plan**
The plan is to make a game that recreates a feeling of going into the jungle. The user needs to get a feeling that they have to be experts about animals to survive. The page has to be easy to navigate, and the game has to be easy to understand. If that is all achieved the user should have a good experience. 

* **Implementation**
The implimentation is setup using a easy navigation system, where it is only possible to go very few roads from the menu. All ways are leading to the beginning of the game. The ideale route should be for the user to read the tutorial first and then play the game. But it should also be possible to play the game without reading the tutorial

* **Test**    
I had 3 people play the game. All of them wanted to play the game again, as they wanted to beat the score they had gotten before. The easy way through the game, made it easy for the users to understand what they should do, and they understood that it was a quiz game. 1 person had a hard time understanding why he died, as he didn't understand he had 4 lives. That maybe has to be clearer. 

* **Result**  
The users felt entertained and they wanted to play again. A single user did not understand how the game worked, and the progressionbar has to be more clear. 

* **Verdict**  
The game almost passed the userbility test according to the user story. Small changes has to be implimented. 


#### User story: As a user I want to be able to see how well I did compared to others.
* **Plan** 
The user has to be able to see their score against other users. Here the user has to be able to put in their name and pin their score to a highscore board. 

* **Implementation**  
The user will see a modal when they finish the game. Here the user will be able to put in their name and then save their score to the highscore board. If they wish to not save their score, they can just play the game again. 

* **Test** 
3 users tested the highscore function and all went through the functionality without issues.

* **Result** 
the 3 users tested the game and were all able to put in their score. They found the functionality very easily navigated and they didn't have any issues. 1 user noted that their score was not saved, when they played the game on different devices. That is because it is stored localy. For a future update the score will be stored at a database, but for the moment a local storage is what is available. 
* **Verdict** 
The test has passed all the criteria and works like planned.

#### User story: As a user I want to be able to learn new things, by playing the game.
* **Plan** 
The user is supposed to play the game many times to remember the right answers as they go. I expect the user to get some answers right and some wrong, and therefore having to play the game again. 

* **Implementation**
The user will be shown a red button when they answer wrong and a green when they answer right. It is liberatly that the user is not shown the right answer after they get a wrong answer, as they can then play the game more time. 

* **Test**  
The test the users will go through have to do with the users wanting to play the game again and not asking why they don't see the right answer after answering wrong. 

* **Result** 
 3 users tested the functionality of the game, and did not comment on why they didn't see the right answer after they answered wrong. On the other hand they wanted to play again, and therefore the idea of the game works. The users then get knowledge by repeating the game many times. 

* **Verdict**  
The test has passed all the criteria and works like planned.
 

#### User story: As a user I want to be able to contact the owner, if i have anything to ask about.
* **Plan** 
The plan is for the user to be able to contact the owner through a form if they go to the contact page. The contact page is not supposed to be very visible, as it is not a huge part of the application. 

* **Implementation**  
The user can navigate to the contact form through the footer. Here they will arrive at a form they have to fill out. The form is set up with EmailJS and I will recieve any question they ask along with the email it is send from. 

* **Test** 
The user had to navigate to the contact form and send an email without help.

* **Result** 
The 3 users that tested the app had no issues finding the navigation to the form, and send and email on without issues. 
* **Verdict**     
The user was successfully able to send emails to the email set up to recieve. 

### **Bugs**

### Answer 4 was not displaying due to a bug in the loop interating through the questions. Fixed it by starting the loop at 1 instead of 0. 
* **Solution** 
* Fixed it by starting the loop at 1 instead of 0.

### Could not change anything within the modal for the tutorial.
* **Solution** 
* Used !important to make my custom style a priority. tried other solutions, but this was the only one that worked. 

### The highscore was not displaying on the highscore tab
* **Solution** 
* There was an error in the class of the highscore. when fixed the score displayed as expected.

### quotation-marks in the question were rendered as &quote. 
* **Solution** 
* Changed the rendering from JS to HTML and then it was fixed.

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Deployment**

I deployed my Ways project website in the following way:

* Logged in to my GitHub account and locating my repository
* Clicked on the settings icon (near the top right of the page)
* Scrolled down the page to locate the 'GitHub Pages' section
* Under "Source", select "Master" in the dropdown menu.
* In the tab next to "Source", select "/root" if not already selected by default
* Click save then the page will automatically refresh.
* The link should show in a banner just above "GitHub Pages" section.
* This deployed my project to the URL: (https://daniellima338.github.io/Into_The_Wild/)

[Back to Top](#table-of-contents)

<a></a>
--- 

## **Credits**
I have drawn much inspiration from different posts on Stackoverflow. Credit is also given to [Michael Karen](https://michael-karen.medium.com/how-to-save-high-scores-in-local-storage-7860baca9d68), whom i have drawn inspiration from to the functionality of the highscore page. 

### **Acknowledgements**
I want to thank the 3 people who tested the game(Kasper, René and Christina). They gave valuable feedback to optimize the game. 

[Back to Top](#table-of-contents)

<a></a>
