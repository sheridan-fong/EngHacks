from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from api.serializers import FileSerializer, QuestionSerializer
from rest_framework import viewsets
from uuid import uuid4
import random



class FileUploadViewSet(viewsets.ViewSet):


    def create(self, request):
        serializer_class = FileSerializer(data=request.data)
        if 'video' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            handle_uploaded_file(request.FILES.getlist('video'))
            return Response(status=status.HTTP_201_CREATED)

def handle_uploaded_file(f):
    for x in f:
        uuid = uuid4().__str__()
        x.name = f"{uuid}.webm"
        with open(fr"C:\Users\bsun7\Desktop\EngHack\COMRADE\data\WEBM\{x.name}", 'wb+') as destination:
            #Using a for-loop instead of read() ensures that large files don't
            #overwhelm system memory
            for chunk in x.chunks():
                destination.write(chunk)


class QuestionRandomizer(viewsets.ViewSet):



    def list(self, request):
        class QuestionFormatter:
            def __init__(self, selected_question):
                self.question = selected_question


        questions = []
        with open(r'C:\Users\bsun7\Desktop\EngHack\COMRADE\data\questions.txt', 'r') as file:
            questions = [line for line in file.readlines()]


        selection = random.choice(questions)
        selection = QuestionFormatter(selected_question=selection)
        serializer = QuestionSerializer(selection)

        ### write current question to a txt so we can keep track of the current question ??

        return Response(serializer.data)
