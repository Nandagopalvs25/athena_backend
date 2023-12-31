from django.urls import path
from .views import EventView,CoordinatorView,PosterView

urlpatterns = [
    path("/event/", EventView.as_view(), name="index"),
    path("/coordinator/", CoordinatorView.as_view(), ),
     path("/posters/", PosterView.as_view(), ),
    
]