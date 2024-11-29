from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('show/<int:show_id>/', views.show_detail, name='show_detail'),
    path('show/add/', views.add_show, name='add_show'),
    path('show/update/<int:show_id>/', views.update_show, name='update_show'),
    path('delete/<int:show_id>/', views.delete_show, name='delete_show'),
]

# Media URL settings for images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

