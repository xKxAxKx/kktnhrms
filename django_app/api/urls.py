from django.urls import path

from api.views import AboutGetView, SNSGetView, ProductGetView

urlpatterns = [
    path('about/', AboutGetView.as_view()),
    path('sns/', SNSGetView.as_view({'get': 'list'})),
    path('sns/<str:name>/', SNSGetView.as_view({'get': 'retrieve'})),
    path('product/', ProductGetView.as_view({'get': 'list'})),
    path('product/<int:product_id>/',
         ProductGetView.as_view({'get': 'retrieve'})),
]
