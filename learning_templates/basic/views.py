from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'basic/index.html',context_dict)


def other(request):
    return render(request,'basic/other.html')


def relativework(request):
    return render(request,'basic/relative work.html')
