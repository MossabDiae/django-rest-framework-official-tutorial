# django rest framework official tutorial 
## Part 1

### Notes:
- I've setup the project slightly different than the tutorial: 
``` bash
mkdir official-tutorial
cd official-tutorial/
pyenv local django3.2
# already had the needed packages django, drf, pygment so no pip install

# notice the '.' , it means make current folder root for the project
django-admin startproject tutorial .

python manage.py startapp snippets
```

- The explicit Serialization :
``` python
# create a model object
snippet = Snippet(code='print("hello, world")\n')

# model ---[serializer]---> serialized object
serializer = SnippetSerializer(snippet)

# serialized object -----> JSON
content = JSONRenderer().render(serializer.data)
```

- DESerialization :
``` python
# bytes ---> stream --[JSONParser]--> Dict(python native)
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# Dict ---[serializer]-> serialized object
serializer = SnippetSerializer(data=data)

# serialized object ---[serializer.save]---> model
serializer.is_valid()
serializer.save()

# please notice:
# a serializer has the ability to write directly to db with .save()
# a serializer is the linking part btwn data and models as follows:
# data ---[serializer(data=data).save]--> model
# model ---[serializer(model).data]--> data

```
