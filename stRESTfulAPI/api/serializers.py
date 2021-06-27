from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import FileUpload



class FileSerializer(serializers.Serializer):
    video = serializers.FileField(max_length=None, allow_empty_file=False)


class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=None, allow_blank=False, trim_whitespace=True)
