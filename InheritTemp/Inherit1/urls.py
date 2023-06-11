from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
     path('child/',views.child,name='child'),
     path('child1/',views.child1,name='child1'),
  
  
]