from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('',views.PostsList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create_post'),
    path('by/<str:username>/',views.UserPosts.as_view(),name='for_user'),
    path('delete/<int:pk>/',views.DeleteViwe.as_view(),name='delete'),
    path('by/<str:username>/<int:pk>/',views.PostDetail.as_view(),name='single'),

]
