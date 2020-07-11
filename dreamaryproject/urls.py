from django.contrib import admin
from django.urls import path
from page import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('introduce/', views.introduce, name = "introduce"),
    path('profile/<int:designer_id>', views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)