from django.shortcuts import render
from .models import student
from .serializers import studentserializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def apiall(request):
    stu = student.objects.all()
    # stu = student.objects.all()
    serialize = studentserializer(stu, many = True)
    # json = JSONRenderer().render(serialize.data)
    # return HttpResponse(json, content_type = 'application/json')
    return JsonResponse(serialize.data, safe=False)

@csrf_exempt
def studentapi(request):
    if request.method == 'GET':
        json = request.body
        stream = io.BytesIO(json)
        py = JSONParser().parse(stream)
        id = py.get('id', None)
        if id is not None:
            stu = student.objects.get(id= id)
            serialize = studentserializer(stu)
            json_data = JSONRenderer().render(serialize.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = student.objects.all()
        serialize = studentserializer(stu, many=True)
        json_data = JSONRenderer().render(serialize.data)
        return HttpResponse(json_data, content_type = 'application/json')
    if request.method == 'POST':
        json = request.body
        stream = io.BytesIO(json)
        py = JSONParser().parse(stream)
        deserialize = studentserializer(data=py)
        if deserialize.is_valid():
            deserialize.save()
            msg = {'msg': 'data is created successfully!'}
            rend = JSONRenderer().render(msg)
            return HttpResponse(rend, content_type = 'application/json')
        rend = JSONRenderer().render(deserialize.errors)
        return HttpResponse(rend, content_type = 'application/json')
    if request.method == 'PUT':
        json = request.body
        stream = io.BytesIO(json)
        py = JSONParser().parse(stream)
        id = py.get('id')
        stu = student.objects.get(id= id)
        deserialize = studentserializer(stu, data = py, partial = True)
        if deserialize.is_valid():
           deserialize.save()
           json_data = JSONRenderer().render(deserialize.data)
           return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(deserialize.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'DELETE':
        json = request.body
        stream = io.BytesIO(json)
        py = JSONParser().parse(stream)
        id = py.get('id')
        stu = student.objects.get(id = id)
        stu.delete()
        m = {'msg': 'object deleted successfully!'}
        json_data = JSONRenderer().render(m)
        return HttpResponse(json_data, content_type='application/json')

                    
# def create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_n = JSONParser().parse(stream)   #converts json into python dict
#         serialize = studentserializer(data=python_n) #python dict into model instance(database)
#         if serialize.is_valid():
#             serialize.save()
#             success = {'msg': 'object has been created successfully'}
#             json = JSONRenderer().render(success)
#             return HttpResponse(json, content_type = 'application/json')
#         else:
#             json = JSONRenderer().render(serialize.errors)
#             return HttpResponse(json, content_type = 'application/json')
        