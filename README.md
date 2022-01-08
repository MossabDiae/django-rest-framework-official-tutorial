# django rest framework official tutorial 
After finished reading and practicing with Django for APIs (by William Vincent) I'm planning to do [the official tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/).

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