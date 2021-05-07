from django.shortcuts import render
from advisor.models import Advisor
from advisor.serializers import AdvisorSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics,mixins
from rest_framework import permissions
from django.shortcuts import get_object_or_404

class AdvisorList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = AdvisorSerializer
    queryset = Advisor.objects.all()

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
 