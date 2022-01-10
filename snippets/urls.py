from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# taking the original urlpatterns and generating a new version with taking care of format
# adding something like this : <URLPattern 'snippets<drf_format_suffix:format>'>
urlpatterns = format_suffix_patterns(urlpatterns)
