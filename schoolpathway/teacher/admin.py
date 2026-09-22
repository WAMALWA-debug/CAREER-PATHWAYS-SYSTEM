from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

Group.objects.get_or_create(name='Teacher')