from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings


def upload_image(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            image_file = request.FILES['file']
            save_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
            with open(save_path, 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
            return JsonResponse({'message': 'File uploaded successfully!', 'file_path': save_path})
        return JsonResponse({'message': 'No file received!'}, status=400)
    return render(request, 'upload.html')

def sample(request):
    return render(request, 'main.html')
