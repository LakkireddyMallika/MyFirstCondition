from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d3={'a':10,'b':20}
    return render(request,'a2_first.html',d3)



def a2_second(request):
    d4={'name':'mallika'}
    return render(request,'a2_second.html',d4)
