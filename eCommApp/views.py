from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from eCommApp.models import productsDb, myOrderDb, contactUsDb
from math import ceil
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please Login and Explore")
    allProducts = []
    catProds = productsDb.objects.values("productCategory", "id")
    cats = {item["productCategory"] for item in catProds}
    for cat in cats:
        prod = productsDb.objects.filter(productCategory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod, range(1, nSlides), nSlides])
    parameters = {"allProducts": allProducts}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        obj = contactUsDb(Name=name, Email=email, Subject=subject, Message=message)
        obj.save()
        messages.success(request, "Email Sent Successfully")
    return render(request, "index.html", parameters)


def cart(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return redirect("/eComAuth/loginPage")
    if request.method == "POST":
        itemJson = request.POST.get("itemsJson")
        firstName = request.POST.get("firstName")
        secondName = request.POST.get("secondName")
        inputEmail = request.POST.get("inputEmail")
        inputPhone = request.POST.get("inputPhone")
        inputAddress = request.POST.get("inputAddress")
        inputAddress2 = request.POST.get("inputAddress2")
        inputCity = request.POST.get("inputCity")
        inputState = request.POST.get("inputState")
        inputPin = request.POST.get("inputPin")
        orders = myOrderDb(
            Items_Json=itemJson,
            First_Name=firstName,
            second_Name=secondName,
            Email=inputEmail,
            phone=inputPhone,
            Address1=inputAddress,
            Address2=inputAddress2,
            City=inputCity,
            State=inputState,
            Pin_code=inputPin,
        )
        orders.save()
        messages.success(request, "Order Placed Successfully")
    return render(request, "cart.html")

