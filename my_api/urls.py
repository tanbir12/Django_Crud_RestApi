from django.urls import path
from .views import StudentView

urlpatterns = [
    path('myapp/',StudentView.as_view()),
    path('myapp/<int:id>',StudentView.as_view()),
]