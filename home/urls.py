from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/videos/', views.get_videos, name='get_videos'),
    path('video/<str:id>', views.main_preview, name='main_preview'),
    path('save-video-data/', views.save_video_data, name='save_video_data'),
]
