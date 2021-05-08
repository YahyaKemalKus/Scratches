from django.shortcuts import HttpResponse


def view1(request):
    return HttpResponse('<h1> view1 page </h1>')

def view2(request):
    return HttpResponse('<h1> view2 page </h1>')