import json
from service.state_service import StateService
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def find_by_name(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        if name != "":
            print(f'Name: {name}')
            state_service = StateService()
            result = state_service.find(name)
            print(type(result))

            json_obj = json.dumps(result)
            return HttpResponse(json_obj, content_type="application/json")
        else:
            return HttpResponse("Name required")
