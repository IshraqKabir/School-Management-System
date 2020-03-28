from django.shortcuts import render, redirect
from .forms import Create_Class_Form

def add_class(request):
    if request.method == 'POST':
        form = Create_Class_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('add_class')
    else:
        form = Create_Class_Form()
        context = {
            'form': form,
        }
        return render(request, 'classes/add_class.html', context)
