from django.shortcuts import render

# Create your views here.
def traggic(request):
    d={'in2':'poor Bahuballi got killed by KATTAPA'}
    return render(request,'traggic.html',context=d)
