from django.urls import path
from .views import user_login, user_logout, user_register, home, UserProfileDetailView, UserProfileListView

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile'),
    path('user_profiles/', UserProfileListView.as_view(), name='userprofile_list'),
    path('', home, name='home'),
]
