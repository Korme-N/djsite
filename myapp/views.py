# myapp/views.py
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, )
from rest_framework.permissions import IsAuthenticated


class PostList(ListCreateAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)
        

class LimitOffPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        post_id = self.kwargs.get('id')
        post = get_object_or_404(Post, id=post_id)
        post.views_count = post.views_count + 1
        post.save()
        return post
