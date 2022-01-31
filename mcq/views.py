from django.shortcuts import render
from rest_framework import serializers
# Create your views here.
# import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# import local data
from .serializers import OptionSerializer, QuestionsSerializer, QuestionSetsSerializer
from .models import Option, Question_Sets, Questions

# create a viewset


class OptionViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Option.objects.all()

    # specify serializer to be used
    serializer_class = OptionSerializer

    def post(self, request):
        serializer_class = OptionSerializer(data=request.data)
        if serializer_class.is_valid():

            serializer_class.save()
            return Response(serializer_class.data, status="CREATED")
        return Response(serializer_class.errors, status="Invalid")


class QuestionViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Questions.objects.all()

    # specify serializer to be used
    serializer_class = QuestionsSerializer

    def post(self, request):
        serializer_class = QuestionsSerializer(data=request.data)
        if serializer_class.is_valid():

            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionSetsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Question_Sets.objects.filter(section__startswith='A')

    # specify serializer to be used
    serializer_class = QuestionSetsSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = QuestionSetsSerializer(data=request.data)
        if serializer_class.is_valid():

            serializer_class.save()
            return Response("CREATED")
        return Response("INVALID")
