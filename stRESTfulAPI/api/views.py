from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from api.serializers import FileSerializer, QuestionSerializer
from rest_framework import viewsets
from uuid import uuid4
import random
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
import subprocess, sys


@permission_classes([AllowAny])
class FileUploadViewSet(viewsets.ViewSet):


    def create(self, request):
        serializer_class = FileSerializer(data=request.data)
        if 'video' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            handle_uploaded_file(request.FILES['video'])
            return Response(status=status.HTTP_201_CREATED)

def handle_uploaded_file(f):
    with open(r'~\data\current_question.txt', 'r') as file:
        uuid = file.readlines()[1]

    f.name = f"{uuid}.webm"
    with open(fr"~\data\WEBM\{f.name}", 'wb+') as destination:
            #Using a for-loop instead of read() ensures that large files don't
            #overwhelm system memory
        for chunk in f.chunks():
            destination.write(chunk)


@permission_classes([AllowAny])
class QuestionRandomizer(viewsets.ViewSet):



    def list(self, request):
        class QuestionFormatter:
            def __init__(self, selected_question, id):
                self.question = selected_question
                self.uuid = id

        questions = []
        with open(r'~\data\questions.txt', 'r') as file:
            questions = [line for line in file.readlines()]

        uuid = uuid4().__str__()
        selection = random.choice(questions)
        selection = QuestionFormatter(selected_question=selection, id=uuid)

        serializer = QuestionSerializer(selection)

        with open(r'~\data\current_question.txt', 'w') as tmp:
            tmp.write(selection.question)
            tmp.write(selection.uuid)

        return Response(serializer.data)


@permission_classes([AllowAny])
class Results(viewsets.ViewSet):

    def list(self, request):
        class ResultFormatter:
            def __init__(self, metrics):
                self.results = metrics

        scores = subprocess.run(r"powershell.exe python 'main.py'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        results = ResultFormatter(scores.stdout)
        serializer = ResultSerializer(results.results)
        return Response(serializer.data)

