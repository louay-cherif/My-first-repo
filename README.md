# My-first-repo
This is the documentation for the right set up of our project
I hope you enjoy


1) start by installing python3 on your local machine

if you don't have Python installed, feel free to install it from the official website on the link bellow

2) install the project dependencies:
project dependencies are files that need to be installed with your Python as the project needs them to run successfully. Please go to your command line if you are using Windows or your terminal if you're using Linux and follow the steps bellow.


On windows:
a) go to your project folder: please move the folder of the project you downloaded or cloned from Github and position it on your Desktop before following those steps.
paste to your command line:
cd Desktop\<the project folder name>
replace the word between <> to the project folder name first
b) paste the following:
pip install requirements.txt
you might need to wait for some time until all dependencies are installed. Please note that the dependencies will be installed to your local machine, if you wnat to install them for the use of this project only, you can consider creating a vertual environment with the commands bellow before the pip install requiremnts.txt

python m venv .venv
.venv\script\activate.
then youare in the vertual environment whrere you can install he dependencie without interfering with your local machine preinstalled dependencies and they will no onger exist when you leave the vertual environment.

final step: run your flask environment ane start using the project:
in your cmd, paste the following lines line by line
flask run app.py
go to your broser and paste hte follwoing url to your address bar
http://127..0.1
the project will finally load on the local server, enjoy using it.

on your linux terminal
suppose you have the project folder  on your home directory past eht efollowing to your terminal
cd ~/<project_name>
replace the <project_name> with the actual name of the folder.


