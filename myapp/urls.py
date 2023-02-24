from django.urls import path
from . import views # import views from myapp. El . significa que es de la misma carpeta


urlpatterns = [ path("", views.hello),
    path("about/", views.about)
]