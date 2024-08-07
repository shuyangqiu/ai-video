from rest_framework.serializers import Serializer, URLField, CharField


class VideoSerializer(Serializer):
    video = URLField()
    prompt = CharField(allow_blank=True)

    class Meta:
        fields = ['video', 'prompt']
