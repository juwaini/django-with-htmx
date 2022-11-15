"""djhx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from example.views import IndexView, ClickToEditView, ClickEditView, WordCreateView, ClickDemo, clicked, WordDemoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('word-demo', WordDemoView.as_view(), name='word-demo'),
    path('word-create', WordCreateView.as_view(), name='word-create'),
    path('click-to-edit', ClickToEditView.as_view(), name='click-to-edit'),
    path('click-edit', ClickEditView.as_view(), name='click-edit'),

    path('click-demo', ClickDemo.as_view(), name='click-demo'),
    path('clicked', clicked, name='clicked'),
]
