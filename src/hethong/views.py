from django.shortcuts import render, redirect
from .models import  user, product, container, product_category, tinhtrangkhohang, makho, chuyenkho
from django.http import HttpResponse
from django.contrib import messages
import pymysql, secrets, string

# command ma nguon, tài liệu mã nguồn giống javadoc
# Create your views here.
def connectMySQL():
	"""Kết nối MySQL.

	Sử dụng thư viện pymysql kết nối với MySQL để thao tác dữ liệu.
 
	"""
	connection = pymysql.connect('localhost', 'root', '123456', 'doan2', autocommit = True)
	return connection

def nha_phan_phoi(request):
	"""Hiển thị giao diện chính của nhà phân phối khi nhận được yêu cầu từ trình duyệt.

	Args:
		request : Yêu cầu từ trình duyệt.
	Returns:
		Giao diện chính của nhà phân phối.

	"""
	return render(request, 'hethong/nha_phan_phoi.html')
 
def tao_moi_hang_hoa(request):
	"""Hiển thị giao diện tạo mới sản phẩm khi nhận được yêu cầu từ trình duyệt.
	
	Args:
		request : Yêu cầu từ trình duyệt.

	Returns:
		Giao diện tạo mới sản phẩm.
		Kết quả tạo mới sản phẩm.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if (request.method == 'POST'):
		try:
			giaban = float(request.POST['price'])
			if giaban < 0:
				CRITICAL = 50
				messages.add_message(request, CRITICAL, 'Giá sản phẩm không phù hợp')
			else:
				stringSource  = string.ascii_letters + string.digits
				code = secrets.choice(string.ascii_lowercase)
				code = secrets.choice(string.ascii_uppercase)
				code += secrets.choice(string.digits)
				for i in range(6):
					code += secrets.choice(stringSource)
				sql = "select id from hethong_product_category where name = %s"
				cursor.execute(sql, request.POST['product_type'])
				row = cursor.fetchone()
				id = row[0]
				sql = "insert into hethong_product(code, name, price, product_category_id, image, description, dele) values(%s, %s, %s, %s, %s, %s, %s)"
				cursor.execute(sql, ("PRODUCT_" + code, request.POST['name'], request.POST['price'], id, request.POST['image'], request.POST['description'], '0'))
				CRITICAL = 50
				messages.add_message(request, CRITICAL, 'Tạo mới thành công')
		except:
			CRITICAL = 50
			messages.add_message(request, CRITICAL, 'Giá sản phẩm phải là số nguyên dương')
	sql = "select name from hethong_product_category"
	cursor.execute(sql)
	product_type = []
	for row in cursor:
		product_type.append(row[0])
	return render(request, 'hethong/tao_hang_hoa.html', {'form': product_type})
 
def danh_sach_hang_hoa(request):
	"""Hiển thị danh sách sản phẩm của nhà phân phối.

	Hiển thị danh sách sản phẩm khi thao tác tìm kiếm sản phẩm.

	Args:
		request: Yêu cầu từ trình duyệt.

	Returns:
		Danh sách sản phẩm.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		if not request.POST['name'] and request.POST['code']:
			sql = "select code, name, price, description, image, product_category_id from hethong_product where code like %s and product_category_id = %s"
			cursor.execute(sql, ("%" + request.POST['code'] + "%", request.POST['product_type']))
		elif not request.POST['code'] and request.POST['name']:
			sql = "select code, name, price, description, image, product_category_id from hethong_product where name like %s and product_category_id = %s"
			cursor.execute(sql, ("%" + request.POST['name'] + "%", request.POST['product_type']))
		else:
			sql = "select code, name, price, description, image, product_category_id from hethong_product where (name like %s or code like %s) and product_category_id = %s"
			cursor.execute(sql, ("%" + request.POST['name'] + "%", "%" + request.POST['code'] + "%", request.POST['product_type']))
	else:
		sql = "select code, name, price, description, image, product_category_id from hethong_product"
		cursor.execute(sql)
	listproduct = []
	for row in cursor:
		hh = product()
		hh.code = row[0]
		hh.name = row[1]
		hh.product_category_id = row[5]
		hh.description = row[3]
		hh.image = row[4]
		hh.price = row[2]
		listproduct.append(hh)	
	sql = "select id from hethong_product_category"
	cursor.execute(sql)
	idnhomhanghoa = []
	for row in cursor:
		idnhomhanghoa.append(row[0])
	listproduct.append(idnhomhanghoa)
	return render(request, 'hethong/danh_sach_hang_hoa.html', {'form': listproduct})

