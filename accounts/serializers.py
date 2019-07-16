from rest_framework import serializers
from .models import Buyer, Seller, User


class UserSellerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    email = serializers.EmailField(allow_blank=False)
    last_name = serializers.CharField()
    cellphone = serializers.CharField()
    address = serializers.CharField()
    town = serializers.CharField()
    post_code = serializers.CharField()
    country = serializers.CharField()
    username = serializers.CharField(source='user.username')

    # photo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url='photos/%Y/%m/%d')
    # is_mvp = serializers.BooleanField(default=False)
    # join_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", input_formats=None, default_timezone=None)

    class Meta:
        model = Seller
        fields = ('email', 'first_name', 'last_name', 'cellphone', 'address', 'town', 'post_code', 'country', 'username')
        read_only_fields = ('username',)
class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # username = serializers.CharField()
    # first_name = serializers.CharField()
    # email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    # last_name = serializers.CharField()
    # cellphone = serializers.CharField()
    # address = serializers.CharField()
    # town = serializers.CharField()
    # post_code = serializers.CharField()
    # country = serializers.CharField()
    # photo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url='photos/%Y/%m/%d')
    # is_mvp = serializers.BooleanField(default=False)
    # join_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", input_formats=None, default_timezone=None)
    password = serializers.CharField(write_only=True)
    seller = UserSellerSerializer(required=False)
    class Meta:
        model = User
        fields = ('username', 'password', 'seller')


    def create(self, validated_data):
        profile_data = validated_data.pop('seller')
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_seller = True
        user.save()
        Seller.objects.update_or_create(user=user,**profile_data)
        return user