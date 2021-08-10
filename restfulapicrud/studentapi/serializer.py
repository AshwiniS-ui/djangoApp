# from rest_framework import serializers
# from . models import Student
#
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         field = "__all__"


from rest_framework import serializers
from . models import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ("userId", "name", "department", "cgpa")