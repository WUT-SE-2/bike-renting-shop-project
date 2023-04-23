# Bike renting shop web application
[![Django CI/CD Workflow](https://github.com/WUT-SE-2/bike-renting-shop-project/actions/workflows/main.yml/badge.svg)](https://github.com/WUT-SE-2/bike-renting-shop-project/actions/workflows/main.yml)

### How to start project 
To start the project you have to run commands from the commands.txt file.
Remember to run them on docker in the directory that contains the content of the repository


#### Requirements
- Docker installed 
- POSTGRES installed 


### Setting up dataubase
#### Linux Setup 
Run the following commands to download postgres:
- sudo apt update 
- sudo apt install postgresql postgresql-contrib
- sudo service postgresql start 
Assure that the service is running with -sudo service postgresql status (port should be 5432)
- sudo su postgres4
- CREATE USER admin WITH PASSWORD 'admin';
There should be an information then that the suer has been created (CREATE ROLE) 
Then list user to check if the user was added by entering \du
Now issue:
- ALTER USER admin WITH SUPERUSER;
Then check if the superuser  attributes was added (\du)
Then create databse:
- CREATE DATABSE django
Grant privileges to the db for user admin
- grant all privileges on databse django to admin
Now the databse is configured, but remember to still create superuser for admin panel using python manage.py createsuperuser

#### Windows Setup
#####Option 1 
Download wsl and configure it and then do Linux configuration 
#####Option 2 
Download posgresql from official page and set up all from pgadmin4 panel 

