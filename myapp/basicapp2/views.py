from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basicapp2/index.html')


def about(request):
    return render(request, 'basicapp2/about.html')
    
def project(request):
    return render(request, 'basicapp2/project.html')
    
def contacts(request):
    return render(request, 'basicapp2/contacts.html')    

def relative(request):
    return render(request, 'basicapp2/relative_url_templates.html')
