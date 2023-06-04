"""eCommerceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Shopping Bag"
admin.site.site_title = "ShoppingBag Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("eCommApp.urls")),
    path("eComAuth/", include("eComAuth.urls")),
    path("", TemplateView.as_view(template_name="signup.html")),
    path("accounts/", include("allauth.urls")),
    path("logout", LogoutView.as_view()),
    path("verification/", include("verify_email.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
