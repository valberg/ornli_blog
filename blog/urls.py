from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'(?P<slug>[-\w]+)/', views.PostDetail.as_view(), name='post-detail'),
    url(r'$', views.IndexView.as_view(), name='index'),
)
