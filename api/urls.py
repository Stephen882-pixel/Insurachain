from django.urls import path
from .views import RegiserUserView,LoginView,PolicyListCreateView,ClaimDetailView,ClaimListCreateView


urlpatterns  = [
    path('register/',RegiserUserView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('policies/',PolicyListCreateView.as_view(),name='policy-list-create'),
    path('claims/',ClaimListCreateView.as_view(),name='claim-list-create'),
    path('claims/<int;pk>/',ClaimDetailView.as_view(),name='claim-detail')
]