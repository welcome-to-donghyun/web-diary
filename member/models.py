from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, user_img=None, password=None):
        user = MyUser(email = email,
                      nickname = nickname)
        user.set_password(password)
        user.is_active = True
        user.save()

        return user

    def create_superuser(self, email, nickname, password):
        user = MyUser(email = email,
                      nickname = nickname)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save()

        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    user_img = models.ImageField(blank=True,
                                 upload_to="user_img")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("nickname",)

    objects = MyUserManager()

    def get_short_name(self):
        return self.nickname

    def get_full_name(self):
        return self.nickname
