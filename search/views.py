from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher

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
