from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializers import *

# @api_view(['GET'])
# def getAllStudents(request):
#     student = Student.objects.all()
#     serializer = StudentSerializer(student, context={'request': request}, many=True)
#     return Response(serializer.student)

# @api_view(['GET'])
# def getStudent(request, pk):
#     if request.method == 'GET':
#         try:
#             student = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student, context={'request': request}, many=True)
#         return Response(serializer.student)

@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def students_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)