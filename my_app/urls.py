from django.urls import path
from . import views
from my_app import views

urlpatterns=[
    path('',views.home,name='home'),
    #path('new-search/',views.new_search, name='new-search'),
    #path('admin/', admin.site.urls),
    path('new_search', views.new_search, name='new_search'),
    path('<int:pk1>/' ,views.delete, name='delete'),
    path('clearall/',views.clearall, name='clear')



]