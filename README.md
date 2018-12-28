# HỆ THỐNG QUẢN LÝ CHUỖI CUNG ỨNG
## Phần I: Mục tiêu
- Mô tả quá trình nhà phân phối nhập hàng từ thương lái và vận chuyển hàng hóa đến các siêu thị.
- Lưu lại lịch sử lưu chuyển hàng hóa giữa các kho của nhà phân phối.

## Phần II: Công nghệ sử dụng
1. Cơ sở dữ liệu quan hệ MySQL
2. Framework Django

## Phần III: Hướng dẫn cài đặt
### **1. Cài đặt MySQL**

Để download MySQL Community, truy cập vào địa chỉ:
[http://dev.mysql.com/downloads/mysql]()
 
Mở **MySQL Workbench** và tạo 1 cơ sở dữ liệu với tên là doan2.

### **2. Cài đặt django**
Với windows, mở cửa sổ terminal trong windows và gõ:
> **pip install django**

Với linux và mac, mở cửa sổ terminal và gõ:
> **sudo apt-get install django**

Tạo django project có tên là doan2
> **django-admin startproject doan2**

Tiếp theo cd vào thư mục doan2 và tạo 1 app với tên là hethong
> **manage.py startapp hethong**

Trong app hethong tạo 2 folder static và templates.

### **3. Cài đặt pymysql**
Tương tự cài đặt django. Mở terminal:

Đối với windows, gõ:
> **pip install pymysql**  

Đối với linux và mac, gõ:
> **sudo apt-get install pymysql**

### **4. Kết nối django với MySQL**
- Vào file settings.py của project doan2 vừa tạo ở trên

    - Thay đổi các thông số trong DATABASE.
    <img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/48921805_1172268686261581_4248535946456203264_n.png?_nc_cat=103&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=401d7f203e051b14c134b3c455ae5b7b&amp;oe=5C8F4D9C" alt="" class="img" style="width: 436px; height: 197px;">

    Trong đó user và password là user và password lúc cài đặt MySQL.
    
    - Tìm và thay dòng **"BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))"** bằng 2 dòng sau:
    
        **PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))**
    
       **PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)**
    - Tìm và thay dòng **"STATIC_URL = '/static/'"** bằng 5 dòng sau:
    
        **STATIC_URL = '/skin/'** 
        
        **STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)** 
        
        **STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))** 
        
        **MEDIA_URL = "/media/"** 
        
        **MEDIA_ROOT = os.path.join(BASE_DIR, "static",\*MEDIA_URL.strip("/").split("/"))** 
- Vào file __init__.py của project và gõ:

---
    import pymysql
    pymysql.install_as_MySQLdb()
---

- Mở terminal và chuyển đến thư mục project doan2 vừa tạo ở trên và gõ:

> **manage.py runserver**

## Phần IV: Hướng dẫn sử dụng
- Mở trình duyệt và gõ địa chỉ: [localhost:8000/nhaphanphoi]()

Giao diện của hệ thống hiện ra (đây là giao diện của nhà phân phối).

![](media/giaodienchung.PNG)

**1. Hệ thống sản phẩm**

![](media/hethongsanpham.PNG)
Ở đây thực hiện các chức năng: Tạo mới sản phẩm cho nhà phân phối, hiển thị danh sách các sản phẩm, nhóm sản phẩm, tạo mới nhóm sản phẩm, cập nhật thông tin của sản phẩm và nhóm sản phẩm, tìm kiếm thông tin sản phẩm.

**1.1. Tạo mới sản phẩm**


![](media/taomoisanpham.PNG)

Ở đây chúng ta điền đầy đủ thông tin của form **Tạo mới sản phẩm** và click **"Tạo mới"**.

**1.2. Danh sách sản phẩm**

![](media/danhsachsanpham.PNG)

- Cập nhật thông tin sản phẩm
 
![](media/capnhatthongtinsanpham.PNG)

Ở đây chúng ta có thể thay đổi 1 số thông tin của sản phẩm và click **"Cập nhật"** để cập nhật lại thông tin của sản phẩm.
- Tìm kiếm sản phẩm theo tên và nhóm hàng hóa bằng cách nhập tên hàng hóa và nhóm sản phẩm, sau đó click **"Tìm kiếm"**.

