from django.urls import path
from users import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('upload_img/', views.image_request, name='image_request')
]
