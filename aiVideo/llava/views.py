from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from .serializer import VideoSerializer


class FileUploadView(APIView):
    serializer_class = VideoSerializer

    def post(self, request, format=None):
        try:
            video = request.data['video']
            prompt = request.data['prompt']
            return JsonResponse({'prompt': prompt})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
