from django.conf.urls import patterns, include, url
import views
import feeds

urlpatterns = patterns('',
    url(r'post/(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post-detail'),

    url(r'feed/rss$', feeds.RSSFeed(), name='rss-feed'),
    url(r'feed/atom$', feeds.AtomFeed(), name='atom-feed'),
    url(r'$', views.IndexView.as_view(), name='index'),
)
