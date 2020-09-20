"""mungpot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
import community.views
import community.urls
import account.urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',community.views.home, name="home"),
    path('account', include(account.urls)),
    path('community', include(community.urls)),
    path('new', community.views.new, name='new'),
    path('createfeed', community.views.createfeed, name='createfeed'),
    path('detail/<int:feed_id>',community.views.detail, name='detail'),
    path('edit/<int:feed_id>',community.views.edit,name="edit"),
    path('feedupdate/<int:feed_id>',community.views.feedupdate,name="feedupdate"),
    path('postdelete/<int:feed_id>',community.views.feeddelete,name="delete"),
    path('commentcreate/<int:feed_id>', community.views.commentcreate, name='commentcreate'),
    path('commentdelete/<int:feed_id>/<int:comment_id>', community.views.commentdelete, name='commentdelete'),
    path('profile', community.views.profile, name="profile"),
    path('map', community.views.map, name="map"),
    path('loc', community.views.loc, name="loc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
