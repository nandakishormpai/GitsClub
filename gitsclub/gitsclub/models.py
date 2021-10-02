from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Custom UserManager Model

class MemberManager(BaseUserManager):
    def create_user(self, email, githubuserId, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not githubuserId:
            raise ValueError('Users must have a github username')

        user = self.model(
            email=self.normalize_email(email),
            githubuserId=githubuserId,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, githubuserId, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            githubuserId=githubuserId,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, githubuserId, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            githubuserId=githubuserId,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# Custom User Model


class Member(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    githubuserId = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    objects = MemberManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['githubuserId']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

# 'User' Model is an unregistered user here


class User(models.Model):
    userId = models.CharField(max_length=50)
    profilePic = models.CharField(max_length=200)
    name = models.CharField(max_length=50, null=True)
    bio = models.CharField(max_length=1000, null=True)
    starCount = models.IntegerField()
    repoCount = models.IntegerField()
    followerCount = models.IntegerField()
    contributionCount = models.IntegerField(default=0)
    groupName = models.CharField(
        max_length=50, default="HackerNoobs", null=True)
    namegroupid = models.CharField(
        max_length=100, default="name_HackerNoobs", null=True)

    def __str__(self):
        return self.userId
