# for rendering functions/pages
from lib2to3.pgen2.tokenize import generate_tokens
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse


# for authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# for showing messages
from django.contrib import messages

# importing current site
from django.contrib.sites.shortcuts import get_current_site

# activate user account
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes

# getting token from utils.py
from .utils import tokenGenerator, generateToken

# for emails
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings


# class function
from django.views.generic import View

# sendinG MAIL
import threading

# reset password generators
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# threading
class emailThread(threading.Thread):
    def __init__(self, emailMessage):
        self.emailMessage = emailMessage
        threading.Thread.__init__(self)

    def run(self):
        self.emailMessage.send()


# threading


# signup page functions
def signupPage(request):
    if request.method == "POST":
        signupEmail = request.POST.get("email")
        signupPassword = request.POST.get("password")
        confirmPassword = request.POST.get("confPassword")
        # checking the passwords are same
        if signupPassword != confirmPassword:
            messages.error(request, "Incorrect password")
            return redirect("signupPage")

        # checking the email exists or not
        try:
            if User.objects.get(username=signupEmail):
                messages.error(request, "Email already has been taken")
                return redirect(signupPage)
        except:
            pass
        # end of checking the email exists or not

        myUser = User.objects.create_user(signupEmail, signupEmail, signupPassword)

        # making account inactive
        myUser.is_active = False
        myUser.save()

        currentSite = get_current_site(request)
        emailSub = "Activate your account"
        emailMess = render_to_string(
            "auth/activate.html",
            {
                "user": myUser,
                "domain": "127.0.0.1:8000",
                "uid": urlsafe_base64_encode(force_bytes(myUser.pk)),
                "token": generateToken.make_token(myUser),
            },
        )
        emailMessage = EmailMessage(
            emailSub,
            emailMess,
            settings.EMAIL_HOST_USER,
            [signupEmail],
        )

        # sending email
        emailThread(emailMessage).start()
        messages.success(request, "Activate your account from email")
        return render(request, "auth/login.html")

    return render(request, "auth/signup.html")


# activating from mail
class activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generateToken.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Activation successful")
            return redirect("loginPage")
        else:
            return render(request, "auth/activationfail.html")


# end of activating from mail


def loginPage(request):
    if request.method == "POST":
        loggedEmail = request.POST.get("email")
        loggedPassword = request.POST.get("password")
        myUser = authenticate(username=loggedEmail, password=loggedPassword)

        if myUser is not None:
            login(request, myUser)
            messages.success(request, "Continue shopping " + loggedEmail)
            return render(request, "index.html")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("loginPage")
    return render(request, "auth/login.html")


def logoutPage(request):
    logout(request)
    messages.info(request, "Logout Successful!! Please login to explore")
    return redirect(loginPage)


# reset password function
class changePasswordPage(View):
    def get(self, request):
        return render(request, "auth/resetPassword.html")

    def post(self, request):
        email = request.POST["email"]
        user = User.objects.filter(email=email)

        if user.exists():
            currentSite = get_current_site(request)
            emailSub = "Reset your password"
            message = render_to_string(
                "auth/resetUserPassword.html",
                {
                    "domain": "127.0.0.1:8000",
                    "uid": urlsafe_base64_encode(force_bytes(user[0].pk)),
                    "token": PasswordResetTokenGenerator().make_token(user[0]),
                },
            )
            emailmessage = EmailMessage(
                emailSub, message, settings.EMAIL_HOST_USER, [email]
            )
            emailThread(emailmessage).start()

            messages.info(request, "Reset link send to your Email ")
            return render(request, "auth/resetPassword.html")


class setNewPassword(View):
    def get(self, request, uidb64, token):
        context = {"uidb64": uidb64, "token": token}
        try:
            userId = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=userId)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.warning(request, "Password reset link is invalid")
                return render(request, "auth/resetPassword.html")
        except UnicodeDecodeError as identifier:
            pass
        return render(request, "auth/setNewPassword.html",context)

    def post(self, request, uidb64, token):
        context = {
            "uidb64": uidb64,
            "token": token,
        }
        password = request.POST["Password"]
        confirmPassword = request.POST["confPassword"]
        if password != confirmPassword:
            messages.error(request, "Password is not matching")
            return render(request, "auth/setNewPassword.html")
        try:
            userId = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=userId)
            user.set_password(password)
            user.save()
            messages.success(
                request, "Password reset success Please login with the new password"
            )
            return redirect("/auth/loginPage/")
        except UnicodeDecodeError as identifier:
            messages.error(request, "something went wrong")
            return render(request, "auth/resetPassword")


# end of reset password function
