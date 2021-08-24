from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'homepage.html',context=my_dict)
