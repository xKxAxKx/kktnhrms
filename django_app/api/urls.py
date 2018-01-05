from django.urls import path

from api.views import AboutGetView, SNSGetView, ProductGetView, InquiryPostView

urlpatterns = [
    path('about/', AboutGetView.as_view(), name='about'),
    path('sns/', SNSGetView.as_view({'get': 'list'}), name='sns_list'),
    path('sns/<str:name>/', SNSGetView.as_view({'get': 'retrieve'}),
         name='sns_get'),
    path('product/', ProductGetView.as_view({'get': 'list'}),
         name='product_list'),
    path('product/<int:product_id>/',
         ProductGetView.as_view({'get': 'retrieve'}),
         name='product_get'),
    path('inquiry/', InquiryPostView.as_view(),
         name='inquiry')
]
