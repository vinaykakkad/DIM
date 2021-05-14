from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    ActivateAccountView,
    ForgotPasswordView,
    PasswordSetterView,
    logout_view,
    profile_view,
)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("forgot_password/", ForgotPasswordView.as_view(), name="get_email"),
    path("set_password/", PasswordSetterView.as_view(), name="set_password"),
    path(
        "set_password/<username64>/<token>/",
        PasswordSetterView.as_view(),
        name="set_password",
    ),
    path("profile/<username>", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),
]
