from django.contrib import admin
from . models import Category, Customer, Product, Order, Profile           # _2, _24

from django.contrib.auth.models import User                                 # _24

# Register your models here.



# _2

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

admin.site.register(Profile)                    # _24



# Mix profile info and user info                  # _24
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model                               # _24
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Unregister the old way                          # _24
admin.site.unregister(User)

# Re-Register the new way                          # _24
admin.site.register(User, UserAdmin)