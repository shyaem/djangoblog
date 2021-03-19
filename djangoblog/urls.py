
from django.contrib import admin
from django.urls import path,include
from . import views
from articles import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import urls
from articles import views as article_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',article_views.article_list,name="home"),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('about/',views.about),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)