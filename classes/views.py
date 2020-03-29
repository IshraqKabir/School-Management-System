from django.shortcuts import render, redirect
from .forms import Create_Class_Form
from days.models import Day
from timings.models import Timing
from classes.models import Class
from batches.models import Batch
from rooms.models import Room

def add_class(request):
    if request.method == 'POST':
        form = Create_Class_Form(request.POST)
        day_id = request.POST['day']
        day_name = Day.objects.get(id=day_id)
        timing_id = request.POST['timing']
        timing_instance = Timing.objects.get(id=timing_id)
        batch_id = request.POST['batch']
        batch_instance = Batch.objects.get(id=batch_id)
        room_id = request.POST['room']
        room_instance = Room.objects.get(id=room_id)

        classes = Class.objects.all()

        for single_class in classes:
            if single_class.day.name == day_name.name:
                print("day matched")
                if single_class.timing.time == timing_instance.time:
                    if room_instance.name is not None:
                        if single_class.room.name == room_instance.name:
                            if single_class.batch.name == batch_instance.name:
                                print("slot not available")
                                return redirect('add_class')
                    else:
                        if single_class.room.number == room_instance.number:
                            if single_class.batch.name == batch_instance.name:
                                print("slot not available")
                                return redirect('add_class')

            else:
                print(single_class.day.name)
                print("day does not match")
        form.save()
        return redirect('home')
    else:
        form = Create_Class_Form()
        context = {
            'form': form,
        }
        return render(request, 'classes/add_class.html', context)






