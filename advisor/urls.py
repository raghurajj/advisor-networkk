from django.conf.urls import url
from advisor.views import AdvisorList

urlpatterns = [
    url(r'^advisor', AdvisorList.as_view()),
    ]