def cap_nhat_thong_tin_hang_hoa(request, mahanghoa):
	"""Hiển thị giao diện cập nhật thông tin sản phẩm.
	
	Cập nhật thông tin sản phẩm vào cơ sở dữ liệu.
	
	Args:
		request: Yêu cầu từ trình duyệt
		mahanghoa: Mã sản phẩm của sản phẩm cần cập nhật.

	Returns:
		Giao diện cập nhật thông tin sản phẩm.
		Kết quả cập nhật.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if (request.method == 'POST'):
		if request.POST.get('luu'):
			sql = "update hethong_product set name = %s, price = %s, description = %s, image = %s where code = %s"
			cursor.execute(sql, (request.POST['name'], request.POST['price'], request.POST['description'], request.POST['image'], mahanghoa))
			CRITICAL = 50
			messages.add_message(request, CRITICAL, 'Cập nhật thành công')
	sql = "select code, name, price, description, image, product_category_id from hethong_product where code = %s"
	cursor.execute(sql, mahanghoa)
	sanpham = []
	for row in cursor:
		hh = product()
		hh.code = row[0]
		hh.name = row[1]
		hh.product_type = row[5]
		hh.description = row[3]
		hh.image = 'images/' + row[4]
		hh.price = row[2]
		sanpham.append(hh)	
	return render(request, 'hethong/cap_nhat_thong_tin_hang_hoa.html', {'form': sanpham})
 
def danh_sach_nhom_hang_hoa(request):
	"""Hiển thị danh sách nhóm sản phẩm của nhà phân phối.
	 
	Xử lý việc tạo thêm nhóm sản phẩm mới.

	Args:
		request: Yêu cầu từ trình duyệt.

	Returns:
		Danh sách nhóm sản phẩm.
		Kết quả tạo nhóm sản phẩm mới.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		# Kiem tra da ton tai loai hang hoa trong kho chua
		sql = "select name from hethong_product_category where name = %s"
		cursor.execute(sql, request.POST['product_type'])
		row = cursor.fetchone()
		if row:
			CRITICAL = 50
			messages.add_message(request, CRITICAL, 'Nhóm hàng hóa đã tồn tại')
		else:
			sql = "insert into hethong_product_category(name, description, dele) values(%s, %s, %s)"
			cursor.execute(sql, (request.POST['product_type'], request.POST['description'], '0'))
			CRITICAL = 50
			messages.add_message(request, CRITICAL, 'Tạo mới thành công')
	sql = "select name, description from hethong_product_category"
	cursor.execute(sql)
	pro = []
	for row in cursor:
		hh = product_category()
		hh.name = row[0]
		hh.description = row[1]
		pro.append(hh)	
	return render(request, 'hethong/danh_sach_nhom_hang_hoa.html', {'form': pro})

def cap_nhat_loai_hang_hoa(request, loaihanghoa):
	"""Hiển thị giao diện cập nhật thông tin nhóm sản phẩm.
	
	Cập nhật thông tin nhóm sản phẩm vào cơ sở dữ liệu.
	
	Args:
		request: Yêu cầu từ trình duyệt
		loaihanghoa: Mã nhóm sản phẩm cần cập nhật.

	Returns:
		Giao diện cập nhật thông tin nhóm sản phẩm.
		Kết quả cập nhật.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if (request.method == 'POST'):
		if request.POST.get('luu'):
			sql = "update hethong_product_category set description = %s where name = %s"
			cursor.execute(sql, (request.POST['des'], loaihanghoa))
			CRITICAL = 50
			messages.add_message(request, CRITICAL, 'Cập nhật thành công')
	sql = "select  name, description from hethong_product_category where name = %s"
	cursor.execute(sql, loaihanghoa)
	row = cursor.fetchone()
	pro = []
	hh = product_category()
	hh.name = row[0]
	hh.description = row[1]
	pro.append(hh)
	return render(request, 'hethong/cap_nhat_loai_hang_hoa.html', {'form': pro})

def tao_moi_kho_hang(request):
	"""Hiển thị giao diện tạo mới kho hàng.

	Args:
		request : Yêu cầu từ trình duyệt.

	Returns:
		Giao diện tạo mới sản phẩm.
		Kết quả tạo mới sản phẩm.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if (request.method == 'POST'):
		# Sinh ra ma code cua kho hang
		stringSource  = string.ascii_letters + string.digits
		code = secrets.choice(string.ascii_lowercase)
		code = secrets.choice(string.ascii_uppercase)
		code += secrets.choice(string.digits)
		for i in range(6):
			code += secrets.choice(stringSource)
		# Them vao co so du lieu
		sql = "insert into hethong_container(code, name, address, mobile, dele) values(%s, %s, %s, %s, %s)"
		cursor.execute(sql, ("CONTAINER_" + code, request.POST['name'], request.POST['address'], request.POST['mobile'], '0'))
		CRITICAL = 50
		messages.add_message(request, CRITICAL, 'Tạo mới thành công')
	return render(request, 'hethong/tao_kho_hang.html')

