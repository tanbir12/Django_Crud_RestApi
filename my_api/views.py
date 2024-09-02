from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentView(APIView):
    def get(self,request,student_id=None):
        if student_id:
            item = models.Students.objects.get(id==student_id)
            serializer = serializers.StudentSerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        
        items = models.Students.objects.all()
        serializer = serializers.StudentSerializer(items,many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    
    def patch(self,request,student_id=None):
        item = models.Students.objects.all()
        serializer = serializers.StudentSerializer(item,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,student_id=None):
        item = models.Students.objects.filter(student_id)
        print(item)
        item.delete()
        return Response({"status":"success","data":item},status=status.HTTP_200_OK)
