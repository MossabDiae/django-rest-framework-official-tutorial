# django rest framework official tutorial 
## Part 3

### Notes:
- when rewriting our functions as views that inherit from `APIview` we changed the the check for Http methods for e.g `if request.method == 'GET'` to methods `def get()` , the question that I had was : how does our class knows that it should call the get() method when it has a GET request or post() method when it get a POST request ?

at first I checked the `APIview`'s source code looking form something as simple as `if request.method == 'GET'` , well little did I know , nothing to be found . Later I found [this](https://stackabuse.com/creating-a-rest-api-with-django-rest-framework#theapiviewclass) article which had the following line :
> We will be using the APIView class to represent views, which is a **subclass of Django's View class**. This way we get bootstrapped post(), get(), patch()

Aha ! maybe the answer was after all in Django's View class , a peak into [its source code](https://github.com/django/django/blob/ca9872905559026af82000e46cde6f7dedc897b6/django/views/generic/base.py#L93) and indeed , a dispatch method was responsible on checking that (code shortened for clarity).
``` python
class View:
  # ........
  http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
  # ........
  def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
    if request.method.lower() in self.http_method_names:
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
    else:
        handler = self.http_method_not_allowed
    return handler(request, *args, **kwargs)
```

- when using Mixins 
``` python
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView)
```
the `ListModelMixin` provides `list()` that can be linked to a GET request:
``` python
def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```
Now, `list()` is taking care of getting the queryset, making a serializer and giving the response back 
> return Response(serializer.data)

the reason this is working dynamically is that `GenericAPIView` will provide the mixins with methods such as `.get_object`, `.get_serializer` in the [tutorial](https://www.django-rest-framework.org/tutorial/3-class-based-views/) this was called **core functionality**.

- Finally you can do another level of abstraction and use generic views that have already implemented the definition of get(), post(), delete() .. etc , all you need to provide is a `queryset` and a `serializer` , for e.g this is the implementation of `rest_framework.generics.RetrieveAPIView` which returns one object:

``` python
class RetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```
How does it know which object to get while all you're giving in queryset is `queryset = Snippet.objects.all()` ?

the answer inside `rest_framework.mixins.RetrieveModelMixin` :
``` python
class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  #<--- HERE (its definition in GenericAPIView)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
```