def danh_sach_kho_hang(request):
	"""Hiển thị danh sách kho hàng của nhà phân phối.

	Hiển thị danh sách kho hàng khi thao tác tìm kiếm kho hàng.

	Args:
		request: Yêu cầu từ trình duyệt.

	Returns:
		Danh sách kho hàngs.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		# Chi nhap ma san pham
		if not request.POST['name'] and request.POST['code']:
			sql = "select id, code, name, address, mobile from hethong_container where code like %s"
			cursor.execute(sql, ("%" + request.POST['code'] + "%"))
		elif not request.POST['code'] and request.POST['name']:
			sql = "select id, code, name, address, mobile from hethong_container where name like %s"
			cursor.execute(sql, ("%" + request.POST['name'] + "%"))
		else:
			sql = "select id, code, name, address, mobile from hethong_container where (code like %s or name like %s)"
			cursor.execute(sql, ("%" + request.POST['code'] + "%", "%" + request.POST['name'] + "%"))
	else:
		sql = "select id, code, name, address, mobile from hethong_container"
		cursor.execute(sql);
	khohang = []
	for row in cursor:
		kho = container()
		kho.id = row[0]
		kho.code = row[1]
		kho.name = row[2]
		kho.address  = row[3]
		kho.mobile = row[4]
		khohang.append(kho)	
	return render(request, 'hethong/danh_sach_kho_hang.html', {'form': khohang})

def chi_tiet_kho_hang(request, idkhohang):
	"""Hiển thị giao diện chi tiết kho hàng.
	
	Hiển thị menu thông tin cơ bản, tình trạng kho hàng, lịch sử kho hàng, chuyển kho của kho hàng.
	 
	Args:
		request: Yêu cầu từ trình duyệt.
		idkhoang: Mã kho hàng cần xem chi tiết.

	Returns:
		Giao diện chi tiết kho hàng của kho hàng có mã idkhohang.

	"""
	ma = []
	ma1 = makho(idkhohang)
	ma.append(ma1)
	return render(request, 'hethong/chi_tiet_kho_hang.html', {'form': ma})

def thong_tin_co_ban(request, idkhohang):
	"""Hiển thị giao diện thông tin cơ bản của kho hàng.
	 
	Args:
		request: Yêu cầu từ trình duyệt.
		idkhohang: Mã kho hàng, được dùng để truy xuất vào cơ sở dữ liệu lấy thông tin cơ bản của kho hàng.

	Returns:
		Thông tin cơ bản của kho hàng có mã kho hàng là idkhohang.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		sql = "update hethong_container set address = %s, mobile = %s where id = %s"
		cursor.execute(sql, (request.POST['address'], request.POST['mobile'], idkhohang))
		CRITICAL = 50
		messages.add_message(request, CRITICAL, 'Cập nhật thành công')
	sql = "select code, name, address, mobile from hethong_container where id = %s"
	cursor.execute(sql, idkhohang);
	khohang = []
	for row in cursor:
		kho = container()
		kho.id = idkhohang
		kho.code = row[0]
		kho.name = row[1]
		kho.address  = row[2]
		kho.mobile = row[3]
		khohang.append(kho)	
	kho = container()
	kho.id = idkhohang
	khohang.append(kho)
	return render(request, 'hethong/thong_tin_co_ban.html', {'form': khohang})

