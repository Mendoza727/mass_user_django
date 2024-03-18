from django.shortcuts import render
from django.http import JsonResponse
from faker import Faker
from .models import User

def create_fake_users(request, num_users):
    fake = Faker()
    created_users = []
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            created_users.append({
                'username': username,
                'email': email
            })
    return JsonResponse({'created_users': created_users})
