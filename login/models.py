from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
      def create_user(self, name, email, day_of_birth, password=None):
          if not email:
               raise ValueError("Precisa ter um email")
          
          email = self.normalize_email(email)
          user = User.objects.create(
               name=name,
               email = email,
               day_of_birth = day_of_birth,
               password = password
          )

          user.set_password(password)
          user.save(using=self.__db)

          return user

class User(AbstractBaseUser):
      name = models.CharField(max_length=255, blank=False, null=False)
      email = models.EmailField(unique=True,blank=False, null=False)
      day_of_birth = models.DateField(blank=False, null=False)
      is_activate = models.BooleanField(default=True)
      create_at = models.DateTimeField(auto_now_add=True)

      objects = UserManager()

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['name', 'day_of_birth']


      def __str__(self):
           return self.name





