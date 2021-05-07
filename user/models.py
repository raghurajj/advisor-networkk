import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email,name, password=None):
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email,name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = "login"

    
    

class  Call(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='calls')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    advisor_name = models.CharField(max_length=50, unique=False)
    advisor_pic = models.URLField(max_length = 200)
    advisor_id = models.UUIDField()
    booking_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "call"