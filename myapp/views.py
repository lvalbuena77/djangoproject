from django.shortcuts import render, redirect # Para que me devuelva un html con el template que le indique en la vista de esta app myapp
from django.http import HttpResponse, JsonResponse # Para que me devuelva un json
from .models import Project, Task # Importo los modelos de la app myapp para poder usarlos en las vistas de esta app myapp  
from django.shortcuts import get_object_or_404 # Para que me devuelva un 404 si no encuentra el objeto que busco en la base de datos
from django.shortcuts import render # Para que me devuelva un html con el template que le indique en la vista de esta app myapp
from .forms import CreateNewTask, CreateNewProject # Importo el formulario que cree en forms.py

# Create your views here.
def index(request):
    #return HttpResponse("Index Page")
    title = "Djando course!!"
    return render(request, "index.html", {"title": title}) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template

def about(request):
    #return HttpResponse("<h2>About Page</h2>")
    username = "Luis"
    return render(request, "about.html", {"username": username}) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
    
def hello(request, username):
    print (username)
    return HttpResponse("<h2>Hello %s</h2>" % username) # %s Lo reemplaza por el valor de username que se le pasa por la url en el navegador.

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()   
    #return JsonResponse(projects, safe=False) # safe=False es para que no me de error al pasarle una lista de diccionarios a JsonResponse y me devuelva un json
    #return render(request, "projects.html") # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
    return render(request, "projects/projects.html", {"projects": projects}) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
    
def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id) # Si no encuentra el objeto que busco en la base de datos me devuelve un 404
    #task = Task.objects.get(title=title)
    #return HttpResponse("task: %s" % task.title)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks}) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
    #return render(request, "tasks.html") # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
    
def create_task(request):
    if request.method == "GET":
      # Show the interface
       return render(request, "tasks/create_task.html",
                  {'form': CreateNewTask()}) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
    else:
      # Process the form data and save it to the database (if valid) and redirect to the index page
        Task.objects.create(title=request.POST["title"], 
                            description=request.POST["description"],
                            project_id=2)
        return redirect("tasks") # Le paso el nombre de la url que quiero que me redireccione

def create_project(request):
   if request.method == "GET":
      # Show the interface
       return render(request, "projects/create_project.html",
                  {'form': CreateNewProject()}) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template
   else:
       # Process the form data and save it to the database (if valid) and redirect to the index page
       Project.objects.create(name=request.POST["name"])
       return redirect("projects")
   
def project_detail(request, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id) # Si no encuentra el objeto que busco en la base de datos me devuelve un 404
    tasks = Task.objects.filter(project_id=id) # Me devuelve una lista de objetos de tipo Task que tienen el project_id igual al id que le paso por la url
    return render(request, "projects/detail.html", 
                  {"project": project,
                   "tasks": tasks
                   }) # Le paso el request, el template que quiero que me devuelva y el diccionario con los datos que quiero que me muestre en el template