def tinh_trang_kho_hang(request, idkhohang):
	"""Hiển thị giao diện tình trạng của kho hàng.
	 
	Args:
		request: Yêu cầu từ trình duyệt.
		idkhohang: Mã kho hàng, được dùng để truy xuất vào cơ sở dữ liệu lấy thông tin tình trạng của kho hàng.

	Returns:
		Tình trạng của kho hàng có mã kho hàng là idkhohang.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		# Chi nhap ma san pham
		if not request.POST['name'] and request.POST['code']:
			sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date from hethong_product, hethong_container_product_detail, hethong_container where hethong_product.id = hethong_container_product_detail.product_id and hethong_container_product_detail.container_id = %s and hethong_product.code like %s"
			cursor.execute(sql, (idkhohang, "%" + request.POST['code'] + "%"))
		elif not request.POST['code'] and request.POST['name']:
			sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date from hethong_product, hethong_container_product_detail, hethong_container where hethong_product.id = hethong_container_product_detail.product_id and hethong_container_product_detail.container_id = %s and hethong_product.name like %s"
			cursor.execute(sql, (idkhohang, "%" + request.POST['name'] + "%"))
		else:
			sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date from hethong_product, hethong_container_product_detail, hethong_container where hethong_product.id = hethong_container_product_detail.product_id and hethong_container_product_detail.container_id = %s and (hethong_product.code like %s or hethong_product.name like %s)"
			cursor.execute(sql, (idkhohang, "%" + request.POST['code'] + "%", "%" + request.POST['name'] + "%"))
	else:
		sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date from hethong_product, hethong_container_product_detail, hethong_container where hethong_product.id = hethong_container_product_detail.product_id and hethong_container_product_detail.container_id = %s"
		cursor.execute(sql, idkhohang);
	khohang = []
	for row in cursor:
		kho = tinhtrangkhohang(id = idkhohang, code = row[0], name = row[1],  amount = row[2], manufacturing_date = row[3], expiry_date = row[4], container_from = '0', container_to = '0')
		khohang.append(kho)
		
	kho = tinhtrangkhohang(id = idkhohang, code = 0, name = 0,  amount = 0, manufacturing_date = 0, expiry_date = 0, container_from = 0, container_to = 0)
	khohang.append(kho)
	return render(request, 'hethong/tinh_trang_kho_hang.html', {'form': khohang})

def chuyen_kho(request, idkhohang, mahanghoa):
	"""Hiển thị giao diện lưu chuyển sản phẩm.
	 
	Xử lý thông tin lưu chuyển sản phẩm giữa các kho.
	 
	Args:
		request: Yêu cầu từ trình duyệt.
		idkhohang: Mã kho hàng đích.
		mahanghoa: Mã hàng hóa cần lưu chuyển.

	Returns:
		Giao diện lưu chuyển sản phẩm.
		Kết quả lưu chuyển sản phẩm.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		if request.POST.get('capnhat'):
			sql = "select hethong_product.id, amount, provider_id from hethong_product, hethong_container_product_detail where hethong_product.id = hethong_container_product_detail.product_id and hethong_product.code = %s and hethong_container_product_detail.container_id = %s"
			cursor.execute(sql, (mahanghoa, idkhohang))
			row = cursor.fetchone()
			amount = int(row[1])
			try:
				soluong = int(request.POST['amount'])
				if soluong < 0 or soluong > amount:
					CRITICAL = 50
					messages.add_message(request, CRITICAL, 'Số lượng chuyển không phù hợp')
				else:
					sql = "select id from hethong_container where name = %s"
					cursor.execute(sql, request.POST['container_to'])
					id_to = cursor.fetchone()
					sql = "select amount from hethong_container, hethong_product, hethong_container_product_detail where hethong_product.id = hethong_container_product_detail.product_id and hethong_container_product_detail.container_id = hethong_container.id and hethong_product.id = %s and hethong_container_product_detail.container_id = %s"
					cursor.execute(sql, (row[0], id_to[0]))
					row_to = cursor.fetchone()
					
					#  Neu hang hoa can chuyen chua co trong kho dich
					if not row_to:
						sql = "insert into hethong_container_product_detail(product_id, container_id, provider_id, amount) values(%s, %s, %s, %s)"
						cursor.execute(sql, (row[0], id_to[0], row[2], request.POST['amount']))
						sql = "update hethong_container_product_detail set amount = %s where product_id = %s and container_id = %s"
						cursor.execute(sql, (str(amount - soluong), row[0], idkhohang))
						sql = "insert hethong_container_product_log(container_from, container_to, product_id, amount) values(%s, %s, %s, %s)"
						cursor.execute(sql, (idkhohang, id_to[0], row[0], request.POST['amount']))
						CRITICAL = 50
						messages.add_message(request, CRITICAL, 'Cập nhật thành công')
					else:
						amount_to = int(row_to[0])
						sql = "update hethong_container_product_detail set amount = %s where container_id = %s and product_id = %s"
						cursor.execute(sql, (str(amount - soluong), idkhohang, row[0]))
						sql = "update hethong_container_product_detail set amount = %s where container_id = %s and product_id = %s"
						cursor.execute(sql, (str(amount_to + soluong), id_to[0], row[0]))
						sql = "insert hethong_container_product_log(container_from, container_to, product_id, amount) values(%s, %s, %s, %s)"
						cursor.execute(sql, (idkhohang, id_to[0], row[0], request.POST['amount']))
						CRITICAL = 50
						messages.add_message(request, CRITICAL, 'Cập nhật thành công')
			except:
				CRITICAL = 50
				messages.add_message(request, CRITICAL, 'Số lượng chuyển phải là số nguyên dương')
	sql = "select hethong_product.name, amount, manufacturing_date, expiry_date, hethong_container.name from hethong_product, hethong_container, hethong_container_product_detail where hethong_container_product_detail.product_id = hethong_product.id and hethong_container_product_detail.container_id = hethong_container.id and hethong_product.code = %s and hethong_container.id = %s"
	cursor.execute(sql, (mahanghoa, idkhohang))
	row = cursor.fetchone()
	sql1 = "select hethong_container.name from hethong_container where id <> %s"
	cursor.execute(sql1, idkhohang)
	move = []
	for i in cursor:
		move.append(i[0])
	ck = chuyenkho(id = idkhohang, name = row[0], amount = row[1], manufacturing_date = row[2], expiry_date = row[3], container_from_name = row[4], container_to_name = move)
	chuyen = []
	chuyen.append(ck)
	return render(request, 'hethong/chuyen_kho.html', {'form': chuyen})

