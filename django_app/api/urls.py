from django.urls import path

from api.views import AboutGetView, SNSGetView

urlpatterns = [
    path('about/', AboutGetView.as_view()),
    path('sns/', SNSGetView.as_view({'get': 'list'})),
    path('sns/<str:name>/', SNSGetView.as_view({'get': 'retrieve'}))
]
