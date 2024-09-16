from django.urls import path
from . import views
urlpatterns = [
    path('', views.postlist,name='postlist'),
     path('create/', views.postcreate,name='postcreate'),
      path('<int:post_id>edit/', views.postedit,name='postedit'),
     path('<int:post_id>delete/', views.postdelete,name='postdelete'),
     path('register/', views.Register,name='register'),
]
 