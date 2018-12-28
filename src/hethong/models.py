from django.db import models

# Create your models here.

# Tao bang user 
class user(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 255)
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 255, null = True, blank = True)
	email = models.EmailField(null = True, blank = True)
	mobile = models.CharField(max_length = 12, null = True, blank = True)
	code = models.CharField(max_length = 255)
	image = models.ImageField(null = True, blank = True)
	status = models.PositiveSmallIntegerField()
	account_type = models.CharField(max_length = 45)
	dele = models.PositiveSmallIntegerField()

# Tao bang product
class product(models.Model):
 	code = models.CharField(max_length = 255)
 	name = models.CharField(max_length = 255)
 	price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
 	description = models.CharField(max_length = 500, null = True, blank = True)
 	image = models.CharField(max_length = 500, null = True, blank = True)
 	dele = models.PositiveSmallIntegerField()
 	product_category_id = models.PositiveIntegerField(null = True, blank = True)

# Tao bang product_category
class product_category(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 500, null = True, blank = True)
	dele = models.PositiveIntegerField()

# Tao bang container_product_detail
class container_product_detail(models.Model):
	product_id= models.PositiveIntegerField()
	container_id = models.PositiveIntegerField()
	provider_id = models.PositiveIntegerField()
	amount = models.PositiveIntegerField()
	manufacturing_date = models.DateField(null = True, blank = True)
	expiry_date = models.DateField(null = True, blank = True)

# Tao bang provider_product
class provider_product(models.Model):
	user_id = models.PositiveIntegerField()
	product_id = models.PositiveIntegerField()
	dele = models.PositiveSmallIntegerField()

# Tao bang container
class container(models.Model):
	code = models.CharField(max_length = 255, null = True, blank = True)
	name = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	mobile = models.CharField(max_length = 12, null = True, blank = True)
	dele = models.PositiveSmallIntegerField()

# Tao bang container_product_log
class container_product_log(models.Model):
	container_from = models.PositiveIntegerField()
	container_to = models.PositiveIntegerField()
	product_id = models.PositiveIntegerField()
	amount = models.PositiveIntegerField()
	manufacturing_date = models.DateField(null = True, blank = True)
	expiry_date = models.DateField(null = True, blank = True)

# Tao bang order
class order(models.Model):
	code = models.CharField(max_length = 255)
	user_id = models.PositiveIntegerField()
	price_total = models.PositiveIntegerField(null = True, blank = True)
	order_date = models.DateField(auto_now_add = True)
	export_date = models.DateField(null = True, blank = True)
	status = models.CharField(max_length = 45)

# Tao bang order_detail
class order_detail(models.Model):
	order_id = models.PositiveIntegerField()
	product_id = models.PositiveIntegerField()
	amount = models.PositiveIntegerField()
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	manufacturing_date = models.DateField(null = True, blank = True)
	expiry_date = models.DateField(null = True, blank = True)

# Tao lop tinh trangkhohang nham truyen du lieu vao trang tinh_trang_kho_hang.html
class tinhtrangkhohang():
	def __init__(self, id, code, name, amount, manufacturing_date, expiry_date, container_from, container_to):
		self.id = id
		self.code = code
		self.name = name
		self.amount = amount
		self.manufacturing_date = manufacturing_date
		self.expiry_date = expiry_date
		self.container_from = container_from
		self.container_to = container_to

class makho():
	def __init__(self, id):
		self.id = id
		
# Tao lop tinh trangkhohang nham truyen du lieu vao trang lich_su_kho_hang.html
class chuyenkho():
	def __init__(self, id, name, amount, manufacturing_date, expiry_date, container_from_name, container_to_name):
		self.id = id
		self.name = name
		self.amount = amount
		self.manufacturing_date = manufacturing_date
		self.expiry_date = expiry_date
		self.container_from_name= container_from_name
		self.container_to_name = list(container_to_name)