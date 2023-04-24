from django.shortcuts import render
import sys
# Create your views here.
def compiler(request):
    return render(request,"compiler.html")

def runn(request):
    if request.method=="POST":
        code = request.POST['code-area']
    
        term = request.POST["term"]
       
        try:
            original_code = sys.stdout
            sys.stdout = open("f.txt","w")

            if term != "":
                exec(f"n=int({term});{code}")
            else:
                exec(code)
            sys.stdout.close()
            sys.stdout = original_code
            op = open("f.txt","r").read() 
            print(op)
        except Exception as e:
            sys.stdout = original_code
            op = e
    return render(request,"compiler.html",{"code":code,"op":op})