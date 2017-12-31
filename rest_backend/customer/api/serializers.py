from rest_framework import serializers
from django.contrib.auth.models import User
from customer.models import Customer


class UserSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='customer.address')
    phone_number = serializers.CharField(source='customer.phone_number')
    age = serializers.CharField(source='customer.age')
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'address', 'phone_number', 'age')

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        customer_data = validated_data.pop('customer', {})
        address = customer_data.pop('address')
        phone_number = customer_data.pop('phone_number')
        age = customer_data.pop('age')
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        Customer.objects.create(user=user, address=address, phone_number=phone_number, age=age)
        return user

    def update(self, instance, validated_data):
        customer = instance.customer
        for attr, value in validated_data.items():
            if attr == 'customer':
                for attr1, value1 in value.items():
                    setattr(customer, attr1, value1)
            else:
                setattr(instance, attr, value)
        instance.save()
        customer.save()
        return instance
