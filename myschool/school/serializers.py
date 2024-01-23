from rest_framework import serializers
from django.http import JsonResponse
from school.models import Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
def First_student(request):
    students = Student.objects.all()
    serializer = SchoolSerializer(students, many=True)  # Make sure to set many=True for multiple instances
    return JsonResponse(serializer.data, safe=False)        