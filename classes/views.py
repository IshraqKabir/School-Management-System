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
        day_instance = Day.objects.get(name=day_name)
        timing_id = request.POST['timing']
        timing_instance = Timing.objects.get(id=timing_id)
        batch_id = request.POST['batch']
        batch_instance = Batch.objects.get(id=batch_id)
        room_id = request.POST['room']
        room_instance = Room.objects.get(id=room_id)

        classes = Class.objects.all()
        batch_classes = classes.filter(batch__id__iexact=batch_id)

        for single_class in classes:
            if single_class.day.name == day_name.name:
                print("day matched")
                if single_class.timing.time == timing_instance.time:
                    if room_instance.name is not None:
                        if single_class.room.name == room_instance.name:
                            error_message = 'Slot not available'
                            form = Create_Class_Form()
                            context = {
                                'form': form,
                                'error_message': error_message
                            }            
                            print("slot not available")
                            return render(request, 'classes/add_class.html', context)
                    else:
                        if single_class.room.number == room_instance.number:
                            error_message = 'Slot not available'
                            form = Create_Class_Form()
                            context = {
                                'form': form,
                                'error_message': error_message
                            }            
                            print("slot not available")
                            return render(request, 'classes/add_class.html', context)

            else:
                print(single_class.day.name)
                print("day does not match")
        
        # for single_class in batch_classes:
        #     if single_class.timing.time == timing_instance.time:
        #         if single_class.day.id == day_instance.id: 
        #             error_message = 'The Batch already has another class at this slot'
        #             form = Create_Class_Form()
        #             context = {
        #                 'form': form,
        #                 'error_message': error_message
        #             }            
        #             print("slot not available")
        #             return render(request, 'classes/add_class.html', context)
        form.save()
        return redirect('home')
    else:
        form = Create_Class_Form()
        context = {
            'form': form,
        }
        return render(request, 'classes/add_class.html', context)






