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