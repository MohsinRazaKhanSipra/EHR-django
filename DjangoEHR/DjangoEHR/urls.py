
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include("patient.urls")),
    path('patientrecords/', include("patientrecords.urls")),
    path('article/', include("article.urls")),
    path('', include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
