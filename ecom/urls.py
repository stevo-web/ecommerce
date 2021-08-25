from ariadne.contrib.django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(schema=schema))),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('shop/', include('shop.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
