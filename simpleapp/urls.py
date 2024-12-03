from django.urls import path
from .views import (
    Posts, PostDetail, PostCreate, AuthorCreate, CategoryCreate, PostUpdate, PostDelete
)

urlpatterns = [
    path('', Posts.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('author_create/', AuthorCreate.as_view(), name='author_create'),
    path('category_create/', CategoryCreate.as_view(), name='category_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
