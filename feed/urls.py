from django.urls import path
from .views import HomePageView
from .views import PostDetailView
from .views import PostView

app_name = "feed"

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/', PostView.as_view(), name="post"),
]
