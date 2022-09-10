from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('viewEmp', views.viewEmp, name='viewEmp'),
    path('addEmp', views.addEmp, name='addEmp'),
    path('removeEmp', views.removeEmp, name='removeEmp'),
    path('filterEmp', views.filterEmp, name='filterEmp'),
    path('updateEmp', views.updateEmp, name='updateEmp'),
    path('updateEmp2', views.updateEmp2, name='updateEmp2'),
    path('updateEmp3', views.updateEmp3, name='updateEmp3'),
    path('search', views.search, name='search'),
]