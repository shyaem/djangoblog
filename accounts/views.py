from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponse
from . models import Detail
from . forms import ProfileForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user.username)
            print(user)
            login(request, user)
            return redirect('articles:list')

    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')


def create_view(request, fullname):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.fullname = request.user
            instance.save()
            str1 = '/accounts/profile/{0}/'.format(request.user.username)
            return redirect(str1)
        else:
            return render(request, 'accounts/alterprofile.html', {'form': form, 'fullname': fullname})

    else:
        if(str(request.user) == fullname):
            try:
                pro = Detail.objects.get(fullname=fullname)
                return HttpResponse('already profile exists')
            except Exception as e:
                form = ProfileForm()
                return render(request, 'accounts/alterprofile.html', {'form': form, 'fullname': fullname})
        else:
            return HttpResponse('you are not allowed for this')


def update_view(request, fullname):
    pro = Detail.objects.get(fullname=fullname)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=pro)
        if form.is_valid():
            str1 = '/accounts/profile/{0}/'.format(request.user.username)
            return redirect(str1)
        else:
            return render(request, 'accounts/editprofile.html', {'form': form, 'fullname': fullname})

    else:
        if(str(request.user) == fullname):
            form = ProfileForm(instance=pro)
            return render(request, 'accounts/editprofile.html', {'form': form, 'fullname': fullname})
        else:
            return HttpResponse('you are not allowed for this')


@login_required(login_url='/accounts/login/')
def profile_view(request, fullname):
    try:
        if(str(request.user) == fullname):
            print(type(str(request.user)))
            print(type(fullname))
            pro = Detail.objects.get(fullname=fullname)
            context = {'pro': pro}
            return render(request, 'accounts/profile.html', context)
        else:
            return HttpResponse('you are not allowed for this')

    except Exception as e:
        return redirect('/accounts/create_view/{0}/'.format(request.user.username))


@login_required(login_url='/accounts/login/')
def userprofile_view(request, fullname):
    if(str(request.user) == fullname):
        str1 = '/accounts/profile/{0}/'.format(request.user.username)
        return redirect(str1)
    else:
        try:
            pro = Detail.objects.get(fullname=fullname)
            context = {'pro': pro}
            return render(request, 'accounts/userprofile.html', context)
        except Exception as e:
            return render(request, 'accounts/nullprofile.html')
            # return HttpResponse("user still didn't create profile")
