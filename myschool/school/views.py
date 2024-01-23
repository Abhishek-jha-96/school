from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from school.models import Student
from django.core.serializers import serialize
from school.serializers import SchoolSerializer  # Import your serializer

@csrf_exempt
def First_student(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        transformed_data = {
            "name": data["name"],
            "age": data["age"],
            "gender": data["gender"],
            "physics_Total_marks": data["marks"]["physics"][1],
            "chemistry_Total_marks": data["marks"]["chemistry"][1],
            "maths_Total_marks": data["marks"]["maths"][1],
            "physics_obtained_marks": data["marks"]["physics"][0],
            "chemistry_obtained_marks": data["marks"]["chemistry"][0],
            "maths_obtained_marks": data["marks"]["maths"][0],
        }

        serializer = SchoolSerializer(data=transformed_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    

    
    elif request.method == 'GET':
        data = Student.objects.all()
        result = []
        for student in data:
            physics_percentage = (student.physics_obtained_marks / student.physics_Total_marks) * 100
            chemistry_percentage = (student.chemistry_obtained_marks / student.chemistry_Total_marks) * 100
            maths_percentage = (student.maths_obtained_marks / student.maths_Total_marks) * 100

            overall_percentage = (physics_percentage + chemistry_percentage + maths_percentage) / 3

            student_data = {
                'name': student.name,
                'age': student.age,
                'gender': student.gender,
                'physics_percentage': physics_percentage,
                'chemistry_percentage': chemistry_percentage,
                'maths_percentage': maths_percentage,
                'overall_percentage': overall_percentage
            }

            result.append(student_data)

        print(data[0])
        serialized_data = serialize('json', data)
        return JsonResponse({'data': result}, safe=False)

@csrf_exempt
def Second_student(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        transformed_data = {
            "name": data['first_name'] + " " + data['last_name'],
            "age": data['years_old'],
            "gender": None,
            "physics_Total_marks": data['scores']['total_marks'][0],
            "chemistry_Total_marks": data['scores']['total_marks'][1],
            "maths_Total_marks": data['scores']['total_marks'][2],
            "physics_obtained_marks": data['scores']['marks_obtained'][0],
            "chemistry_obtained_marks": data['scores']['marks_obtained'][1],
            "maths_obtained_marks": data['scores']['marks_obtained'][2]
        }
        serializer = SchoolSerializer(data=transformed_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)        
    else:
        return JsonResponse({'error': 'Bad Request - Only POST method is allowed.'}, status=400)