from django.http import HttpResponse

def hello_world(req):
    return HttpResponse("Hello, django")

def hello_school(req):
    return HttpResponse("Hello, school")
