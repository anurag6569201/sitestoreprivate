from django.db import models

class CrousalHome(models.Model):
    RATING=[
        (1, '#'),
        (2, '##'),
        (3, '###'),
        (4, '####'),
        (5, '#####'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    logo_link=models.CharField(max_length=400,default="https://static.vecteezy.com/system/resources/thumbnails/008/174/695/small_2x/loading-circle-icon-loading-gif-loading-screen-gif-loading-spinner-gif-loading-animation-loading-free-video.jpg")
    rating=models.IntegerField(default=0,choices=RATING)
    visiting_link=models.CharField(max_length=200)
    

from django.db import models

class VideoAPIResponse(models.Model):
    """Model to store the raw JSON response from the video API."""
    session_key = models.CharField(max_length=255, unique=True)
    response_data = models.TextField()  # Field to store the JSON response
    created_at = models.DateTimeField(auto_now_add=True)
