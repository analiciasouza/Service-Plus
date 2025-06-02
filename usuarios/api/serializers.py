from django.contrib.auth import get_user_model
from rest_framework import serializers
from usuarios.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = User
          fields = [ 'id', 'name' , 'email' , 'password' ,'day_of_birth' , 'is_activate' , 'type_user' ,  
                    'create_at', 'is_staff' , 'is_superuser'] 

          extra_kwargs = {
               'password' : {'write_only' : True}
          }  
          def create(self, validated_data):
               return User.objects.create_user(**validated_data)
          
          def update(self, instance, validated_data):
               updated = super().update(instance, validated_data)

               if 'password' in validated_data:
                   updated.set_password(validated_data['password'])
                   updated.save()

               return updated 
                