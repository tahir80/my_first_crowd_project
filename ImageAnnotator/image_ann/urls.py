from django.urls import path
from image_ann import views


urlpatterns = [
  path('hit/<int:pk>',views.hit, name = 'hit'),
]
