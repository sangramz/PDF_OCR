from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dash, name='dash'),
    path('uploaded-files/', views.uploadedfiles, name='uploadedfiles'),
    path('doc-view/', views.docviews, name='docviews'),
    path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)