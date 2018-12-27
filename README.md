# Phần I: Hướng dẫn cài đặt
## 1. Cài đặt MySQL
Để download MySQL Community, truy cập vào địa chỉ:
[http://dev.mysql.com/downloads/mysql]()

![](https://o7planning.org/vi/10221/cache/images/i/20529.png)

![](https://o7planning.org/vi/10221/cache/images/i/20524.png)

![](https://o7planning.org/vi/10221/cache/images/i/20531.png)

Sau khi download file cài đặt về xong, chạy nó:

![](https://o7planning.org/vi/10221/cache/images/i/20709.png)

![](https://o7planning.org/vi/10221/cache/images/i/20711.png)

Chọn cài đặt tất cả.
![](https://o7planning.org/vi/10221/cache/images/i/20713.png)

Tại bước này bộ cài đặt thông báo máy tính của bạn chưa cài đặt một vài thư viện cần thiết. Vì vậy cần phải nhấn vào các thư viện cần thiết và nhấn nút **"Execute"**.
![](https://o7planning.org/vi/10221/cache/images/i/21283524.png)

![](https://o7planning.org/vi/10221/cache/images/i/21284005.png)

Nhấn **Next** để tiếp tục cài đặt **MySQL**.
![](https://o7planning.org/vi/10221/cache/images/i/21284204.png)

![](https://o7planning.org/vi/10221/cache/images/i/20717.png)

Bộ cài hiển thị các gói sẽ được cài vào.
![](https://o7planning.org/vi/10221/cache/images/i/20719.png)

![](https://o7planning.org/vi/10221/cache/images/i/20721.png)

Cấu hình **MySQL Server**.
![](https://o7planning.org/vi/10221/cache/images/i/20723.png)

![](https://o7planning.org/vi/10221/cache/images/i/20725.png)

![](https://o7planning.org/vi/10221/cache/images/i/21284731.png)

![](https://o7planning.org/vi/10221/cache/images/i/21284820.png)

![](https://o7planning.org/vi/10221/cache/images/i/20729.png)

![](https://o7planning.org/vi/10221/cache/images/i/20731.png)

![](https://o7planning.org/vi/10221/cache/images/i/21285092.png)

![](https://o7planning.org/vi/10221/cache/images/i/20733.png)

![](https://o7planning.org/vi/10221/cache/images/i/20735.png)

![](https://o7planning.org/vi/10221/cache/images/i/20737.png)

![](https://o7planning.org/vi/10221/cache/images/i/21285417.png)

Nhập vào password và nhấn **Check** để kiểm tra việc kết nối với **MySQL**.
![](https://o7planning.org/vi/10221/cache/images/i/20739.png)

![](https://o7planning.org/vi/10221/cache/images/i/20741.png)

![](https://o7planning.org/vi/10221/cache/images/i/20743.png)

![](https://o7planning.org/vi/10221/cache/images/i/20745.png)

Nhấn **Finish** để hoàn thành cài đặt.
![](https://o7planning.org/vi/10221/cache/images/i/20747.png)

## **2. Sử dụng MySQL Workbench**
Mở **MySQL Workbench:**
![](https://o7planning.org/vi/10221/cache/images/i/20765.png)

![](https://o7planning.org/vi/10221/cache/images/i/20767.png)
Hình ảnh **MySQL Workbench** với một vài cơ sở dữ liệu mẫu.
![](https://o7planning.org/vi/10221/cache/images/i/20769.png)
Tạo cơ sở dữ liệu với tên là doan2 tại đây:
![](https://o7planning.org/vi/10221/cache/images/i/20771.png)

## **3. Cài đặt django**
Với windows, mở cửa sổ terminal trong windows và gõ:
> **pip install django**

Với linux và mac, mở cửa sổ terminal và gõ:
> **sudo apt-get install django**

Tạo django project có tên là doan2
> **django-admin startproject doan2**

Tiếp theo cd vào thư mục doan2 và tạo 1 app với tên là hethong
> **manage.py startapp hethong**

## **4. Cài đặt pymysql**
Tương tự cài đặt django. Mở terminal và gõ:

Đối với windows:
> **pip install pymysql**  

Đối với linux và mac:
> **sudo apt-get install pymysql**

## **4. Kết nối django với MySQL**
- Vào file settings.py của project doan2 vừa tạo ở trên và thay đổi các thông số trong DATABASE.
    <img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/48921805_1172268686261581_4248535946456203264_n.png?_nc_cat=103&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=401d7f203e051b14c134b3c455ae5b7b&amp;oe=5C8F4D9C" alt="" class="img" style="width: 436px; height: 197px;">
    
    Trong đó user và password là user và password lúc cài đặt MySQL.
- Vào file __init__.py của project và gõ:

---
    import pymysql
    pymysql.install_as_MySQLdb()
---

# Phần II: Hướng dẫn sử dụng
- Mở terminal và chuyển đến thư mục project và gõ:

> **manage.py runserver**

để chạy chương trình.
- Mở trình duyệt và gõ địa chỉ: [localhost:8000/nhaphanphoi]()

Giao diện của hệ thống hiện ra (đây là giao diện của nhà phân phối).

![](images/giaodienchung.PNG)
**1. Hệ thống sản phẩm**

![](images/hethongsanpham.PNG)
Ở đây thực hiện các chức năng: Tạo mới sản phẩm cho nhà phân phối, hiển thị danh sách các sản phẩm, nhóm sản phẩm, tạo mới nhóm sản phẩm, cập nhật thông tin của sản phẩm và nhóm sản phẩm, tìm kiếm thông tin sản phẩm.

**1.1. Tạo mới sản phẩm**

![](images/taomoisanpham.PNG)
Ở đây chúng ta điền đầy đủ thông tin của form **Tạo mới sản phẩm** và click **"Tạo mới"**.

**1.2. Danh sách sản phẩm**

![](images/danhsachsanpham.PNG)

- Cập nhật thông tin sản phẩm
 
    ![](images/capnhatthongtinsanpham.PNG)
Ở đây chúng ta có thể thay đổi 1 số thông tin của sản phẩm và click **"Cập nhật"** để cập nhật lại thông tin của sản phẩm.
- Tìm kiếm sản phẩm theo tên và nhóm hàng hóa
Nhập tên hàng hóa và nhóm sản phẩm, sau đó click **"Tìm kiếm"**.
![](images/timkiemtheoten.PNG)
- Tìm kiếm sản phẩm theo mã
Nhập mã sản phẩm sau đó click **"Tìm kiếm"**.
![](images/timkiemtheoma.PNG)
**1.3. Hệ thống nhóm sản phẩm**
![](images/hethongnhomsanpham.PNG)
Ở đây chúng ta có thể thực hiện chức năng tạo mới nhóm sản phẩm và cập nhật thông tin của nhóm sản phẩm.
- Tạo mới nhóm sản phẩm
![](images/taomoinhomhanghoa.PNG)
Điền đầy đủ thông tin của nhóm sản phẩm cần tạo vào form, sau đó click **"Tạo mới"**.

    ![](images/ketquataomoi.PNG)

- Cập nhật thông tin của nhóm sản phẩm
Chọn nhóm sản phẩm muốn cập nhật thông tin sau đó click **"Cập nhật"**. Giao diện cập nhật thông tin nhóm sản phẩm hiện ra, người quản trị có thể thay đổi 1 số thông tin của nhóm sản phẩm, sau đó click **"Lưu"** để lưu thông tin mới của nhóm sản phẩm.
![](images/capnhatthongtinnhomsanpham.PNG)

    **2. Hệ thống kho hàng**
![](images/hethongkhohang.PNG)
Ở đây thực hiện các chức năng: Tạo mới kho hàng, xem danh sách kho hàng, xem chi tiết kho hàng (bao gồm: Thông tin cơ bản, tình trạng kho hàng, lịch sử kho hàng).

**2.1. Tạo mới kho hàng**
![](images/taomoikhohang.PNG)
Điền thông tin đầy đủ vào form tạo mới kho hàng và click **"Tạo mới"**
**2.2. Danh sách kho hàng**
![](images/danhsachkhohang.PNG)
Ở đây chúng ta có thể tìm kiếm thông tin của kho hàng theo tên kho hàng hoặc mã kho hàng.
Tìm kiếm kho hàng theo tên kho hàng:
![](images/timkiemkhohangtheoten.PNG)
Tìm kiếm kho hàng theo mã kho hàng:
![](images/timkiemkhohangtheoma.PNG)

- Thông tin cơ bản của kho hàng
Click **"Xem chi tiết"** sau đó vào giao diện click **"Thông tin cơ bản"**
![](images/thongtincoban.PNG)
Ở đây chúng ta có thể thay đổi thông tin về địa chỉ, số điện thoại của kho hàng và click **"Cập nhật"**.
- Tình trạng kho hàng

    - Click **"Tình trạng kho hàng"** để xem thông tin chi tiết các mặt hàng có trong kho và có thể thực hiện chức năng **"Chuyển kho"**.
![](images/tinhtrangkhohang.PNG)

        Ở đây chúng ta có thể tìm kiếm các mặt hàng thông qua tên hàng hóa và mã hàng hóa hoặc thực hiện chức năng **"Chuyển kho"**.
    - Click **"Chuyển kho"** để sang giao diện **Lưu chuyển hàng hóa**.
        ![](images/luuchuyenhanghoa.PNG)
        
        ![](images/luuchuyenhanghoa1.PNG)
    
- Lịch sử kho hàng

    Click **"Lịch sử kho hàng"** để xem thông tin về lịch sử chuyển kho của kho hàng.
![](images/lichsukhohang.PNG)
Ở đây chúng ta cũng có thể tìm kiếm thông tin các mặt hàng thông qua tên hàng hóa, mã hàng hóa bằng cách nhập thông tin cần tìm kiếm vào các thanh tìm kiếm và nhấn **"Tìm kiếm"**.







    
    

