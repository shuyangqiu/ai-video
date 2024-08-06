from rest_framework.serializers import Serializer, FileField, CharField

class VideoSerializer(Serializer):
    video = FileField()
    prompt = CharField(allow_blank=True)
    class Meta:
        fields = ['video', 'prompt']
