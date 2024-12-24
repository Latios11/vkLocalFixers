from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('splogin',views.spsignin,name= 'splogin'), 
    path('spregister', views.spsignup, name='spregister'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('splogout',views.splogout,name='splogout'),
    path('spupdate', views.spupdate, name='spupdate'),
    path('addservices', views.addservices, name='addservices'),
    path('services',views.services,name='services'),
    path('delete/<int:service_id>',views.delete_service,name='delete_service'),
    path('back',views.back,name='back'),
    path('orders',views.sporders,name='sporders'),
    path('complete/<int:oid>',views.complete,name='complete'),
    path('corders',views.corders,name='corders'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)