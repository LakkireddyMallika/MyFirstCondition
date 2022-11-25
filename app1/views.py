from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d1={'a':10,'b':20,}
    return render(request,'a1_first.html',d1)


def a1_second(request):
    d2={'a':200,'b':100,'c':500}
    return render(request,'a1_second.html',d2)
