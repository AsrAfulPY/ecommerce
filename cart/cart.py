from store.models import Product, Profile           # _15, _27


# _12
class Cart():
	def __init__(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}


		# Make sure cart is available on all pages of site
		self.cart = cart



# _28

	def db_add(self, product, quantity):
		product_id = str(product)
		product_qty = str(quantity)
		# Logic
		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


# _13

	def add(self, product, quantity):                      # _ ,_16=
	# def add(self, product):
		product_id = str(product.id)
		product_qty = str(quantity)                             # _16
		# Logic
		if product_id in self.cart:
			pass
		else:
			# self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)                             # _16

		self.session.modified = True


		# _27
		# Deal with logged in user                                        # _27
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))

	def cart_total(self):                                       # _19
		# Get product IDS
		product_ids = self.cart.keys()
		# lookup those keys in our products database model
		products = Product.objects.filter(id__in=product_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for product in products:
				if product.id == key:
					if product.is_sale:
						total = total + (product.sale_price * value)
					else:
						total = total + (product.price * value)



		return total


     #     # _14

	def __len__(self):
		return len(self.cart)


	# _15
	def get_prods(self):
		# Get ids from cart
		product_ids = self.cart.keys()
		# Use ids to lookup products in database model
		products = Product.objects.filter(id__in=product_ids)

		# Return those looked up products
		return products

	def get_quants(self):                    # _16
		quantities = self.cart
		return quantities

	def update(self, product, quantity):          # _16
		product_id = str(product)
		product_qty = int(quantity)
		

		# {'4':3, '2':5}



		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[product_id] = product_qty

		self.session.modified = True
	

		# thing = self.cart                                      # -_28
		# return thing                                         # -_28


		# _28
		# Deal with logged in user                                        # _28
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


		thing = self.cart
		return thing





	def delete(self, product):
		product_id = str(product)
		# Delete from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True


		# _28
		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))