![](media/timkiemtheoten.PNG)

- Tìm kiếm sản phẩm theo mã bằng cách nhập mã sản phẩm sau đó click **"Tìm kiếm"**.

![](media/timkiemtheoma.PNG)
    
**1.3. Hệ thống nhóm sản phẩm**

![](media/hethongnhomsanpham.PNG)
Ở đây chúng ta có thể thực hiện chức năng tạo mới nhóm sản phẩm và cập nhật thông tin của nhóm sản phẩm.

- Tạo mới nhóm sản phẩm

![](media/taomoinhomhanghoa.PNG)

Điền đầy đủ thông tin của nhóm sản phẩm cần tạo vào form, sau đó click **"Tạo mới"**.

![](media/ketquataomoi.PNG)

- Cập nhật thông tin của nhóm sản phẩm
Chọn nhóm sản phẩm muốn cập nhật thông tin sau đó click **"Cập nhật"**. Giao diện cập nhật thông tin nhóm sản phẩm hiện ra, người quản trị có thể thay đổi 1 số thông tin của nhóm sản phẩm, sau đó click **"Lưu"** để lưu thông tin mới của nhóm sản phẩm.

![](media/capnhatthongtinnhomsanpham.PNG)

![](media/ketquacapnhat.PNG)

![](media/ketquacapnhat1.PNG)

**2. Hệ thống kho hàng**
    
![](media/hethongkhohang.PNG)
Ở đây thực hiện các chức năng: Tạo mới kho hàng, xem danh sách kho hàng, xem chi tiết kho hàng (bao gồm: Thông tin cơ bản, tình trạng kho hàng, lịch sử kho hàng).

**2.1. Tạo mới kho hàng**

![](media/taomoikhohang.PNG)

Điền thông tin đầy đủ vào form tạo mới kho hàng và click **"Tạo mới"**

**2.2. Danh sách kho hàng**

![](media/danhsachkhohang.PNG)
Ở đây chúng ta có thể tìm kiếm thông tin của kho hàng theo tên kho hàng hoặc mã kho hàng.

- Tìm kiếm kho hàng theo tên kho hàng:

![](media/timkiemkhohangtheoten.PNG)

- Tìm kiếm kho hàng theo mã kho hàng:

![](media/timkiemkhohangtheoma.PNG)

- Thông tin cơ bản của kho hàng

Click **"Xem chi tiết"** sau đó vào giao diện click **"Thông tin cơ bản"**
 
![](media/thongtincoban.PNG)

Ở đây chúng ta có thể thay đổi thông tin về địa chỉ, số điện thoại của kho hàng và click **"Cập nhật"**.
- Tình trạng kho hàng

- Click **"Tình trạng kho hàng"** để xem thông tin chi tiết các mặt hàng có trong kho và có thể thực hiện chức năng **"Chuyển kho"**.

![](media/tinhtrangkhohang.PNG)


Ở đây chúng ta có thể tìm kiếm các mặt hàng thông qua tên hàng hóa và mã hàng hóa hoặc thực hiện chức năng **"Chuyển kho"**.
        
- Click **"Chuyển kho"** để sang giao diện **Lưu chuyển hàng hóa**.
    
![](media/luuchuyenhanghoa.PNG)
    
![](media/luuchuyenhanghoa1.PNG)
        
- Lịch sử kho hàng

Click **"Lịch sử kho hàng"** để xem thông tin về lịch sử chuyển kho của kho hàng.
![](media/lichsukhohang.PNG)

Ở đây chúng ta cũng có thể tìm kiếm thông tin các mặt hàng thông qua tên hàng hóa, mã hàng hóa bằng cách nhập thông tin cần tìm kiếm vào các thanh tìm kiếm và nhấn **"Tìm kiếm"**.

## Phần V: Demo video

[https://drive.google.com/file/d/1BWD2KHJYgzQxNcHwHDqPHlZF8QFmAEuL/view?usp=sharing](https://drive.google.com/file/d/1BWD2KHJYgzQxNcHwHDqPHlZF8QFmAEuL/view?usp=sharing)

[media/video.wmv](media/video.wmv)