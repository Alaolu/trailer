from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from trailerweb.views import home
from trailerweb.views import detail



urlpatterns = [
    path('', home, name='anasayfa'),
    path ('detail/', detail, name='detay'),
]