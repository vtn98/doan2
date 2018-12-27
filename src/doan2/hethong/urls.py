from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('nhaphanphoi/', views.nha_phan_phoi, name = 'nhaphanphoi'),

	path('', views.header, name = 'header'),

	path('themncc/', views.them_ncc, name = 'them_ncc'),

	path('danhsachncc/', views.danh_sach_ncc, name = 'danh_sach_ncc'),

	path('taomoihanghoa/', views.tao_moi_hang_hoa, name = 'tao_moi_hang_hoa'),

	path('danhsachhanghoa/', views.danh_sach_hang_hoa, name = 'danh_sach_hang_hoa'),

	path('capnhat/(?P<mahanghoa>regex)', views.cap_nhat_thong_tin_hang_hoa, name = 'cap_nhat_thong_tin_hang_hoa'),

	path('danhsachnhomhanghoa/', views.danh_sach_nhom_hang_hoa, name = 'danh_sach_nhom_hang_hoa'),

	path('danhsachnhomhanghoa/capnhat/(?P<loaihanghoa>regex)', views.cap_nhat_loai_hang_hoa, name = 'cap_nhat_loai_hang_hoa'),

	path('taomoikhohang/', views.tao_moi_kho_hang, name = 'tao_moi_kho_hang'),

	path('danhsachkhohang/', views.danh_sach_kho_hang, name = 'danh_sach_kho_hang'),

	path('chitietkhohang/(?P<idkhohang>regex)', views.chi_tiet_kho_hang, name = 'chi_tiet_kho_hang'),

	path('chitietkhohang/(?P<idkhohang>regex)/thongtincoban', views.thong_tin_co_ban, name = 'thong_tin_co_ban'),

	path('chitietkhohang/(?P<idkhohang>regex)/lichsukhohang', views.lich_su_kho_hang, name = 'lich_su_kho_hang'),

	path('chitietkhohang/(?P<idkhohang>regex)/tinhtrangkhohang', views.tinh_trang_kho_hang, name = 'tinh_trang_kho_hang'),

	path('chitietkhohang/(?P<idkhohang>regex)/tinhtrangkhohang/(?P<mahanghoa>regex)', views.chuyen_kho, name = 'chuyen_kho'),

	path('chitietkhohang/(?P<idkhohang>regex)/thongkekhohang', views.thong_ke_kho_hang, name = 'thong_ke_kho_hang'),
]
