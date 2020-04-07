from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    x = "asdfasdf"
    context = {
        'x': x
    }
    return render(request, 'home.html', context)

def profile_of_others(request, id):
    profile = User.objects.get(id=id)
    user_type = ""
    try: 
        user_type = profile.teacher.user_type
    except:
        pass
    try:
        user_type = profile.student.user_type
    except:
        pass
    context = {
        'profile': profile,
        'user_type': user_type
    }
    return render(request, 'pages/profile_of_others.html', context)
