from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
      def create_user(self, name, email, day_of_birth, cpf=None, numero= None, type_user=None,password=None):
          if not email:
               raise ValueError("Precisa ter um email")
          
          email = self.normalize_email(email)
          user = self.model(
               name=name,
               email = email,
               day_of_birth = day_of_birth,
               type_user = type_user
          )

          user.set_password(password)
          user.save(using=self._db)

          return user
     
      def create_superuser(self, name, email, password=None, type_user=None ,**extras):
          email = self.normalize_email(email)
          extras.setdefault('is_staff', True)
          extras.setdefault('is_superuser', True)

          day_of_birth = extras.pop('day_of_birth', '2002-08-11')
          tipo_usuario = extras.pop('tipo_usuario', 'admin')

          user = User.objects.create_user(
               name=name,
               email = email,
               password = password,
               day_of_birth=day_of_birth,
               type_user = type_user,
          )

          user.is_superuser = True
          user.is_staff = True
          user.save(using=self._db)

          return user



class User(AbstractBaseUser, PermissionsMixin):
     USER_TYPE_CHOICES = {
         'cliente' : 'Cliente',
         'profissional' : 'Profissional',
         'admin' : 'Administrador'
     }

     name = models.CharField(max_length=255, blank=False, null=False)
     email = models.EmailField(unique=True,blank=False, null=False)
     day_of_birth = models.DateField(blank=False, null=False)
     type_user = models.CharField(choices=USER_TYPE_CHOICES, blank=False, null=False)

     is_activate = models.BooleanField(default=True)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at=models.DateTimeField(auto_now=True)
     is_staff = models.BooleanField(default=False)
     is_superuser = models.BooleanField(default=False)

     objects = UserManager()

     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['name', 'type_user']


     def has_perm(self, perm, obj=None):
        return self.is_superuser  

     def has_module_perms(self, app_label):
        return self.is_superuser 


     def __str__(self):
          return self.name
      

class PerfilClientes(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='perfil_cientes')
     cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
     numero = models.CharField(max_length=15,blank=False, null=False)
     image = models.ImageField(upload_to='usuarios/', null=True, blank=True)

     def __str__(self):
          return self.name
      

class PerfilProfissionais(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='perfil_profissional')
     cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
     numero = models.CharField(max_length=15,blank=False, null=False)
     image = models.ImageField(upload_to='usuarios/', null=True, blank=True)
     area_de_servico = models.CharField(max_length=255, blank=False, null=False)
     tipos_de_serviso = models.TextField()
     image = models.ImageField(upload_to='usuariosProfissionais/', null=True, blank=True)


     def __str__(self):
        return f"{self.name} - {self.area_de_servico}"

      
      
      
    
      





