from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('members/', views.member_view, name='members'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('forum/', views.forum_view, name='forum'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]