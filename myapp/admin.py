from django.contrib import admin
from .models import Project, Task # Import the models you want to register here (in this case, Project and Task)

# Register your models here.
admin.site.register(Project) # Register the models here (in this case, Project)
admin.site.register(Task) # Register the models here (in this case, Task)