from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("This is home page")
    return render(request ,"index.html")
def about(request):
    return HttpResponse("This about my company")
def services(request):
    return HttpResponse("These services are provided by Dewarekhas")
def contact(request):
    return HttpResponse("Contact us")