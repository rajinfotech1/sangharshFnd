
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
    path('update_user/<int:id>/', views.update_user_admin, name="update_user"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('ajax/', views.ajax_fun, name="ajax"),
    path('profile/', views.profile, name="profile"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
