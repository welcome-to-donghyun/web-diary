from django.conf.urls import url
from . import views

app_name='schedule'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^schedule/(?P<current>[0-9]+)$', views.to_do_list_calendar, name='memo_main'),

    url(r'^memo/new$', views.MemoNew.as_view(), name='memo_new'),
    url(r'^memo/edit/(?P<pk>[0-9]+)$', views.memo_edit, name='memo_edit'),
    url(r'^memo/detail/(?P<pk>[0-9]+)$', views.MemoDetailView.as_view(), name='memo_detail'),
    url(r'^memo/delete/(?P<pk>[0-9]+)$', views.MemoDelete.as_view(), name='memo_delete'),

    url(r'^diary/new/(?P<diary_id>[0-9]+)$', views.DiaryNew.as_view(), name='diary_new'),
    url(r'^diary/edit/(?P<diary_id>[0-9]+)$', views.diary_edit, name='diary_edit'),
    url(r'^diary/detail/(?P<diary_id>[0-9]+)$', views.diary_detail, name='diary_detail'),
    url(r'^diary/delete/(?P<diary_id>[0-9]+)$', views.DiaryDelete.as_view(), name='diary_delete'),
]
