from django.urls import path
from eComAuth import views

urlpatterns = [
    path("signupPage/", views.signupPage, name="signupPage"),
    path("loginPage/", views.loginPage, name="loginPage"),
    path("logoutPage/", views.logoutPage, name="logoutPage"),
    path("activate/<uidb64>/<token>", views.activate.as_view(), name="activate"),
    path(
        "changePasswordPage/",
        views.changePasswordPage.as_view(),
        name="changePasswordPage",
    ),
    path(
        "setNewPassword/<uidb64>/<token>",
        views.setNewPassword.as_view(),
        name="setNewPassword",
    ),
]
