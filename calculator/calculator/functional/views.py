from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def operation(request):
    return render(request,'index.html')
def result(request):
    num1 = int(request.GET.get('first_number', 0))
    num2 = int(request.GET.get('second_number', 0))
    operation = request.GET.get('operation')

    if operation == 'add':
        ans = num1 + num2
    elif operation == 'subtract':
        ans = num1 - num2
    elif operation == 'multiply':
        ans = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            ans = num1 / num2
        else:
            return HttpResponse("Error")
    else:
        return HttpResponse("Invalid operation.")

    return render(request, 'result.html', {'ans': ans})