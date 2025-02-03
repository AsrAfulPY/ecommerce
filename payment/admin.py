from django.contrib import admin                        # _29
from .models import ShippingAddress, Order, OrderItem        # _29  # _35      #, ,😇#&&#&#&#&#&#&&#&##&#&&#&#&##&#&#&#&&#&
from django.contrib.auth.models import User                         # _37




# Register the model on the admin section thing
admin.site.register(ShippingAddress)                            # _29
admin.site.register(Order)                                    # _35      #😇#&&#&#&#&#&#&&#&##&#&&#&#&##&#&#&#&&#&
admin.site.register(OrderItem)                                # _35      #😇#&&#&#&#&#&#&&#&##&#&&#&#&##&#&#&#&&#&

# Create an OrderItem Inline                                  #  # [ _37 ]..........
class OrderItemInline(admin.StackedInline):
	model = OrderItem
	extra = 0

# Extend our Order Model
class OrderAdmin(admin.ModelAdmin):
	model = Order
	readonly_fields = ["date_ordered"]
	fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]
	inlines = [OrderItemInline]

# Unregister Order Model
admin.site.unregister(Order)

# Re-Register our Order AND OrderAdmin
admin.site.register(Order, OrderAdmin)                      #  # [ _37 ]..........