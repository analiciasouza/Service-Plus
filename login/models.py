from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
      def create_user(self, name, email, day_of_birth, password=None):
          if not email:
               raise ValueError("Precisa ter um email")
          
          email = self.normalize_email(email)
          user = self.model(
               name=name,
               email = email,
               day_of_birth = day_of_birth,
          )

          user.set_password(password)
          user.save()

          return user
     
      def create_superuser(self, name, email, day_of_birth, password=None):
          email = self.normalize_email(email)
          user = User.objects.create_user(
               name=name,
               email = email,
               day_of_birth = day_of_birth,
               password = password
          )


          user.is_superuser = True
          user.is_staff = True
          user.save()

          return user



class User(AbstractBaseUser):
      name = models.CharField(max_length=255, blank=False, null=False)
      email = models.EmailField(unique=True,blank=False, null=False)
      day_of_birth = models.DateField(blank=False, null=False)
      is_activate = models.BooleanField(default=True)
      create_at = models.DateTimeField(auto_now_add=True)
      is_staff = models.BooleanField(default=False)
      is_superuser = models.BooleanField(default=False)

      objects = UserManager()

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['name', 'day_of_birth']


      def has_perm(self, perm, obj=None):
        return self.is_superuser  

      def has_module_perms(self, app_label):
        return self.is_superuser 


      def __str__(self):
           return self.name





