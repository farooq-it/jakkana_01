from django.shortcuts import render

# Create your views here.
def traggic(request):
    d={'in1':'Bahuballi announced as KING'}
    return render(request,'traggic.html',context=d)