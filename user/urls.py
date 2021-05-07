from django.urls import path
from user.views import UserRegistrationView,UserLoginView,AdvisorList,BookCall
from user.views import CallList

urlpatterns = [
    path('register', UserRegistrationView.as_view()),
    path('login', UserLoginView.as_view()),
    path('<str:user_id>/advisor', AdvisorList.as_view()),
    path('<str:user_id>/advisor/booking', CallList.as_view()),
    path('<str:user_id>/advisor/<str:advisor_id>', BookCall.as_view()),
    ]