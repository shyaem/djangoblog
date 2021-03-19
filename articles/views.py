from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.contrib.auth.signals import user_logged_in
from . import forms


def article_list(request):
    now = timezone.now()
    articles = Article.objects.all().order_by('-date')
    context = {'articles': articles, 'now': now}
    return render(request, 'articles/article_list.html', context)


@login_required(login_url='/accounts/login/')
def article_detail(request, subject):
    articles = Article.objects.get(subject=subject)
    return render(request, 'articles/article_detail.html', {'articles': articles})


@login_required(login_url='/accounts/login/')
def create_view(request):
    if request.method == 'POST':
        form = forms.CreateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
        else:
            return render(request, 'articles/create.html', {'form': form})
    else:
        form = forms.CreateForm()
        return render(request, 'articles/create.html', {'form': form})
