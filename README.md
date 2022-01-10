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

- A new git trick : use `git log --oneline` to see commits line

After checking that the browsable api was still working after disabling the the multi formats support ,I decided to go back one step to the past . so the commits list was like this :
``` bash
git log --oneline
# 9fcccb8 (HEAD -> 2-requests-and-responses) re-disabled the format support to test if browsable api works
# dacb714 updated readme
# 1534d76 adding support for different formats
```
want to make a new state based on the dacb714 commit (NOT TO DETACH TO IT BUT TO BRING CHANGES FROM IT) so I did : `git checkout dacb714 .` (if no dot > detach mode)

Indeed `git status` is giving this as if we made changes ourselves:
``` bash
$ git status 
On branch 2-requests-and-responses
Your branch is ahead of 'origin/2-requests-and-responses' by 3 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   snippets/urls.py
        modified:   snippets/views.py
```
from there just : `git commit -am 'your comment'` and the `git log --oneline` gives now:
``` bash
ec0b0ae (HEAD -> 2-requests-and-responses) api still working , back to the future
9fcccb8 re-disabled the format support to test if browsable api works
dacb714 updated readme
1534d76 adding support for different formats
```
source of this git trick [here](https://medium.com/swlh/using-git-how-to-go-back-to-a-previous-commit-8579ccc8180f)

Part 2 DONE.