from django.shortcuts import render
from .models import Batch
from classes.models import Class

def batch_list(request):
    all_batches = Batch.objects.all()

    context = {
        'all_batches': all_batches
    }
    return render(request, 'batches/batch_list.html', context)

def batch_class_list(request, id):
    batch_instance = Batch.objects.get(id=id)
    batch_classes = Class.objects.filter(batch__name__iexact=batch_instance.name)

    context = {
        'batch_classes': batch_classes
    }
    return render(request, 'classes/batch_class_list.html', context)



