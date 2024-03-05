# CONNECTED 

Connected is a newssite focused on articles regarding technology and internet media.
The sites maingoal is the update the user about different discoveries in subjects and categories such as:
- Artificial Intelligence
- Technological Sience
- Online Culture
- Technews
- Technological Gadgets

Connected is not only a site for news and article research, but also an online forum where the user can discuss with other users about different subjects and questions, regarding the main concept. 

This website includes a firstpage displaying the latest articles, an "About us" page, different pages for the different categories that the article is posted in, an discussion forum, and lastely their own profilepage which allow the user to see their own previously made posts and comments. 

The Connected website can be found here - [Connected.](https://connected-c643fb1afe74.herokuapp.com/).

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/amiresponsiveconnected.png)


## Table of Contents

SKRIV INNEHÅLLSFÖRTECKNING HÄR

## Site Owner Goals

- As a Site Owner I can present relevant and interesting news articles about recent discoveries or updates in the online tech world. 

- As a Site Owner I can allow the users access to the website and dicsussionforum, allowing the user to comment on different articles and discussionpost along with other users and because of that create an interactiv enviorment for who wishes to join.

- As a Site Owner I can present the user with a website that is easy to navigate, fully responsive and that contains a simple, yet beautiful layout, suitable for the websites purpose.

- As a Site Owner I can allow the user to sign up to the website and interact thorugh comments and posts. 


## User Stories

#### User Profile

- As a Site User I can register my account, allowing me to comment on existing articles and discussion posts. 

- As a Site User I can register my account, allowing me to create my own posts in the designated discussion forum. 

- As a Site User I can find all my previously made posts and comments in my own profile.

- As a Site User I can edit and delete my previously made comments and posts, even if they been approved or haven't been approved, by the site administration. 

- As a Site User I can log in or log out of my account so that I can keep my account secure.

- As a Site User I can see if I am logged in or not.

#### User Navigation

- As a Site User I can easily navigate to the home page, viewing the latest articles posted.

- As a Site User I can easily navigate to a page regarding a specific category containing the relevant articles.

- As a Site User I can easily find information about the website and the websites purpose.

- As a Site User I can navigate to the online forum allowing me to interact with other users on relevant topics. 

- As a Site User I can easily sign up, log in and log out.

#### Site Administration

- As a Site Administrator I can easily update the website with new articles and associated images.

- As a Site Administrator I can manually approve the users comments before the site users can view them, in order to secure that all the content is relevant and following the websites guidelines.

- As a Site Administrator I can manually approve the users posts before the site users can view them, in order to secure that all the content is relevant and following the websites guidelines.

#### User Stories that hasn't been implemented

- As a Site User I can choose what category I want my discussion post to be in. 

- As a Site User I can filter the articles by date or writer.

#### Future User Stories to consider

- As a Site User I can save or give a like to articles. 
- As a Site User I can find my saved or liked articles in my own profilepage to find the concerned articles easier.

## Design & Layout 

The site has a very simple and clean design which was chosen purposely in order to create a sense of reliability that aligns with the websites goals, to act like a newssite.

### Wireframes

Wireframes were produced using Balsamiq.

 <details>

 <summary>Desktop Wireframe</summary>

![Desktop Wireframe]()

 </details>

 <details>
    <summary>Mobile Wireframe</summary>

![Mobile Wireframe]()

 </details>

### Color Scheme 

The colors used for Connected Website is mainly black, white and grey, to present a serious approach. 
The different pop of colors that appear are mainly focused on the buttons and icons in the footer. 
The colors or the button is matched and faded with different generic gradient palettes based of these:

![Color that the palettes are based of](/docs/readme_images/color-for-palettes.png)

### Images

