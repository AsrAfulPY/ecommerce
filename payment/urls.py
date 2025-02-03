from django.urls import path, include
from . import views

# _29
urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),          # _29
    # path('payment_failed', views.payment_failed, name='payment_failed'),
    path('checkout', views.checkout, name='checkout'),                          # _32
    path('billing_info', views.billing_info, name="billing_info"),                # _34
    path('process_order', views.process_order, name="process_order"),            # _35
    path('shipped_dash', views.shipped_dash, name="shipped_dash"),             # _39
    path('not_shipped_dash', views.not_shipped_dash, name="not_shipped_dash"),   # _39
    path('orders/<int:pk>', views.orders, name='orders'),                        # _40
    # path('paypal', include("paypal.standard.ipn.urls")),

]
