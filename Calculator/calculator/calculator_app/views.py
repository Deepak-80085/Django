from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculator(request):
    result = ''
    expression = ''
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # Using eval() for simplicity, but it's not secure for production
            result = eval(expression)
        except:
            result = 'Error'
    return render(request, 'calculator_app/index.html', {'result': result, 'expression': expression})