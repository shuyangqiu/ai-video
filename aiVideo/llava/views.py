import os
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from .serializer import VideoSerializer
import replicate
from replicate.exceptions import ReplicateError


class FileUploadView(APIView):
    def get(self, request, format=None):
        serializer = VideoSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        video = serializer.data['video']
        prompt = serializer.data['prompt']

        try:
            output = replicate.run(
                os.getenv('REPLICATE_LLAVA_ENDPOINT'),
                input={
                    'video_path': video,
                    'text_prompt': prompt
                }
            )
            return JsonResponse({'output': output})
        except ReplicateError as e:
            return JsonResponse({'error': str(e.detail)}, status=e.status)
        except Exception as e:
            if settings.DEBUG:
                return JsonResponse({'error': str(e)}, status=500)
            return HttpResponse(status=500)

