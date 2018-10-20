from user import views
from django.conf.urls import url

app_name = 'user'

urlpatterns = [
    url(r'^(?P<public_address>\w+)/$', views.UserView.as_view()),
]
