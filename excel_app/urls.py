from django.urls import path
from .import views
urlpatterns = [
    # path('',views.fileApi.as_view(),name='fileApi')
    path('addfile',views.Fileapi.as_view(),name='fileApi')

]