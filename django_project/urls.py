"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from questions.views import (start_proccess,list_view,send_form,contacts_view,
                             about_view,result_view,result_ruk,result_ruk_seo,
                             result_ruk_index,exportdate

                             )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^indes/', list_view),
    url(r'^contacts/', contacts_view),
    url(r'^result/', result_view),
    url(r'^about/', about_view),
    url(r'^$', send_form,name='form'),
    url(r'^result_ruk/',result_ruk),
    url(r'^result_ruk_seo/',result_ruk_seo),
    url(r'^result_ruk_index/',result_ruk_index),
    url(r'^exportdate/',exportdate)
]
