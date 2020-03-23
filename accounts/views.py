from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from students.models import Student
from .forms import RegisterForm
from students.forms import StudentRegisterForm
from django.views.generic.edit import UpdateView
from courses.models import Course

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)

        if form.is_valid() and student_form.is_valid():
            user = form.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('login')
        else:
            return redirect('register')

    else:
        form = RegisterForm()
        student_form = StudentRegisterForm(request.POST)


        context = {
            'form': form,
            'student_form': student_form
        }

        return render(request, 'accounts/register.html', context)


def profile(request):
    return render(request, 'accounts/profile.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now looged out')
        return redirect('login')


def update(request):
    if request.method == 'POST':
        if request.POST['username'] != '':
            request.user.username = request.POST['username']
        if request.POST['email'] != '':
            request.user.email = request.POST['email']
        if request.POST['first_name'] != '':
            request.user.student.first_name = request.POST['first_name']
        if request.POST['last_name'] != '':
            request.user.student.last_name = request.POST['last_name']
        if request.POST['student_roll'] != '':
            request.user.student.student_roll = request.POST['student_roll']

        request.user.save()
        request.user.student.save()
        return redirect('profile')
    else:
        return render(request, 'accounts/update.html')



