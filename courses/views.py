from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from courses.models import Course

def add_courses(request):
    if request.method == 'POST':
        for added_course_title in request.POST:
            courses = Course.objects.all()
            
            for course in courses:
                if added_course_title == course.title:
                    course = Course.objects.get(title=added_course_title)
                    request.user.student.courses.add(course)
                    request.user.student.save()

        return redirect('profile')
    else:
        courses = Course.objects.all()

        context = {
            'courses': courses
        }

        return render(request, 'courses/add_courses.html', context)
