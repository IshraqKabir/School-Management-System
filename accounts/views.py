from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from students.models import Student
from .forms import RegisterForm
from students.forms import StudentRegisterForm
from teachers.forms import TeacherRegisterForm
from django.views.generic.edit import UpdateView
from courses.models import Course

def register_student(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)

        if form.is_valid() and student_form.is_valid():
            
            user = form.save()
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('login')
        else:
            return redirect('register_student')

    else:
        form = RegisterForm()
        student_form = StudentRegisterForm(request.POST)


        context = {
            'form': form,
            'student_form': student_form
        }

        return render(request, 'accounts/register_student.html', context)

def register_teacher(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        teacher_form = TeacherRegisterForm(request.POST)

        if form.is_valid() and teacher_form.is_valid():
            user = form.save()
            user.save()

            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('login')
        else:
            return redirect('register_teacher')

    else:
        form = RegisterForm()
        teacher_form = TeacherRegisterForm(request.POST)


        context = {
            'form': form,
            'teacher_form': teacher_form
        }

        return render(request, 'accounts/register_teacher.html', context)


def profile(request):
    user_type = ""
    try: 
        user_type = request.user.teacher.user_type
    except:
        pass
    try:
        user_type = request.user.student.user_type
    except:
        pass

    context = {
        'user_type': user_type
    }
    
    return render(request, 'accounts/profile.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now looged out')
        return redirect('login')


def update(request):
    user_type = ""
    try: 
        user_type = request.user.teacher.user_type
    except:
        pass
    try:
        user_type = request.user.student.user_type
    except:
        pass
    if request.method == 'POST':
        if request.POST['username'] != '':
            request.user.username = request.POST['username']
        if request.POST['email'] != '':
            request.user.email = request.POST['email']
        if user_type == 'student':
            if request.POST['first_name'] != '':
                request.user.student.first_name = request.POST['first_name']
            if request.POST['last_name'] != '':
                request.user.student.last_name = request.POST['last_name']
            if request.POST['student_roll'] != '':
                request.user.student_roll = request.POST['student_roll']
            request.user.save()
            request.user.student.save()
        elif user_type == 'teacher':
            if request.POST['first_name'] != '':
                request.user.teacher.first_name = request.POST['first_name']
            if request.POST['last_name'] != '':
                request.user.teacher.last_name = request.POST['last_name']
            if request.POST['teacher_roll'] != '':
                request.user.teacher_roll = request.POST['teacher_roll']
            request.user.save()
            request.user.student.save()

        return redirect('profile')
    else:
        return render(request, 'accounts/update.html')



