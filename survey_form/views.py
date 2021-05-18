from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    

def result(request):
    context = {
        "name" :request.POST["name"],
        "dojo" : request.POST["dojo"],
        "lang" :request.POST["language"],
        "comments" : request.POST["comments"],
    }
    return render(request, 'submissions.html', context)

