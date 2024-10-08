"""URL configuration for strife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    # channels included by servers
    # path("emoji/", include(("strife.apps.emoji.urls", "emoji"), namespace="emoji")),
    # path("messages/", include(("strife.apps.messages.urls", "messages"), namespace="messages")),
    # path("reactions/", include(("strife.apps.reactions.urls", "reactions"), namespace="reactions")),
    # path("roles/", include(("strife.apps.roles.urls", "roles"), namespace="roles")),
    path("servers/", include(("strife.apps.servers.urls", "servers"), namespace="servers")),
    path("", include(("strife.apps.users.urls", "users"), namespace="users")),
    path("", include(("strife.apps.home.urls", "home"), namespace="home")),
    # static/
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    # media/
]
