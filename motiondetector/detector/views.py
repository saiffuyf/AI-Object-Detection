from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .motiondetector import generate_frames
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

# def video_feed(request):
#     return StreamingHttpResponse(generate_frames(),
#         content_type='multipart/x-mixed-replace; boundary=frame')
def video_feed(request):
    return StreamingHttpResponse(generate_frames(get_status),
        content_type='multipart/x-mixed-replace; boundary=frame')

is_running = False

def toggle_motion(request):
    global is_running
    is_running = not is_running
    return JsonResponse({'is_running': is_running})

def get_status():
    return is_running
