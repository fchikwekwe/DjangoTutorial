from django.http import HttpResponse

def index(resquest):
    return HttpResponse("Hello, world. You're at the polls index.")