from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index,name="index"),
    path('contact/contact', views.contact,name="contact"),
    path('', views.signin,name="signin"),
    path('signup', views.signup,name="signup"),
    path('admin', views.admin,name="admin"),
    path('scan', views.scan,name="scan"),

]



