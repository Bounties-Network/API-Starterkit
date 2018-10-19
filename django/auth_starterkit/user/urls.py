from user import views
from django.conf.urls import url

app_name = 'user'

urlpatterns = [
    url(r'^(?P<public_address>\w+)/nonce/$', views.Nonce.as_view()),
    url(r'^user/$', views.UserView.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^logout/$', views.Logout.as_view()),
]
