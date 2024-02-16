from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, name,usertype, password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            usertype=usertype,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,usertype, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            usertype=usertype
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




# Create your models here.

class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=30)
    password=models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    bio=models.CharField(max_length=500)
    dp=models.CharField(max_length=255)
    usertype = models.CharField(max_length=10)
    verified=models.CharField(max_length=5,default='NO')
    createdAt=models.DateField(default=timezone.now)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","usertype"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
