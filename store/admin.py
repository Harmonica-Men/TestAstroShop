from django.contrib import admin
from .models import Category, Product, Profile, Subscription, Supplier
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Subscription)
admin.site.register(Supplier)


# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]


# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)
