from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schedule$', views.to_do_list_calendar, name='schedule_main'),
]
