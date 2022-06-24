from django.shortcuts import render


# views of app.

def index(request):
    return render(request, 'index.html')
