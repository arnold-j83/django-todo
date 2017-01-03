from django.conf.urls import url
from django.contrib import admin
from todo.views import TodoView as todo_views
from accounts.views import RegistrationView as registration_view
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/$', todo_views.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', todo_views.as_view()),
    url(r'accounts/register/$', registration_view.as_view()),
    url(r'accounts/api-token-auth/$', obtain_jwt_token),
]
