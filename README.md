# django rest framework official tutorial 
## Part 2

### Notes:
- according to drf source code by using `@api_view` decorator you convert your function views to sub-class of APIview which uses the Request object of drf thus giving you access to more features mainly the `request.data` that gives access to submitted data of many http verbs (POST, PATCH, PUT). Default Django HttpRequest object lacked that.

- notice that instead of returning `JsonResponse` in our views forcing us to use JSON , we're using drf's `Response` , giving it the needed data like this `Response(serializer.data)` and everything is good .