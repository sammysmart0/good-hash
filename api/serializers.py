from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=True)

  class Meta:
      model = CustomUser
      fields = (
        'id',
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'phone_number',
        'email',
        'matric_number',
        'department',
        'password',
        'username',
      )
      extra_kwargs = {
        'password': {'write_only': True},
      }


      # def create(self, validated_data):
      #   # Since no required fields from your model, i will just use the email, first_name, last_name and password to create
      #   # for now. I am assuming you're pass them too
      #   email = validated_data.pop('email')
      #   first_name = validated_data.pop('first_name')
      #   last_name = validated_data.pop('last_name')
      #   password = validated_data.pop('password')

      #   new_user = CustomUser(
      #       email=email,
      #       first_name=first_name,
      #       last_name=last_name
      #   )
      #   new_user.is_active = True
      #   new_user.set_password(password)
      #   new_user.save()

      #   return new_user