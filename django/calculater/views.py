import re
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
   
def analyze(request):
    age_of_boy=int(request.GET.get("ba"))
    age_of_girl=int(request.GET.get("ga"))
    print(age_of_boy)
    print(age_of_girl)
    print(type(age_of_boy))
    print(type(age_of_girl))
    if((age_of_boy>=21)and(age_of_girl>=18)):
        print("vaild")
        print("Good Luck For Your Future")
        result='''vaild
        Good Luck For Your Future'''
        
    else:
        print("Invaild")
        result="Invaild"
    dict1={"key1":result} 
    return render(request,'analyze.html',dict1)
    