def lich_su_kho_hang(request, idkhohang):
	"""Hiển thị giao diện lịch sử lưu chuyển sản phẩm của kho hàng.
	 
	Args:
		request: Yêu cầu từ trình duyệt.
		idkhohang: Mã kho hàng đích.

	Returns:
		Lịch sử lưu chuyển sản phẩm của kho hàng có mã kho hàng là idkhohang.

	"""
	connection = connectMySQL()
	cursor = connection.cursor()
	if request.method == 'POST':
		# Chi nhap ma san pham
		if not request.POST['name'] and request.POST['code']:
			sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date, container_from, container_to from hethong_product, hethong_container_product_log, hethong_container where hethong_product.id = hethong_container_product_log.product_id and hethong_container_product_log.container_from = %s and hethong_product.code like %s"
			cursor.execute(sql, (idkhohang, "%" + request.POST['code'] + "%"))
		elif not request.POST['code'] and request.POST['name']:
			sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date, container_from, container_to from hethong_product, hethong_container_product_log, hethong_container where hethong_product.id = hethong_container_product_log.product_id and hethong_container_product_log.container_from = %s and hethong_product.name like %s"
			cursor.execute(sql, (idkhohang, "%" + request.POST['name'] + "%"))
		else:
			sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date, container_from, container_to from hethong_product, hethong_container_product_log, hethong_container where hethong_product.id = hethong_container_product_log.product_id and hethong_container_product_log.container_from = %s and (hethong_product.code like %s or hethong_product.name like %s)"
			cursor.execute(sql, (idkhohang, "%" + request.POST['code'] + "%", "%" + request.POST['name'] + "%"))
	else:
		sql = "select distinct hethong_product.code, hethong_product.name, amount, manufacturing_date, expiry_date, container_from, container_to from hethong_product, hethong_container_product_log, hethong_container where hethong_product.id = hethong_container_product_log.product_id and hethong_container_product_log.container_from = %s"
		cursor.execute(sql, idkhohang)
	khohang = []
	for row in cursor:
		kho = tinhtrangkhohang(id = idkhohang, code = row[0], name = row[1],  amount = row[2], manufacturing_date = row[3], expiry_date = row[4], container_from = row[5], container_to = row[6])
		khohang.append(kho)	
	kho = tinhtrangkhohang(id = idkhohang, code = 0, name = 0,  amount = 0, manufacturing_date = 0, expiry_date = 0, container_from = 0, container_to = 0)
	khohang.append(kho)
	return render(request, 'hethong/lich_su_kho_hang.html', {'form': khohang})