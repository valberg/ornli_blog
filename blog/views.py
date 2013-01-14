from django.views import generic
from blog import models

class IndexView(generic.ListView):
    queryset = models.Post.objects.all().order_by('-created')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetail(generic.DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
