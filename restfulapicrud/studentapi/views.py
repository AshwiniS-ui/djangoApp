# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # Create your views here.
# from . serializer import StudentSerializer
# from .models import Student
# @api_view(['GET'])
# def stuOverview(request):
#     stu_urls = {
#         'List': '/student-list',
#         'Detail View' : '/student-detail/<int:id>',
#         'Create': '/student-create/<int:id>',
#         'Update': '/student-update/<int:id>',
#         'Delete': '/student-delete/<int:id>',
#
# }
#     return Response(stu_urls);
#
# @stuOverview(['GET'])
# def showAll(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import student
from . serializer import studentSerializer

class studentView(APIView):
    def get(self, request):
        stu1 = student.objects.all()
        stu2 = studentSerializer(stu1, many=True)
        return Response(stu2.data)

    def post(self, request):
        a = request.data
        a1 = studentSerializer(data=a)
        a1.is_valid()
        a1.save()
        return Response(a)

    def put(self, request):
        a = request.GET.get("id")
        a1 = student.objects.get(id=a)
        a3 = request.data
        a2 = studentSerializer(a1, data=a3)
        a2.is_valid()
        a2.save()
        return Response(a3)

    def delete(self, request):
        a = request.GET.get("id")
        a1 = student.objects.get(id=a)
        a1.delete()
        return Response("sucessfully deleted")
