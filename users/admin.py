from django.contrib import admin

from .models import Profile, Review, CustomUser

admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(CustomUser)
