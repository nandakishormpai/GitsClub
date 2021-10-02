from django.contrib import admin
from .models import User, Member

# Register your models here.
myModels = [User, Member]
admin.site.register(myModels)
