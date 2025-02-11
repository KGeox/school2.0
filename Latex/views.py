from django.shortcuts import render, redirect
from .forms import LatexForm
from .models import LatexExpression

# Create your views here.

def latex_input(request):
    if request.method == 'POST':
        form = LatexForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('latex_output')
    else:
        form = LatexForm()
    return render(request, 'latex_input.html', {'form': form})

def latex_output(request):
    latex_expressions = LatexExpression.objects.all()
    return render(request, 'latex_output.html', {'expressions': latex_expressions})