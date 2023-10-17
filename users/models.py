from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password, **extra_fields):
        '''
        Create and return a `User` with superuser (admin) permisissions.
        '''
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password, is_superuser=True)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    matric_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)




# Create your models here.
# class CustomUser (AbstractUser):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     date_of_birth = models.DateField(null=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField(unique=True)
#     matric_number = models.CharField(max_length=20)
#     department = models.CharField(max_length=50)
