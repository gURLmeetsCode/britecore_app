from django.conf.urls import url
from accounts.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
]
