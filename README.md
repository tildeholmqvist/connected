# CONNECTED 

Connected is a news site focused on articles regarding technology and Internet media.
The site's main goal is to update the user about different discoveries in subjects and categories such as:
- Artificial Intelligence
- Technological Science
- Online Culture
- Tech news
- Technological Gadgets

Connected is not only a site for news and article research but also an online forum where the user can discuss with other users about different subjects and questions, regarding the main concept. 

This website includes a first page displaying the latest articles, an "About us" page, different pages for the different categories that the article is posted in, a discussion forum, and lastly their profile page which allows the user to see their own previously made posts and comments. 

The Connected website can be found here - [Connected.](https://connected-c643fb1afe74.herokuapp.com/)

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/amiresponsiveconnected.png)


## Table of Contents

- [Connected](#connected)
  * [Site Owner Goals](#site-owner-goals)
  * [User Stories](#user-stories)
    - [User Profile](#user-profile)
    - [User Navigation](#user-navigation)
    - [Site Administration](#site-administration)
    - [User Stories that haven't been implemented](#user-stories-that-havent-been-implemented)
    - [Future User Stories to consider](#future-user-stories-to-consider)
  * [Design & Layout](#design--layout)
    - [Wireframes](#wireframes)
    - [Color Scheme](#color-scheme)
    - [Images](#images)
    - [Fonts](#fonts)
    - [Favicon](#favicon)
    - [Social Media Icons](#social-media-icons)
- [Agile Methodology](#agile-methodology)
- [Data Model](#data-model)
- [Features](#features)
  * [Header](#header)
    - [Logo](#logo)
    - [Navigation Bar](#navigation-bar)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [The Article Page](#the-article-page)
  * [About Us Page](#about-us-page)
  * [The Discussion Page](#the-discussion-page)
  * [The Discussionpost Page](#the-discussionpost-page)
  * [The Profile Page](#the-profile-page)
  * [User Account Pages](#user-account-pages)
    - [Log in / Register](#log-in--register)
    - [Sign Up](#sign-up)
- [Testing](#testing)
  * [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [W3C Validator HTML](#w3c-validator-html)
    - [Summernote Errors](#summernote-errors)
    - [Summernote Text Editor and Troubleshooting](#summernote-text-editor-and-troubleshooting)
  * [W3C Validator CSS](#w3c-validator-css)
  * [JS Hint](#js-hint)
  * [PEP8](#pep8)
- [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Responsiveness](#responsiveness)
- [Manually Testing](#manually-testing)
- [Bugs and Issues](#bugs-and-issues)
  * [Unfixed Bugs](#unfixed-bugs)
- [Deployment - Heroku](#deployment---heroku)
  * [Create the Heroku App](#create-the-heroku-app)
  * [Connect the Postgres database](#connect-the-postgres-database)
  * [Create the environment setup](#create-the-enviorment-setup)
  * [Create Files/Directories](#create-filesdirectories)
  * [Update the Heroku Config Vars](#update-the-heroku-config-vars)
  * [Deploy your site](#deploy-your-site)
- [Languages](#languages)
- [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
  * [Additional Libraries Used](#additional-libraries-used)
- [Credits](#credits)



## Site Owner Goals

- As a Site Owner I can present relevant and interesting news articles about recent discoveries or updates in the online tech world. 

- As a Site Owner I can allow the users access to the website and discussion forum, allowing the user to comment on different articles and discussions along with other users and because of that create an interactive environment for those who wish to join.

- As a Site Owner I can present the user with a website that is easy to navigate, fully responsive, and contains a simple, yet well-thought-out layout, suitable for the website.

- As a Site Owner I can allow the user to sign up to the website and interact through comments and posts. 


## User Stories

#### User Profile

- As a Site User I can register my account, allowing me to comment on existing articles and discussion posts. 

- As a Site User I can register my account, allowing me to create my posts in the designated discussion forum. 

- As a Site User I can find all my previously made posts and comments in my profile.

- As a Site User I can edit and delete my previously made comments and posts, even if they have been approved or haven't been approved, by the site administration. 

- As a Site User I can log in or log out of my account so that I can keep my account secure.

- As a Site User I can see if I am logged in or not.

#### User Navigation

- As a Site User I can easily navigate to the home page, viewing the latest articles posted.

- As a Site User I can easily navigate to a page regarding a specific category containing the relevant articles.

- As a Site User I can easily find information about the website and the purpose of the website.

- As a Site User I can navigate to the online forum allowing me to interact with other users on relevant topics. 

- As a Site User I can easily sign up, log in, and log out.

#### Site Administration

- As a Site Administrator I can easily update the website with new articles and associated images.

- As a Site Administrator I can manually approve the user's comments before the site users can view them, to ensure that all the content is relevant and following the website's guidelines.

- As a Site Administrator I can manually approve the user's posts before the site users can view them, to ensure that all the content is relevant and following the website's guidelines.

#### User Stories that haven't been implemented

- As a Site User I can choose what category I want my discussion post to be in. 

- As a Site User I can filter the articles by date or writer.

#### Future User Stories to Consider

- As a Site User I can save or give a like to articles. 
- As a Site User I can find my saved or liked articles in my profilepage to find the concerned articles easier.

## Design & Layout 

The site has a very simple and clean design which was chosen purposely to create a sense of reliability that aligns with the goals of the website, to act like a news site.

### Wireframes

Wireframes were produced using Balsamiq.

 <details>

 <summary>Home Page</summary>

![Home Page](docs/readme_images/wireframes/home-page.png)

 </details>

 <details>
    <summary>About Us Page</summary>

![About Page](docs/readme_images/wireframes/about-page.png)

 </details>

  <details>
    <summary>Category Page</summary>

![Category Page](docs/readme_images/wireframes/category-page.png)

 </details>

 <details>
    <summary>Discussion Page</summary>

![Discussion Page](docs/readme_images/wireframes/discussion-page.png)

 </details>

  <details>
    <summary>Profile Page</summary>

![Profile Page](docs/readme_images/wireframes/profilepage-page.png)

 </details>

  <details>
    <summary>Log in / Register Page</summary>

![Login Page](docs/readme_images/wireframes/login-page.png)

 </details>

### Color Scheme 

The colors used for the Connected Website are mainly black, white, and grey, to present a serious approach. 
The different pops of colors that appear are mainly focused on the buttons and icons in the footer. 
The colors or the button is matched and faded with different generic gradient palettes based on these:

![Color that the palettes are based on](/docs/readme_images/color-for-palettes.png)

### Images

All images are uploaded in the admin panel to the website with Cloudinary. 
Every image is borrowed from:
[Pexels](https://www.pexels.com/sv-se/).

### Fonts

The Roboto font is used on the main content of the website, for example, the "About us" page. 
The Oswald font is used on all headings, as well as the logo name in the header.

All fonts are from [Google Fonts](https://fonts.google.com/).

### Favicon 

The favicon was generated through [Favicon.io](https://favicon.io/) and depicts a big C for Connected.

### Social Media Icons

The design and layout effects of the social media icons in the footer are borrowed from [parthwebdev - GitHub](https://github.com/parthwebdev/UI-Components/blob/main/Socials/02/index.html) and are responsible for creating the effect when the icon is held, the background color of the selected social media icon is transferred to the same apps color scheme.

## Agile Methodology

To manage the development of this project, I used the GitHub projects for an agile approach. 
You can view the projectboard
[here.](https://github.com/users/tildeholmqvist/projects/9)

When planning for this project 11 GitHub Issues were created, with two out of these as future improvement.
Each issue has a list of acceptance criteria, making the execution of the task clear, and easier to navigate to completion.

## Data Model

This project uses the principles of object-oriented programming (OOP) along with Django's Class-Based Generic Views, to create this online news platform.

The site administrator can post articles, while the site users are allowed to comment on them. 
The site user can however post their discussions in the dedicated online forum.

For user authentication, Django Allauth is employed to ensure secure access. 

To manage the posts, both in articles and the discussion forum, a post model was developed, 
showcasing the title, author, and date. 

To add categories, a category model was developed, showcasing the title of the category, allowing the user to easily navigate to their pick of category. 

To manage comments, both in articles and in the discussion forum, a comment model was developed, working in the same way as the post model, with some additions. 

![Database Schema](docs/readme_images/database-schema.png)

## Features

### Header

![Header](/docs/readme_images/header.png)

#### Logo
- A logo was created using the Oswald font.

- The logo is linked to the home page for easier navigation for the user.

#### Navigation Bar

- The header and navigation bar are present on every page and include every link to the other pages.

- The Category link contains a dropdown menu allowing the user to pick their category of choice. 

- For the logged-in user the My Profile link contains a dropdown menu allowing the user to pick between showing their profile page or logging out. 

![Navigation bar - logged in](/docs/readme_images/nav-bar-loggedin.png)

- For the signed-out user the navigation bar contains a link to Log in / Register 

![Navigation bar - logged in](/docs/readme_images/nav-bar-loggedout.png)

### Footer

![Footer](/docs/readme_images/footer.png)

- The footer section includes links to Instagram, Facebook, YouTube and Linkedin.

- When the links in the footer are clicked, that opens a separate browser tab to avoid pulling the user away from the site.

- When hovering the icons their app's original color scheme will appear.
![Footer](/docs/readme_images/footer1.png)
![Footer](/docs/readme_images/footer2.png)
![Footer](/docs/readme_images/footer3.png)
![Footer](/docs/readme_images/footer4.png)

### Home Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/amiresponsiveconnected.png)

- The homepage consists of the latest news articles, showing six posts per page. 

- The homepage articles consist of a preview of the post, showing images and excerpts of the article.

- The homepage has a page navigator allowing the user to read more than six articles. 

### The Article Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/article-page.png)

- The article page appears if a user clicks on one of the titles on the articles on the home page.

- The article page consists of different articles, depending on what article title the user clicked on. 

- The article page allows a logged-in user to comment on the article.

- The article page allows a logged-in user to see their own, unapproved comments. 

- The article page allows a signed-out user to read the articles, but not to comment on them. 

### About Us Page 

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/about-us.png)

- The About Us page lets the user read about the company that's behind the news site Connected. 

- The About Us page informs the user about what they can expect from the new site and what the news site's goals are. 

### The Category Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/category.png)

- The category page appears if a user clicks on one of the categories on the articles on the home page.

- The category page appears if a user clicks on one of the categories in the category drop-down menu in the navigation bar.

- The category page consists of different articles, depending on what category the user clicked on. 

- The category page allows a logged-in user to comment on the article.

- The category page allows a logged-in user to see their own, unapproved comments. 

- The category page allows a signed-out user to read the articles, but not to comment on them. 

### The Discussion Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/discussion.png)

- The discussion page consists of discussion posts made by different users regarding the topic of the news site. 

- The discussion page displays a login button. If the user is not logged in, it transfers the user to a login form. 

- The discussion page displays a button with the caption "Create Your Own" allowing the user to create their post in the discussion forum. 

### The Discussionpost Page

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/discussion-post.png)

- The discussion page appears if a user clicks on one of the titles on the discussions in the forum.

- The discussion post page consists of different discussion posts, depending on what discussion title the user clicked on. 

- The discussion post page allows a logged-in user to comment on the discussions.

- The discussion post page allows a logged-in user to see their own, unapproved comments. 

- The discussion post page allows a signed-out user to read the discussions, but not to comment on them. 

### The Profile Page

![Screenshot of my webpage](/docs/readme_images/profile-page.png)

- The profile page is a page just available for the signed-in user. 

- The profile page includes a User information box, displaying the Username and email address. 

- The profile page consists of the logged-in user's previous comments on news articles and discussion posts, as well as their discussion posts.

### User Account Pages

#### Log in / Register 

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/login-register.png)

- The Log in / Register page consists of a Log in form, provided by Django Allauth. 

- The login / Register page contains a button allowing the user to create a new account if they don't already have one. 

- The login / Register page contains a textbox with a short description about the page and the page's social media links, as icons. 


#### Sign Up 

![Screenshot of my webpage from Am I responsive?](/docs/readme_images/signup.png)

- The Sign Up page consists of a signup form, provided by Django Allauth.

- The Sign Up page lets the user enter a valid username, email address, and password, before allowing them to sign up for Connected.

## Testing

#### User Story Testing 

 - All user stories have been tested out and are working correctly. 
 - All site owner stories have been tested out and are working correctly.

## Validator Testing 

### W3C Validator HTML
- When validating the About Page, no errors were found. 
- When validating the Login / Sign up page, no errors were found. 
- When validating the Logout page, no errors were found.
- When validating, errors related to the Summernote text editor occurred on these pages: 
  - Home Page
  - Article Page
  - Categories Page
  - Discussion Page
  - Profile page
 - When validating, errors related to attributes on buttons occurred on these pages:
   - Article Page
   - Discussion post Page
   - Profile Page

[W3C Validator](https://validator.w3.org/)

#### Summernote Errors
When validating the website a lot of errors occurred, all due to the text areas created in the Summernote text editor. 

#### Summernote Text Editor and Troubleshooting
Summernote is a WYSIWYG editor, used for creating text areas in web applications. While Summernote simplifies the experience for the users and enables interactive content creation on the website, including features allowing the users and admins to write text areas, including images and font styling, this can sometimes result in an unexpectedly behaving code, that doesn't pass through the HTML validators. 

When troubleshooting these errors, it's a good idea to isolate the code snippets that are created with Summernote, to identify that the errors are connected to the Summernote text areas. This makes it easier to guarantee that the issues or errors are only referred to the Summernote editor. 

The Summernote errors could have an impact on how the website presents in other tests and contexts,
the main code structure appears to be fine and without any errors or bugs. 
However, it is important to address the fact that the Summernote is causing errors in the code, to ensure the overall quality of the website. 


#### Fixing Button Attribute Errors
During website validation, errors were identified concerning the buttons responsible for handling delete and edit functions on discussions and comments. These errors appeared due to the use of attributes such as "discussion_pk," "discussion_id," "comment_id," and "post_slug," which are not allowed on button elements.

To correct this issue, I added "data-" before those attributes, changing them to "data-discussion_pk," "data-discussion_id," "data-comment_id," and "data-post_slug." This made sure they met HTML5 standards and resolved the validation errors.


### W3C Validator CSS
#### When validating the CSS styling, 2 errors were found:
- Both errors were located in the code handling the icons in the footer. This code used for the layout of the icons is borrowed from [parthwebdev - GitHub](https://github.com/parthwebdev/UI-Components/blob/main/Socials/02/index.html). When troubleshooting these errors, other attributes were tried out without achieving the same effect. Because of this, I decided to keep the CSS code intact and address the errors without changing it.

[W3C Validator CSS](https://jigsaw.w3.org/css-validator/)

### JS Hint 

No errors were found in my JavaScript.

- The following metrics were returned:
  - There are 7 functions in this file.
  - Function with the largest signature takes 1 argument, while the median is 1.
  - Largest function has 29 statements in it, while the median is 4.
  - The most complex function has a cyclomatic complexity value of 7 while the median is 1.

[Jshint validator](https://jshint.com/)

### PEP8

No errors were found in my Python files.

[CI Python Linter](https://pep8ci.herokuapp.com/)

## Lighthouse 

When I checked my website's performance with the Lighthouse tool, I noticed it wasn't doing as well as I hoped, especially in performance and best practices.
Despite having already optimized the images, it seems other things are slowing down how quickly the website loads.
I suspect that elements such as Javascript and CSS may be contributing to the slowdown. 
Addressing these issues would likely improve the website's performance and provide a better user experience.

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| DESKTOP        |              |               |                 |     |
| Home           |           94 |            90 |              86 | 100 |
| Article Page   |           97 |            90 |              91 | 100 |
| About Us       |           99 |            97 |              95 | 100 |
| Categories     |           94 |            86 |              86 | 100 |
| Discussion     |           98 |            94 |              95 | 100 |
| Log in/Register|           99 |            88 |              95 | 100 |
| Log out        |           98 |           100 |              95 | 100 |
| Create Discussion   |           95 |           89 |             95 | 100 |
| Profilepage    |           97 |            95 |              91 | 100 |
| Edit Comment   |          100  |           94 |              95 |  100 |
| Edit Post      |           97 |            89 |              95 | 100 |
|                |              |               |                 |     |
| MOBILE         |              |               |                 |     |
| Home           |           74 |            90 |              86 | 100 |
| Article Page   |           73 |            90 |              91 | 100 |
| About Us       |           99 |            97 |              95 | 100 |
| Categories     |           92 |            86 |              86 | 100 |
| Discussion     |           93 |            94 |              95 | 100 |
| Log in/Register|           78 |            88 |              95 | 100 |
| Log out        |           87 |           100 |              95 | 100 |
| Create Discussion   |           90 |           89 |             95 | 100 |
| Profilepage    |           91 |            91 |              95 | 100 |
| Edit Comment   |           94  |           94 |              95 | 100 |
| Edit Post      |           90 |            89 |              95 | 100 |


## Browser Testing

The website has been tested on different browsers such as Google Chrome, Safari, and Firefox, and is working correctly.

## Device Testing

The webpage has been tested on different devices such as iPhone, iPad, MacBook Pro, and iMac, and is working correctly.

## Responsiveness

The website's responsiveness has been tested through the Google Chrom Dev Tool, [Am I Responsive?](https://ui.dev/amiresponsive) and [Responsinator](http://www.responsinator.com/), and is working correctly.

## Manually Testing 
#### Home Page
 - Every article has been tested and is working correctly, opening up a new page when clicked. 
 - The previous/Next button has been tested and is working correctly.
 - The links in the navigation bar have been tested and are working correctly. 

 #### Article Page 
  - The Category link has been tested and is working correctly, opening up a new page when clicked. 
  - The leave-a-comment form has been tested and is working correctly. 
  - The nonapproved comments are working correctly and can only be viewed by the author. 
  - The edit/delete button on comments has been tested and is working correctly. 
  - The links in the navigation bar have been tested and are working correctly. 


#### Category Page
 - Every article on the category page has been tested and is working correctly, opening up a new page when clicked. 
 - The links in the navigation bar have been tested and are working correctly. 

#### Discussion Page
 - Every discussion on the page has been tested and opens on a new page when clicked, working correctly. 
- The previous/Next button has been tested and is working correctly.
- The login button has been tested and is working correctly, transferring the logged-out user to the login form. 
- The Submit button in Create your post, has been tested and is working correctly transferring the user to the discussion form. 
 - The links in the navigation bar have been tested and are working correctly. 

#### Profile Page
- The discussions and comments on the page have been tested, and open on a new page when clicked, working correctly. 
- The Edit/Delete/View Post buttons have been tested and are working correctly. 
 - The links in the navigation bar have been tested and are working correctly. 

#### Login / Register Page
- The login form has been tested and is working correctly.
- The Signup form has been tested and is working correctly. 
 - The links in the navigation bar have been tested and are working correctly. 

#### Log out Page
- The logout button has been tested and is working correctly. 
 - The links in the navigation bar have been tested and are working correctly. 
 
#### Forms 
 - The Comment form has been tested and is working correctly, accepting valid input without any issues.
 - The Create Discussion form has been tested and is working, demanding valid input in the title.
   - The Create Discussion form is however also working even with invalid input in the text area.
 - The Login form has been tested and is working correctly, accepting valid input without any issues.
 - The signup form has been tested and is working correctly, accepting valid input without any issues.

#### Messages 
  - Messages providing feedback on the user's actions are working correctly. 

## Bugs and Issues

Overall the website is working correctly, and the main code is free from errors, except for the [Summernote-related ones](#summernote-errors).

### Unfixed Bugs and Issues

When a user is creating their discussion post, they can submit the post with invalid input in the text area.

Although users are required to insert a valid title, the discussion will still be posted even if the text contains invalid content.

For the time being, I have chosen to leave this bug unresolved. Since site administration approval is required before discussion posts are displayed to all users, an empty or invalid discussion post does not significantly impact the user experience.

When users click on 'Forgot your password?', they're unable to reset their password. Although this is a significant issue, it's not directly related to this project, right now. Therefore, I've chosen not to address this problem.

However, I will carefully consider implementing these identified issues as potential areas for future improvement.

## Deployment - Heroku

The website was deployed through the hosting platform Heroku, from its GitHub repository.

### Create the Heroku App
- Create an account or log in to [Heroku](https://dashboard.heroku.com/apps).
- On the main page click "New" at the top right corner and choose "Create New App" from the dropdown menu.
- Give the app a unique and meaningful name.
- Next up, select your region.
- Click "Create App".

### Connect the Postgres database
- In the Resources tab, type "Postgres", and select "Heroku Postgres".
- Copy the DATABASE_URL from Config Vars in the Settings Tab.

### Create the environment setup
- Create an env.py file in the main directory of your GitPod workspace.
- Add the DATABASE_URL value and your personally selected SECRET_KEY value to the env.py file.
- Update your settings.py file to import the env.py file and add the paths for both the DATABASE_URL and SECRET_KEY.
- Comment out the default database configuration.
- Save your files and make the migrations.
- Add Cloudinary URL to the env.py file.
- Add Cloudinary to the "installed apps" in the settings.py.
- Configure static file settings including URL, storage path, directory path, root path, media URL, and default file storage path.
- Connect the file to the templates directory in Heroku.
- Rename the templates directory to TEMPLATES_DIR.
- Add Heroku to your ALLOWED_HOSTS.

### Create  Files/Directories
- Create the requirements.txt file
- Create a file named "Procfile" in the main directory of your project.
- In "Procfile" add "web: gunicorn project-name.wsgi".

### Update the Heroku Config Vars
- In Heroku, add these Config Vars:
    - SECRET_KEY value 
    - CLOUDINARY_URL
    - PORT = 8000
    - DISABLE_COLLECTSTATIC = 1

### Deploy your site
- Before deploying, make sure that your DEBUG is set to false in your settings.py file.
- Go to the deploy tab on Heroku, navigate to connect to GitHub, and then pick the required repository.
- Scroll to the bottom of the page where you can choose if you want to Enable Automatic Deploys for 

- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll down to the bottom of the page and there you can choose if you want the deploys to be Automatic or Manually. The Manually deployed branches need redeploying each time the repository is updated.
- Deploy your website. 
- Click "View", or scroll up to "Open App" to visit the deployed site.

The deployed website can be found here - [Connected](https://connected-c643fb1afe74.herokuapp.com/).

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks, Libraries and Programs Used

- [Django](https://www.djangoproject.com/): The main framework used in this project, built with Python.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): The authentication library used for creating user accounts in this project.
- [PostgreSQL](https://www.postgresql.org/): Used as the database for this project.
- [GitHub](https://github.com/): Used as an agile tool and for project management.
- [Heroku](https://dashboard.heroku.com/login): Used as the cloud-based platform to deploy the site.
- [Bootstrap](https://getbootstrap.com/): Used as the main front-end framework.
- [Summernote](https://summernote.org/): A WYSIWYG editor.
- [Cloudinary](https://cloudinary.com/): Used for for image hosting services on the site.
- [Font Awesome](https://fontawesome.com/): Used for icons in the footer, and on comments.
- [Google Fonts](https://fonts.google.com/): Used to import fonts, elevating the layout of the project.
- [Coolors](https://coolors.co/): Used to find the right colors and palettes.
- [Balsamic](https://balsamiq.com/wireframes/desktop/#): Used to create the wireframes.
- [Am I Responsive?](https://ui.dev/amiresponsive): Used for the images for the README, showing the responsiveness of the site.
- [Favicon](https://favicon.io/): Used to create the favicon.
- [W3C](https://www.w3.org/): Used for HTML & CSS Validation.
- [PEP8 Online](http://pep8online.com/): Used to validate all the Pythoncode files.
- [Jshint](https://jshint.com/): Used to validate all javascript.

### Additional Libraries Used
- [asgiref](https://pypi.org/project/asgiref/): ASGI specification reference implementation.
- [oauthlib](https://pypi.org/project/oauthlib/): Provides OAuth client/server functionality.
- [psycopg2](https://pypi.org/project/psycopg2/): Python adapter for PostgreSQL database.
- [PyJWT](https://pypi.org/project/PyJWT/): Library for JSON Web Token encoding and decoding.
- [python3-openid](https://pypi.org/project/python3-openid/): Python OpenID library.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/): Provides OAuth support for requests.
- [sqlparse](https://pypi.org/project/sqlparse/): SQL parser for Python.
- [urllib3](https://pypi.org/project/urllib3/): HTTP client library for Python.
- [whitenoise](https://pypi.org/project/whitenoise/): Serves static files in Django applications.

## Credits 
- [Stack Overflow](https://stackoverflow.com/)
- [Bootstrap 4.0 Docs](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [Django Docs](https://docs.djangoproject.com/en/5.0/)
- [Real Python](https://realpython.com/)
- [MDBootstrap](https://mdbootstrap.com/docs/standard/extended/login/)
- [Medium](https://medium.com/)
- [Learn Django](https://learndjango.com/tutorials/django-slug-tutorial)
- [Dev Handbook](https://www.devhandbook.com/django/user-profile/)
- [Dev, Profile](https://dev.to/earthcomfy/django-user-profile-3hik)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)
- [Pexels](https://www.pexels.com/sv-se/): Used for the images on the site.
- [Tiny PNG](https://tinypng.com/): Used for optimizing the images.
- [Grammarly](https://app.grammarly.com/): Used for spellcheck. 
- Every article and comment is a mock article, created with [Open AI](https://chat.openai.com/).
- Tutor Support, Code Institute, for their support and advice.
- My mentor Antonio, for all of his knowledge, support, and advice.
