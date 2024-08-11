from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    email = request.session.get("email",None)
    user_email = email
    is_already_exists = False
    error = None
    if request.method == "POST":
        from_user = request.POST.get("email",None)
        if from_user:
            is_already_exists = User.objects.filter(email=from_user).exists()
        if not is_already_exists:
            email = email or from_user
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)

            if not user_email:
                request.session["email"] = email

            if username and password and email:
                is_user = User.objects.filter(username=username).exists()
                if is_user:
                    error = "User already Exists!"
                else:
                    User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    del request.session["email"]
                    return redirect("/login/")
        else:
            error = "User with email already Exists !"
    return render(request,"register.html",{"email":email,"error":error})

def loginn(request):
    if request.user.is_authenticated:
        return redirect("/")
    error = None
    if request.method == "POST":
        username = request.POST["username_email"]
        password = request.POST["password"]

        if username and password:
            credentials = {"email":username,"password":password} if "@" in username else {"username":username,"password":password}
            user = authenticate(
                request,**credentials
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    error = "Disabled Account !"
            else:
                error = "Credentials Doesnot Match !"
            
    return render(request,"login.html",{"error":error})

def logout(request):
    if request.method == "POST" and request.user.is_authenticated:
        auth_logout(request)
        message = "success"
        return JsonResponse({"res":message})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,"profile.html",context)

# @login_required
# def profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }

#     return render(request, 'users/profile.html', context)