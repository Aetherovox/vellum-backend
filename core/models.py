from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None,**kwargs):
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have an email')

        user = self.model(username=username, email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        if username is None:
            raise TypeError('Superusers must have a username')
        if email is None:
            raise TypeError('Superusers must have an email')
        if password is None:
            raise TypeError('Superusers must have a password')
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32,unique=True,db_index=True)
    email = models.EmailField(unique=True,db_index=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

