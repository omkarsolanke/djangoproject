import re
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    
    length=int(request.GET.get(length))
    base=int(request.GET.get(base))
    
    hypotenous=(length*length+base*base)/2
    print(hypotenous)
    dict1={"key1":hypotenous} 
    
    
    return render(request,'analyze.html',dict1)