from django.shortcuts import render

# Create your views here.


def item(request):
    return render(request, 'html/itempage.html')