# django rest framework official tutorial 
## Part 6

### Notes:
- So while Class based views provide methods `get() post() put() ..etc` that will be used to determine the the request types accepted by the View, the ViewSets provide **actions** instead and each action ca .
- Now ViewSets can serve multiple actions (methods) , the link `action <---> request.method` happens at `urls.py` either by extracting (generating) views from ViewSets like this:
``` python
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
urlpatterns = [ path('snippets/', snippet_list, name='snippet-list'),]
```
or by letting DefaultRouter do it for you.

1 function view = 1 class view = 1 action of ViewSet 