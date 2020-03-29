from django.urls import path
from .views import (
    batch_list,
    batch_class_list
)
urlpatterns = [
    path('list/', batch_list, name="batch_list"),
    path('batch/<int:id>/', batch_class_list, name="batch_class_list"),
]