All images is uploaded in the adminpanel to the website with cloudinary. 
Every image is borrowed from:
[Pexels](https://www.pexels.com/sv-se/).

### Fonts

The Roboto font is used on the main content on the website, for example the "About us" page. 
On every heading the font Oswald is used, as well in the logo name in the header. 

All fonts are from [Google Fonts](https://fonts.google.com/).

### Favicon 

The favicon was generated through [Favicon.io](https://favicon.io/), and is depicting a big C for Connected.

### Social Media Icons

The design and layout effects of the social media icons in the footer is borrowed from [parthwebdev - GitHub](https://github.com/parthwebdev/UI-Components/blob/main/Socials/02/index.html), and are responsible for creating the effect when the icon is held, the background color of the selected social media icon is transferred to the same apps color scheme.

## Agile Methodology

To manage the development of this project, I used the GitHub projects for an agile approach. 
You can view the projectboard
[here.](https://github.com/users/tildeholmqvist/projects/9)

When planning for this project 11 Github Issues were created, with two out of this as future improvement.
Each issue has a list of acceptance criterias, making the execution of the task clear, and easier to navigate to completion.

## Data Model

This project uses the principles of Object-Oritented Programming(OOP) along with Django's Class-Based Generic Views, to create this online news platform.

The site administator can post articles, while the site users are allowed to comment on them. 
The site user can however post their own post in the dedicated online forum.

For user authentication, Django Allauth is employed to ensure a secure access. 

To manage the posts, both in articles and in the discussion forum, a post model was developed, 
showcasing the title, author and date. 

To manage the categories, a category model was developed, showcasing the title of the category, allowing the user to easily navigate to their pick of category. 

To manage comments, both in articles and in the discussion forum, a comment model was developed, working in the same way as the post model, with some additions. 

## Features

### Header

![Header](/docs/readme_images/header.png)

#### Logo
- A logo was created using the Oswald font.

- The logo is linked to the home page for easier navigation for the user.

#### Navigation Bar

- The header and navigation bar is present at every page and includes every link to the other pages.

- The Category link contains a dropdown menu allowing the user to pick their category of choice. 

- For the logged in user the My profile link contains of a dropdown menu allowing the user to pick between showing their profilepage or log out. 

![Navigation bar - logged in](/docs/readme_images/nav-bar-loggedin.png)

- For the signed out user the navigation bar contains a link to Log in / Register 

![Navigation bar - logged in](/docs/readme_images/nav-bar-loggedout.png)

### Footer

![Footer](/docs/readme_images/footer.png)

- The footer section includes links to Instagram, Facebook, Youtube and Linkedin.

- When the links in the footer is clicked, that opens a separate browser tab to avoid pulling the user away from the site.

- When hovering the icons their apps original colorscheme will appear.
![Footer](/docs/readme_images/footer1.png)
![Footer](/docs/readme_images/footer2.png)
![Footer](/docs/readme_images/footer3.png)
![Footer](/docs/readme_images/footer4.png)

### Home Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/amiresponsiveconnected.png)

- The homepage consists of the latest news articles, showing six posts per page. 

- The homepage articles consists of a preview of the post, showing images and excerpts of the article.

- The homepage has a page navigator allowing the user to read more than six articles. 

### The Article Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/article-page.png)

- The article page appears if a user clicks on one of the titles on the articles on the home page.

- The article page consists of the different articles, depending on what articles title the user clicked on. 

- The article page allows a logged in user to comment on the article.

- The article page allows a logged in user to see their own, unapproved comments. 

- The article page allows a signed out user to read the articles, but not to comment on them. 

### About Us Page 

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/about-us.png)

- The about us page lets the user read about the company thats behind the news site Connected. 

- The about us page informs the user about what they can expect from the newssite and what the newssites goals is. 

### The Discussion Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/discussion.png)

- The discussion page consists of discussion posts made my different users regarding the topic of the newssite. 

- The discussion page is displaying a login button, if the user is not logged in, transfering the user to a login form. 

- The discussion page is displaying a button with the caption "Create Your Own" allowing the user to create their own post in the discussion forum. 

### The Discussionpost Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/discussion-post.png)

- The discussionpost page appears if a user clicks on one of the titles on the discussions in the forum.

- The discussionpost page consists of the different discussionposts, depending on what discussion title the user clicked on. 

- The discussionpost page allows a logged in user to comment on the discussions.

- The discussionpost page allows a logged in user to see their own, unapproved comments. 

- The discussionpost page allows a signed out user to read the discussions, but not to comment on them. 

### The Profile Page

![Screenshot of my webpage](/docs/readme_images/profile-page.png)

- The profile page is a page just available for the signed in user. 

- The profile page includes a User information box, displaying the Username and email adress. 

- The profile page consists of the logged in users previously made comments on news articles and discussionposts, as well as their own discussion posts.

### Log in / Register Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/login-register.png)

- The Log in / Register page consists of a Log in form, provided by Django Allauth. 

- The Log in / Register page contains a button allowing the user to create a new account if they don't already have one. 

- The Log in / Register page contains a textbox with a short description about the page and the page social media links, as icons. 


### Sign Up Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/signup.png)

- The Sign Up page consists of a sign up form, provided by Django Allauth.

- The Sign Up page lets the user enter a valid username, emailadress and password, before allowing them to sign up for Connected.
