from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from user.models import User,Call



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER



class UserRegistrationSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    # userid = serializers.CharField(max_length=255, read_only=True)

    def get_token(self,user):
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        return jwt_token
        

    class Meta:
        model = User
        fields = ['id','email', 'name','password','token' ]
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        token = jwt_token
        return user



class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    userid = serializers.CharField(max_length=255, read_only=True)
    queryset = ''

    def validate(self, data):
        queryset = ''
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'userid':user.id,
            'token': jwt_token
        }



class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['id','user', 'advisor_name','advisor_pic','advisor_id','booking_time'] 