import os
from decouple import config


from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.contrib import messages
from django.db.models import Q

from .forms import LoginForm, RegisterForm, ProfileForm
from .models import Account, Profile
from .utils import generate_token, only_letters


EMAIL_HOST_USER = config("EMAIL_HOST_USER")


# Generating token and sending mail for activating account
def send_activation_email(request, user, email):
    current_site = get_current_site(request)
    subject = "CEL-Activate your account"
    context = {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": generate_token.make_token(user),
    }
    message = render_to_string("account/activate_link.html", context)
    plain_message = strip_tags(message)

    send_mail(subject, plain_message, EMAIL_HOST_USER, [email], html_message=message)


class RegisterView(View):
    """
    Register View
    Renders registration page, verifies new user.
    On verification sends activation link.
    """

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "account/register.html", context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        fullname = request.POST.get("fullname")
        password = request.POST.get("password")
        type = request.POST.get("type")
        email = request.POST.get("email")

        if not only_letters(username):
            messages.error(
                request,
                "Username should only contain lower-case alphabets \
                    or numbers without spaces",
            )
            return redirect("register")

        try:
            user = Account.objects.get(Q(username=username) | Q(email=email))
        except Exception as identifier:
            user = None

        if user:
            messages.error(request, "Username/Email already exists!!")
            return redirect("register")

        user = Account(
            username=username,
            email=email,
            password=password,
            fullname=fullname,
            type=type,
        )
        user.set_password(password)
        user.save()

        # Email verification is done by encoding user's primary key and generating a token
        send_activation_email(request, user, email)

        messages.info(
            request,
            "Verification link sent. Check your email! Please wait for 5-7 minutes and check for SPAM/Promotions Folder in Gmail!",
        )
        return redirect("login")


class LoginView(View):
    """
    Login View
    Renders login page and authenticates user.
    """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")

        form = LoginForm()
        context = {"form": form}
        return render(request, "account/login.html", context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = authenticate(request, username=username, password=password)
        except Exception as identifier:
            user = None

        if user:
            if not user.is_activated:
                messages.error(request, "Account not activated. Contact administrator")
                return redirect("login")
            login(request, user)
            messages.info(request, "Logged in successfully.")
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password.")
            return redirect("login")


class ActivateAccountView(View):
    """
    Email Activation.
    Verification by decoding primary key and checking token
    """

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is None:
            messages.error(request, "Verification failed!!")
        else:
            if generate_token.check_token(user, token):
                user.is_activated = True
                user.save()
                messages.info(request, "Link verified successfully!!")
            else:
                messages.error(request, "Verification failed!!")
        return redirect("login")


class ForgotPasswordView(View):
    """
    Forgot password view
    Getting email of the user and sending reset link.
    """

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "account/reset_email.html", context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        try:
            user = Account.objects.get(email=email)
        except Exception as identifier:
            user = None

        if user is None:
            messages.error(request, "Enter valid email address")
            return redirect("forgot_password")
        else:
            current_site = get_current_site(request)
            subject = "DogeIN Reset Password"

            context = {
                "user": user,
                "domain": current_site.domain,
                "encoded_username": urlsafe_base64_encode(force_bytes(user.username)),
                "token": generate_token.make_token(user),
            }
            message = render_to_string("account/reset_link.html", context)
            plain_message = strip_tags(message)

            send_mail(
                subject,
                plain_message,
                EMAIL_HOST_USER,
                [user.email],
                html_message=message,
            )
            messages.info(
                request,
                "Reset link sent. Check your email! Please wait for 5-7 minutes and check for SPAM/Promotions Folder in Gmail!",
            )
            return redirect("login")


class PasswordSetterView(View):
    """
    Resetting new password
    Getting new password and updating it.
    """

    def get(self, request, username64, token, *args, **kwargs):
        try:
            username = force_text(urlsafe_base64_decode(username64))
            user = Account.objects.get(username=username)
        except Exception as identifier:
            user = None

        if user is None:
            messages.error(request, "Link verification failed1!!")
            return redirect("get_email")
        else:
            if generate_token.check_token(user, token):
                context = {"username": user.username}
                return render(request, "account/new_password.html", context)
            else:
                messages.error(request, "Link verification failed!!")
                return redirect("get_email")

    def post(self, request, *args, **kwargs):
        password = request.POST.get("password")
        username = request.POST.get("username")

        user = Account.objects.get(username=username)
        user.set_password(password)
        user.save()

        messages.info(request, "Password changed successfully!!")
        return redirect("login")


def profile_view(request, username):
    if request.method == "POST":
        if request.user.completed_profile:
            form = ProfileForm(request.POST, instance=request.user.profile)
        else:
            form = ProfileForm(request.POST)

        if form.is_valid():
            if request.user.completed_profile:
                Profile.objects.filter(user=request.user).delete()
            else:
                request.user.completed_profile = True
                request.user.save()

            profile = form.save(commit=False)
            profile.user = request.user
            print(profile)
            profile.save()
            form.save_m2m()

            return redirect("profile", username=username)

        messages.error(
            request, "There was some error while adding the post, please try again!!"
        )
        return redirect("forum")

    profile = None
    user = None
    form = ProfileForm

    try:
        user = Account.objects.get(username=username)
    except Exception as identifier:
        pass

    try:
        profile = user.profile
        form = ProfileForm(instance=profile)
    except Exception as identifier:
        pass

    context = {"profile": profile, "same": request.user == user, "form": form}

    return render(request, "account/profile.html", context)


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("login")
