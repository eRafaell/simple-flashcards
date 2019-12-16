from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users.views import main_page_view, register, login, logout, profile, ProfileUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile-update/', ProfileUpdate.as_view(), name='profile-update'),

    # REST FRAMEWORK URLS
    path('api/users/', include('users.api.urls', 'users_api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
