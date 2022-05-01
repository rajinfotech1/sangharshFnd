
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from new_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_request, name="register"),
    path('view_members/', views.view_members, name="view_members"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('view_card/<int:id>/', views.view_card, name="print"),
    path('delete_user/<int:id>/', views.delete_user, name="delete_user"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
