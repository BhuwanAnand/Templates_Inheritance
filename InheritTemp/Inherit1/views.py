from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'D:/BhuwanData/Desktop/BhuwanDjango/InheritTemp/templates/index.html',)

def child(request):
    return render(request,'D:/BhuwanData/Desktop/BhuwanDjango/InheritTemp/templates/child.html',)


def child1(request):
    return render(request,'D:/BhuwanData/Desktop/BhuwanDjango/InheritTemp/templates/child1.html',)