from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work_page, name='work_page'),
    path('study/', views.study_page, name='study_page'),
    path('travel/', views.travel_page, name='travel_page'),
    path('health/', views.health_page, name='health_page'),
    path('media/', views.media_page, name='media_page'),
    path('shoes-laundry/', views.shoes_laundry_page, name='shoes_laundry_page'),
    path('register/', views.register_customer, name='registration'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('save-answers/', views.save_answers, name='save_answers'),
]

