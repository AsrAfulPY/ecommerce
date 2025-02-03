from django.shortcuts import render, get_object_or_404          # _,  _13
from .cart import Cart                                        # _13     # from .cart    = cart.py থেকে import করা হয়ে
from store.models import Product                              # _13
from django.http import JsonResponse                            # _13
from django.contrib import messages                            # _14

def cart_summary(request):
	# Get the cart
	cart = Cart(request)                      # _15
	cart_products = cart.get_prods             # _15   # cart.py থেকে get_prods ফাংশন আনা হায়চে 
	quantities = cart.get_quants               # _16
	totals = cart.cart_total()                      # _19
	return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})   # _13, _15, _19
	# return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})


# _13

def cart_add(request):                             # _13     # এই ফানশন গেছে প্রোডাক্ট এইচটিএমএল
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))              # _13
		product_qty = int(request.POST.get('product_qty'))            # _16

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)                            # _16
		# cart.add(product=product)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})          # _14
		response = JsonResponse({'qty': cart_quantity})                      # _14
		messages.success(request, ("Product Added  To Cart..."))
		return response

def cart_delete(request):                  # _18
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		# return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response


# _17

def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		# messages.success(request, ("Your Cart Has Been Updated..."))
		return response
