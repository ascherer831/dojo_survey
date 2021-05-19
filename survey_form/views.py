from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def process(request):
    request.session['name']= request.POST['name']
    request.session['dojo']= request.POST['dojo']
    request.session['lang']= request.POST['language']
    request.session['comments']= request.POST['comments']
    print(request.session)
    return redirect('/result')
    

def result(request):
    # context = {
    #     "name" :request.POST["name"],
    #     "dojo" : request.POST["dojo"],
    #     "lang" :request.POST["language"],
    #     "comments" : request.POST["comments"],
    # }
    print(request.session())
    return render(request, 'submissions.html')

