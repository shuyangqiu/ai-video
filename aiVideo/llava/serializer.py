from rest_framework.serializers import Serializer, URLField, CharField


class VideoSerializer(Serializer):
    video = URLField()
    prompt = CharField(default='')

    class Meta:
        fields = ['video', 'prompt']
