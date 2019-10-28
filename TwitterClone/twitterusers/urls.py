from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile_view, name='profile'),
    path('myprofile', views.my_profile_view,name='myprofile'),
    path('profile/<str:authorname>/', views.follower_view,name='followerprofile'),
    path('follow/<str:followname>/', views.add_follow, name='addFollow'),
    # path('profile/<str:followname>/unfollow/<str:unfollowname>/',views.remove_follow, name='removeFollow'),
    path('unfollow/<str:unfollowname>/', views.remove_follow,name='removefollow')
]