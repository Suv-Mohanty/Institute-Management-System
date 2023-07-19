from django.contrib import admin
from .models import Courses

class AdminCourse(admin.ModelAdmin):
    display=['course','fee','duration','start_date','trainer_name','trainer_exp','training_mode']

admin.site.register(Courses,AdminCourse)
