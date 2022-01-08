# django rest framework official tutorial 
## Part 1

### Notes:
- setup the project slightly different than the tutorial: 
``` bash
mkdir official-tutorial
cd official-tutorial/
pyenv local django3.2
# already had the needed packages django, drf, pygment so no pip install

# notice the '.' , it means make current folder root for the project
django-admin startproject tutorial .

python manage.py startapp snippets
```