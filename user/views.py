from rest_framework import status
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers import UserRegistrationSerializer,CallSerializer,UserLoginSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics,mixins
from user.models import User,Call
from advisor.serializers import AdvisorSerializer
from advisor.models import Advisor
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView 


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_200_OK

        response = {
            'userid': serializer.data['id'],
            'status code' : status_code,
            'token' : serializer.data['token'],
            }
        
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'status code' : status.HTTP_200_OK,
            'userid' : serializer.data['userid'],
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
    
    def get_object(self):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            obj = queryset.get(pk=self.request.user.id)
            self.check_object_permissions(self.request, obj)
            return obj
        except User.DoesNotExist:
            return None


class AdvisorList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = AdvisorSerializer
    queryset = Advisor.objects.all()

    def get(self,request,user_id):
        return self.list(request)


class BookCall(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CallSerializer
    queryset = Call.objects.all()


    def post(self,request,user_id,advisor_id):
        advisor = get_object_or_404(Advisor,id=advisor_id)
        call_data = {
        "user": user_id,
        "advisor_name": advisor.name,
        "advisor_pic": advisor.profile_pic,
        "advisor_id": advisor.id
        }
        serializer = self.serializer_class(data=call_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CallList(generics.GenericAPIView,mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = CallSerializer
    queryset = Call.objects.all()

    def get(self,request,user_id):
        self.queryset = Call.objects.filter(user=user_id)
        return self.list(request)