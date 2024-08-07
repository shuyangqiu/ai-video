import os

from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from .serializer import VideoSerializer
import replicate


class FileUploadView(APIView):
    serializer_class = VideoSerializer

    def post(self, request, format=None):
        try:
            video = request.data['video']
            prompt = request.data['prompt']

            output = replicate.run(
                os.getenv('REPLICATE_LLAVA_ENDPOINT'),
                input={
                    'video_path': video,
                    'text_prompt': prompt
                }
            )
            return JsonResponse({'output': output})
        except Exception as e:
            if settings.DEBUG:
                return JsonResponse({'error': str(e)}, status=500)
            else:
                return HttpResponse(status=500)
