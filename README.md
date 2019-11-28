# PROJECT RANKER 

## Description
Project Ranker is a django application used to rank projects for users. 
It helps in determining the Usability, Design and Content of a Website.  

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I can:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display Home Page | **On page load** | Landing Page and Projects that have uploaded. |
| Log in / Registration | **Click 'Sign In' tab on Navbar** | Login Page|
| View project details and ratings | **Click the Project Cover Photo** | Project details, link and ratings|
| Search for projects |**Enter search term on the navigation bar 'Seach Bar'**|Displays projects that meet the search term|
| View profile details and projects | **Click the 'Account' tab on Navbar** | User details and projects they have uploaded.|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* postgres database
* virtualenv
* django

### Cloning
* In your terminal:
        
        $ git clone https://github.com/sokkyyy/project-ranker.git
        $ cd project-ranker

## Running the Application
* Creating the virtual environment:

        $ pip install virtualenv
        $ virtualenv virtual
        $ source virtual/bin/activate

* Installing Django and other Modules:

        $ pip install -r requirements.txt


* To run the application, in your terminal:


        $ python3.6 manage.py runserver



## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test project

## Technologies Used
* Python3.6
* Django
* Semantic UI
* Google Fonts
* FontAwesome
* Postgres SQL

## License
[Ray Ndegwa](https://github.com/sokkyyy/)
