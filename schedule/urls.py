from django.conf.urls import url
from . import views

app_name='schedule'
urlpatterns = [
    url(r'^schedule$', views.to_do_list_calendar, name='memo_main'),
    url(r'^memo/new$', views.MemoNew.as_view(), name='memo_new'),
    url(r'^memo/edit/(?P<pk>[0-9]+)$', views.memo_edit, name='memo_edit'),
    url(r'^memo/detail/(?P<pk>[0-9]+)$', views.MemoDetailView.as_view(), name='memo_detail'),
    url(r'^memo/delete/(?P<pk>[0-9]+)$', views.MemoDelete.as_view(), name='memo_delete'),
]
