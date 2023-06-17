from django.shortcuts import render

# Create your views here.
def calc(request):
    c=''
    try:
        if request.method == 'POST':
            num1=eval(request.POST.get('first'))
            num2=eval(request.POST.get('second'))
            opr=request.POST.get('opr')
            if opr == "+":
                c=num1+num2
            elif opr == "-":
                c=num1-num2
            elif opr == "*":
                c=num1*num2
            elif opr == "/":
                c=num1/num2
    except:
        c="Invalid operator _____"

    return render(request,'calc.html',{'c':c})