from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/videos/', views.get_videos, name='get_videos'),
    path('video/<str:id>', views.main_preview, name='main_preview'),
    path('save-video-data/', views.save_video_data, name='save_video_data'),

    path('redtube', views.redtube, name='redtube'),
    path('redtube/<str:id>', views.redtube_preview, name='redtube_preview'),
    path('proxy-redtube-api/', views.proxy_redtube_api, name='proxy_redtube_api'),

    path('pornhub', views.pornhub, name='pornhub'),
    path('pornhub/<str:id>', views.pornhub_preview, name='pornhub_preview'),

    path('xhamster', views.xhamster, name='xhamster'),
    path('xhamster/<str:id>', views.xhamster_preview, name='xhamster_preview'),


    path('xvideos', views.xvideos, name='xvideos'),
    path('xvideos/<str:alt1>/<str:alt2>', views.xvideos_preview, name='xvideos_preview'),
]
