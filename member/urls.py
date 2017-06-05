from django.conf.urls import url
from member import views

app_name = 'member'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]
