# django rest framework official tutorial 
## Part 2

### Notes:
- according to drf source code by using `@api_view` decorator you convert your function views to sub-class of APIview which uses the Request object of drf thus giving you access to more features mainly the `request.data` that gives access to submitted data of many http verbs (POST, PATCH, PUT). Default Django HttpRequest object lacked that.

- notice that instead of returning `JsonResponse` in our views forcing us to use JSON , we're using drf's `Response` , giving it the needed data like this `Response(serializer.data)` and everything is good .

- once you setup support for different formats you can ask the server for format type both by :
  1. using **Accept** header : `http http://127.0.0.1:8000/snippets/ Accept:application/json`
  1. appending the format suffix in url : `http http://127.0.0.1:8000/snippets.json`
  
- managed to delete the third snippet in the database using a DELETE request: 
``` bash
http DELETE http://127.0.0.1:8000/snippets/3/                                                                                                       
# HTTP/1.1 204 No Content                                                                                                                               
# Allow: PUT, OPTIONS, GET, DELETE                                                                                                                      
# Content-Length: 0                                                                                                                                     
# Date: Mon, 10 Jan 2022 00:37:17 GMT                                                                                                                   
# Referrer-Policy: same-origin                                                                                                                          
# Server: WSGIServer/0.2 CPython/3.10.1                                                                                                                 
# Vary: Accept, Cookie                                                                                                                                  
# X-Content-Type-Options: nosniff                                                                                                                       
# X-Frame-Options: DENY
```