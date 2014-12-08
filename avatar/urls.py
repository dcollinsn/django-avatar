from django.conf.urls import url

from avatar import views

urlpatterns = [
    url(r'^add/$', views.add, name='avatar_add'),
    url(r'^change/$', views.change, name='avatar_change'),
    url(r'^delete/$', views.delete, name='avatar_delete'),
    url(r'^render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<size>[\d]+)/$',
        views.render_primary,
        name='avatar_render_primary'),
    url(r'^add_for_user/(?P<for_user>[\w@\.\+\-_]+)/$',
        views.add_avatar_for_user, name='avatar_add_for_user'),
    url(r'^change_for_user/(?P<for_user>[\w@\.\+\-_]+)/$',
        views.change_avatar_for_user, name='avatar_change_for_user'),
    url(r'^delete_for_user/(?P<for_user>[\w@\.\+\-_]+)/$',
        views.delete_avatar_for_user, name='avatar_delete_for_user'),
]
