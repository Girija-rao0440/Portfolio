from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from my_profile.views import home
from blog import views
urlpatterns = [
path('',views.blogs),
]
