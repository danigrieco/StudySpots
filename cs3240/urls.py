from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

"""
URL configuration for cs3240 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = "cs3240"

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name='home'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
    path('approval/',views.admin_approval, name="approval"),
    path('places/',views.PlacesView.as_view(), name="places"),
    path('suggest/',views.suggest, name="suggest"),
    path('suggestion/',views.suggest_place, name="suggestion"),
    path('recommend/',views.RecommendView.as_view(), name="recommend"),
    path('places/<int:place_id>/', views.see_place, name="see_place"),
    path('places/<int:place_id>/review', views.ReviewForm, name="ReviewForm")
]
