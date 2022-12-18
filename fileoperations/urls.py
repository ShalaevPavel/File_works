from django.urls import path
from . import views

urlpatterns = [path('', views.index, name="index"),
               path('encrypt', views.encrypt, name="encrypt"),
               path('debug', views.debug_page, name="debug"),
               path('build', views.build, name="build"),
               path('api/file/<int:file_id>', views.api_file, name="api_file"),

               ]
