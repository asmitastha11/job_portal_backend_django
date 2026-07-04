<!-- install virtual environment -->
pip install virtualenv

<!-- create virtual env -->
virtualenv env_name

<!-- activate virtualenv -->
env\Scripts\activate

<!-- install django -->
pip install django

<!-- to create django projects -->
django-admin startproject project_name(it creates project directory inside another folder )
So,
django-admin startproject project_name .

both are acceptable

<!-- To start server -->
py manage.py runserver

<!-- Add .gitignore file -->
(it tells git which files and folders to intentionally ignore and exclude)
-create .gitignore files
-then search for python in gitignore.io and paste in that file

<!-- Create an django-app  -->
py manage.py startapp appname
(Then put the app name in project settings.py in installed app)