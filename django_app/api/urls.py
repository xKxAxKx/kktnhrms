from django.urls import path

from api.views import AboutGetView

urlpatterns = [
    path('about/', AboutGetView.as_view()),
]
