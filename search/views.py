from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from classes.models import Class

def search_students(request):
    return render(request, 'search/search_students.html')


def search_teachers(request):
    return render(request, 'search/search_teachers.html')



def search_results_students(request):
    student_query = Student.objects.order_by('student_roll')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        student_roll = request.POST['student_roll']
    
        if first_name is not None:
            student_query = student_query.filter(first_name__icontains=first_name)
    
        if last_name is not None:
            student_query = student_query.filter(last_name__icontains=last_name)
    
        if student_roll is not None:
            student_query = student_query.filter(student_roll__icontains=student_roll)

    context = {
        'students': student_query
    }
    return render(request, 'search/search_results_students.html', context)


def search_results_teachers(request):
    teacher_query = Teacher.objects.order_by('teacher_roll')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        teacher_roll = request.POST['teacher_roll']
    
        if first_name is not None:
            teacher_query = teacher_query.filter(first_name__icontains=first_name)
    
        if last_name is not None:
            teacher_query = teacher_query.filter(last_name__icontains=last_name)
    
        if teacher_roll is not None:
            teacher_query = teacher_query.filter(teacher_roll__icontains=teacher_roll)

    context = {
        'teachers': teacher_query
    }
    return render(request, 'search/search_results_teachers.html', context)


def search_classes(request):
    return render(request, 'search/search_classes.html')


def search_results_classes(request):
    class_query = Class.objects.all()
    if request.method == 'POST':
        course_title = request.POST['course_title']
        teacher_username = request.POST['teacher_username']
        teacher_roll = request.POST['teacher_roll']
        course_day = request.POST['course_day']
        class_timing = request.POST['timing']
        batch = request.POST['batch']
        room = request.POST['room']

        class_query = Class.objects.all()

        if course_title:
            # print('it is none')
            class_query = class_query.filter(course__title__icontains=course_title)
        elif teacher_username:
            class_query = class_query.filter(teacher__user__username__iexact=teacher_username)
        elif teacher_roll:
            class_query = class_query.filter(teacher__teacher_roll__icontains=teacher_roll)
        elif course_day:
            class_query = class_query.filter(day__name__icontains=course_day)
        elif batch:
            class_query = class_query.filter(teacher__batch__icontains=batch)
        elif class_timing:
            class_query = class_query.filter(timing__time__iexact=class_timing)
        elif room:
            class_query = class_query.filter(room__number__iexact=room)
        
        context = {
            'classes': class_query
        }
        return render(request, 'search/search_results_classes.html', context)