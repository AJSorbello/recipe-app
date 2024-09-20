from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from recipe_project.views import login_view, logout_view, logout_success_view
from recipe import views  # Import the views module from the recipe app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add the home view to the URL patterns
    path('recipes/', include('recipe.urls')),  # Include the URLs from the recipe app
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout_success/', logout_success_view, name='logout_success'),  # Add the logout success URL pattern
    path('recipes/about/', views.about, name='about'),  # Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)