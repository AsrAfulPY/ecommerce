from .cart import Cart           # _12

# Create context processor so our cart can work on all pages of the site
def cart(request):                 # _12
	# Return the default data from our Cart
	return {'cart': Cart(request)}