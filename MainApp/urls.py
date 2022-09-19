from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import converter

app_name = "Internship"
urlpatterns = [
     path("", converter.index, name = "index"),
     path("view/list/", converter.list, name = "list"),
     path("new/upload/", converter.upload, name = "upload"),
]