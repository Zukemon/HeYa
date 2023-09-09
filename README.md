<p align="center">
  <a href="https://heya.herokuapp.com/" target="_blank">
    <h1>HeYa!</h1>
  </a>
</p>

# Table of Contents
1. [Overview](#overview)
2. [Usage](#usage)
3. [Setup](#setup)
4. [Technologies](#technology)



## Overview: 
Heya is a simple App for making video greeting cards. I created it from a function I made during my CS50P course, final project. This version is a work in progress.

## Usage:
<p>Once the user enters the landing page they'll find a welcoming message and instructions to navigate to the next, "HeYa" page. On this page is a form for entering the text for the message that they want printed out on the video card, and an options menu for selecting a theme.
</p>

    It's a simple 2 button APP:
    • The heya emoticon/ button to navigate to the next page, and the render button.

## Setup:
<p>
    • The main project folder contains 2 Python scripts, 'project.py' and 'test_project.py', one 'templates' folder, and one 'renders' folder.
</p>    
<p>
    • The 'templates' folder has all the templates/background per video card theme.
</p>
<p>
    • The 'renders' folder contains all the completed/rendered-out 'HeYa' video cards.
</p> 

<a href= "https://heya.herokuapp.com"><h5>Web App</h5></a>

<a href= "https://youtu.be/5IpgcbLYTug"><h5>YouTube Demo</h5></a>

    
## Technologies <a name="technology"></a>
<table>
  <tr>
    <td>Languages</td>
    <td> <img alt="Python" src="https://img.shields.io/pypi/pyversions/html?style=for-the-badge&logo=python&logoColor=white"/> <img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> <img alt="HTML5" src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img alt="CSS3" src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/></td>
  </tr>
  <tr>
    <td>Frameworks & Libraries</td>
    <td><img alt="Flask" src="https://img.shields.io/badge/flask%20-%2320232a.svg?&style=for-the-badge&logo=flask&logoColor=%white"/></td>
  </tr>
  <tr>
    <td>Hosting</td>
    <td><img alt="Heroku" src="https://img.shields.io/badge/heroku%20-%c9c3e6.svg?&style=for-the-badge&logo=heroku&logoColor=white"/>
    </td>
  </tr>
</table>

<h4>Commands to run app on local server (OS X):</h4>

    • Download code. Go to directory. Create virtual environment
    
    "pip install virtualenv"
    
    • Install requirements
    
    "pip install -r requirements.txt"
    
    • Activate virtual environment
    
    "source venv/bin/activate"
    
    • Enter command "flask run"
    
    Follow the link while app is running succesfully and app should now be visible in your browser.
    
    Use "ctrl c" to quit process.
