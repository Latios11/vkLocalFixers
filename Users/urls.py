from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='index'),
    path('about', views.about, name='about'),
    path('orders', views.orders, name='orders'),
    path('search', views.search, name='search'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('login', views.signin, name='login'),
    path('register', views.signup, name='register'),
    path('logout',views.signout,name='logout'),
    path('test',views.test,name='test'),
    path('category/<str:service_name>', views.category, name='category'),
    path('quickview/<int:service_id>',views.quick,name='quickview'), 
    path('proceed/<int:service_id>',views.proceed,name='proceed'),
    path('checkout/<int:sid>/<int:total>',views.checkout,name='checkout'),
    path('cancel/<int:oid>',views.cancel,name='cancel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)