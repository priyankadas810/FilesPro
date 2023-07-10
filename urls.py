from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name = 'index'),
    path('fileupload', views.fileupload, name='fileupload'),
    path('listfiles', views.listfiles, name='listfiles'),
    path('pdfconverter', views.pdfconverter, name='pdfconverter'),
    path('listofpdfs', views.listofpdfs, name='listofpdfs'),
    #path('wordconverter', views.wordconverter, name='wordconverter'),

]





