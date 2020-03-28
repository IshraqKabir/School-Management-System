from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Course
from .choices import timing_choices
from teachers.models import Teacher

def add_courses(request):
    if request.method == 'POST':
        user_type = ""
        try: 
            user_type = request.user.teacher.user_type
        except:
            pass
        try:
            user_type = request.user.student.user_type
        except:
            pass

        if user_type == "student":
            for added_course_title in request.POST:
                courses = Course.objects.all()            
                for course in courses:
                    if added_course_title == course.title:
                        course = Course.objects.get(title=added_course_title)
                        request.user.student.courses.add(course)
                        request.user.student.save()

        elif user_type == "teacher":
            for added_course_title in request.POST:
                courses = Course.objects.all()            
                for course in courses:
                    if added_course_title == course.title:
                        course = Course.objects.get(title=added_course_title)
                        request.user.teacher.courses.add(course)
                        request.user.teacher.save()

        else:
            return redirect('logout')

        # for added_course_title in request.POST:
        #     courses = Course.objects.all()            
        #     for course in courses:
        #         if added_course_title == course.title:
        #             course = Course.objects.get(title=added_course_title)
        #             request.user.user_type.courses.add(course)
        #             request.user.user_type.save()

        return redirect('profile')
    else:
        courses = Course.objects.all()

        context = {
            'courses': courses
        }

        return render(request, 'courses/add_courses.html', context)


def course_list(request):
    added_course = ""
    user_type = ""
    try: 
        user_type = request.user.teacher.user_type
    except:
        pass
    try:
        user_type = request.user.student.user_type
    except:
        pass
    
    if user_type == 'student':
        added_courses = request.user.student.courses.all()

    if user_type == 'teacher':
        added_course = request.user.teacher.courses.all()

    courses = added_course

    context = {
        'added_courses': courses
    }

    return render(request, 'courses/course_list.html', context)


# finish the function later
# it deletes a course from user's added courses 
# data comes from courses/course_list.html
# use slug in urls

def delete_course(request):
    pass


def add_teacher_course(request, teacher_roll):
    all_courses = Course.objects.all()
    teacher = Teacher.objects.get(teacher_roll=teacher_roll)
    
    if request.method == 'POST':
        for data in request.POST:
            print(data)

        return redirect('home')
    else:
        context = {
            'all_courses': all_courses,
            'teacher': teacher,
            'timing_choices': timing_choices
        }
        return render(request, 'courses/add_teacher_courses.html', context)

