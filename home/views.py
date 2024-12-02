from django.shortcuts import render
from home.models import CrousalHome,VideoAPIResponse


from django.http import JsonResponse
import requests
from django.core.paginator import Paginator
import json
def fetch_videos_from_api(params):
    """Fetch videos from the external API and append the response."""
    url = 'https://www.eporner.com/api/v2/video/'
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Get the current stored response or create a new one if it doesn't exist
        try:
            video_data = response.json()
            total_videos = video_data.get('total_count', 0)
            videos = video_data.get('videos', [])

            # Check if there's an existing record, and if so, append to it
            video_api_response = VideoAPIResponse.objects.first()  # Or use another method to select the record
            if video_api_response:
                # Append new videos to the existing data
                existing_data = video_api_response.response_data
                existing_data = existing_data if existing_data else '[]'
                existing_videos = json.loads(existing_data)

                # Append new videos to the existing list
                existing_videos.extend(videos)

                # Save the updated data back to the database
                video_api_response.response_data = json.dumps(existing_videos)
                video_api_response.save()
            else:
                # If no record exists, create a new one with the fetched data
                VideoAPIResponse.objects.create(
                    response_data=json.dumps(videos)  # Store only the video list initially
                )

            return video_data

        except Exception as e:
            print(f"Error handling response: {e}")
            return None
    else:
        return None


def get_videos(request):
    """Handle video fetching and pagination."""
    query = request.GET.get('query', 'boobs')  # Default query
    page = int(request.GET.get('page', 1))  # Current page
    per_page = int(request.GET.get('per_page', 20))  # Videos per page
    params = {
        'method': 'search',
        'query': query,
        'per_page': per_page,
        'page': page,
        'thumbsize': 'big',
        'order': 'top-weekly',
        'type.': 1,
        'lq': 1,
        'format': 'json',
    }

    api_response = fetch_videos_from_api(params)

    if api_response:
        total_count = api_response.get('total_count', 0)
        videos = api_response.get('videos', [])

        # Paginate manually since we fetch from an external API
        paginator = Paginator(videos, per_page)
        current_page_videos = paginator.get_page(page)

        return JsonResponse({
            'videos': list(current_page_videos),
            'current_page': page,
            'total_pages': paginator.num_pages,
            'total_count': total_count,
        })

    return JsonResponse({'error': 'Failed to fetch videos'}, status=500)


def home(request):
    context={
    }
    return render(request, 'home/home.html',context)

import random

def main_preview(request, id):
    session_key = request.session.session_key
    if not session_key:
        return JsonResponse({'error': 'Session not found'}, status=404)
    
    response_entry = VideoAPIResponse.objects.filter(session_key=session_key).first()
    
    if not response_entry:
        return JsonResponse({'error': 'No response entry found'}, status=404)
    
    try:
        response_data = json.loads(response_entry.response_data)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=500)
    
    videos = response_data.get("videos", [])
    matching_video = next((video for video in videos if video.get("id") == id), None)
    matching_video["keywords"] = matching_video["keywords"].split(",")
    
    default_keywords = ["boobs", "sexy", "teen18", "hot","chubby cute babe"]
    valid_keywords = [keyword for keyword in matching_video.get('keywords', []) if keyword]
    if len(valid_keywords) < 2:
        valid_keywords = default_keywords
    keywords_suggestion=random.sample(valid_keywords, 2)

    recommeded_video=keywords_suggestion[0]
    more_video=keywords_suggestion[1]

    context={
        'specified_video': matching_video,
        'recommeded_video':recommeded_video,
        'more_video':more_video,
    }

    return render(request, 'home/main_preview.html',context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoAPIResponse
import json
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now, timedelta
from .models import VideoAPIResponse

@csrf_exempt
def save_video_data(request):
    """Save or append the API response data into the model."""
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)

            # Get the session key for the current user
            session_key = request.session.session_key
            if not session_key:
                request.session.create()  # Create session if not already created
                session_key = request.session.session_key
            
            # Retrieve the VideoAPIResponse for the current session or create a new one
            response_entry, created = VideoAPIResponse.objects.get_or_create(session_key=session_key)
            
            if not created:
                # If entry already exists, append the new videos
                existing_data = json.loads(response_entry.response_data)  # Convert string to JSON
                existing_data['videos'].extend(data['videos'])  # Append videos to the existing list
                response_entry.response_data = json.dumps(existing_data)  # Convert back to string
                response_entry.save()
            else:
                # If new entry, save the provided data
                response_entry.response_data = json.dumps(data)
                response_entry.save()
            
            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            print(f"Error saving video data: {e}")
            return JsonResponse({'error': 'Failed to save video data'}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)


from django.contrib.sessions.models import Session
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import VideoAPIResponse

@receiver(post_delete, sender=Session)
def delete_video_data_on_session_expiry(sender, instance, **kwargs):
    """Delete VideoAPIResponse when the session is destroyed."""
    session_key = instance.session_key
    VideoAPIResponse.objects.filter(session_key=session_key).delete()









def redtube_preview(request, id):
    url = f'https://lust.scathach.id/redtube/get?id={id}'
    response = requests.get(url)
    data = response.json().get('data', {})
    source = response.json().get('source', '')
    assets = response.json().get('assets', [])
    
    default_keywords = ["boobs", "sexy", "teen18", "hot","chubby cute babe"]
    valid_keywords = [keyword for keyword in data.get('tags', []) if keyword]
    if len(valid_keywords) < 2:
        valid_keywords = default_keywords
    keywords_suggestion=random.sample(valid_keywords, 2)

    recommeded_video=keywords_suggestion[0]
    more_video=keywords_suggestion[1]
    print(more_video)
    return render(request, 'home/redtube_preview.html', {'data': data,'source': source, 'assets': assets,'more_video': more_video,'recommeded_video':recommeded_video,})

def redtube(request):
    context={
    }
    return render(request, 'home/redtube.html',context)

