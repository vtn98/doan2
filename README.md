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
- Mở terminal và chuyển đến thư mục project doan2 vừa tạo ở trên và gõ:

> **manage.py runserver**

để chạy chương trình.
- Mở trình duyệt và gõ địa chỉ: [localhost:8000/nhaphanphoi]()

Giao diện của hệ thống hiện ra (đây là giao diện của nhà phân phối).

<img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/49005442_2247628108818163_7111672699155382272_n.png?_nc_cat=102&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=0eaececc66d66ec6e6280e5385c5b747&amp;oe=5C9460AD" alt="" class="img" style="width: 718px; height: 366px;">

**1. Hệ thống sản phẩm**

<img src="https://scontent.fsgn2-1.fna.fbcdn.net/v/t1.15752-9/49199902_2063079550416048_2738100427827445760_n.png?_nc_cat=111&amp;_nc_ht=scontent.fsgn2-1.fna&amp;oh=ac6471f5665cecb0842867c045b17933&amp;oe=5C94913D" alt="" class="img" style="width: 718px; height: 366px;">
Ở đây thực hiện các chức năng: Tạo mới sản phẩm cho nhà phân phối, hiển thị danh sách các sản phẩm, nhóm sản phẩm, tạo mới nhóm sản phẩm, cập nhật thông tin của sản phẩm và nhóm sản phẩm, tìm kiếm thông tin sản phẩm.

**1.1. Tạo mới sản phẩm**

<img src="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/48427766_719664675084750_6361282968413011968_n.png?_nc_cat=110&amp;_nc_ht=scontent.fsgn2-3.fna&amp;oh=4749884675c82ceb21e9c5c3ec1f00e2&amp;oe=5CD43E06" alt="" class="img" style="width: 718px; height: 365px;">

Ở đây chúng ta điền đầy đủ thông tin của form **Tạo mới sản phẩm** và click **"Tạo mới"**.

**1.2. Danh sách sản phẩm**

<img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/48981174_2031805983574967_6185311105959591936_n.png?_nc_cat=101&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=a47d057987be90ef023a961ddd6e66c0&amp;oe=5CD683F9" alt="" class="img" style="width: 718px; height: 365px;">

- Cập nhật thông tin sản phẩm
 
<img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/49196511_215410002729350_7712765909240119296_n.png?_nc_cat=102&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=8239e79e98c9f7302f81ecc064284e4e&amp;oe=5CD1E3DA" alt="" class="img" style="width: 718px; height: 366px;">

Ở đây chúng ta có thể thay đổi 1 số thông tin của sản phẩm và click **"Cập nhật"** để cập nhật lại thông tin của sản phẩm.
- Tìm kiếm sản phẩm theo tên và nhóm hàng hóa bằng cách nhập tên hàng hóa và nhóm sản phẩm, sau đó click **"Tìm kiếm"**.

<img src="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/48992745_498054904017355_3431771473293869056_n.png?_nc_cat=108&amp;_nc_ht=scontent.fsgn2-3.fna&amp;oh=66c6f8e5af16b47ffb0adf2567684371&amp;oe=5CD8F68D" alt="" class="img" style="width: 718px; height: 355px;">

- Tìm kiếm sản phẩm theo mã bằng cách nhập mã sản phẩm sau đó click **"Tìm kiếm"**.

<img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/49171355_605040963250413_8826281088906166272_n.png?_nc_cat=101&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=4342b4680af79692abdd5831491a1a4a&amp;oe=5C8D98F2" alt="" class="img" style="width: 718px; height: 353px;">
    
**1.3. Hệ thống nhóm sản phẩm**

<img src="https://scontent.fsgn2-1.fna.fbcdn.net/v/t1.15752-9/49292630_403341683740117_3025360257334378496_n.png?_nc_cat=107&amp;_nc_ht=scontent.fsgn2-1.fna&amp;oh=37c23d7310631d1839092aa893aaf2e9&amp;oe=5C96BABE" alt="" class="img" style="width: 718px; height: 366px;">
Ở đây chúng ta có thể thực hiện chức năng tạo mới nhóm sản phẩm và cập nhật thông tin của nhóm sản phẩm.

- Tạo mới nhóm sản phẩm
<img src="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/48425853_552730938534436_1917154468995006464_n.png?_nc_cat=106&amp;_nc_ht=scontent.fsgn2-3.fna&amp;oh=d8210094851f5475a6fdcb1bb423ab0c&amp;oe=5CD30B8A" alt="" class="img" style="width: 718px; height: 366px;">
Điền đầy đủ thông tin của nhóm sản phẩm cần tạo vào form, sau đó click **"Tạo mới"**.

    <img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/49072177_1885089551540401_7202568582394281984_n.png?_nc_cat=109&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=4b5a19470ced67ebd595d35eb28d7f95&amp;oe=5C9EAB86" alt="" class="img" style="width: 718px; height: 365px;">
    
    <img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/49110906_2799423250074046_9081102052628627456_n.png?_nc_cat=103&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=359a8cc8ac4f13bbcef9c645173b5cc7&amp;oe=5CD545D5" alt="" class="img" style="width: 718px; height: 355px;">

- Cập nhật thông tin của nhóm sản phẩm
Chọn nhóm sản phẩm muốn cập nhật thông tin sau đó click **"Cập nhật"**. Giao diện cập nhật thông tin nhóm sản phẩm hiện ra, người quản trị có thể thay đổi 1 số thông tin của nhóm sản phẩm, sau đó click **"Lưu"** để lưu thông tin mới của nhóm sản phẩm.
<img src="https://scontent.fsgn2-1.fna.fbcdn.net/v/t1.15752-9/49147993_396268661116562_5335922847195856896_n.png?_nc_cat=105&amp;_nc_ht=scontent.fsgn2-1.fna&amp;oh=52443ff022277a4e6f35ce465e257389&amp;oe=5CD13E1C" alt="" class="img" style="width: 718px; height: 366px;">

    **2. Hệ thống kho hàng**
    
<img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/48421625_218872242326632_8805683211733565440_n.png?_nc_cat=102&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=6dd599e09232384a4f3119af9bc0ea75&amp;oe=5C9E1188" alt="" class="img" style="width: 718px; height: 366px;">
Ở đây thực hiện các chức năng: Tạo mới kho hàng, xem danh sách kho hàng, xem chi tiết kho hàng (bao gồm: Thông tin cơ bản, tình trạng kho hàng, lịch sử kho hàng).

**2.1. Tạo mới kho hàng**

<img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/49192827_992638364253168_8441283789610549248_n.png?_nc_cat=109&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=5da4048bf86538618a025cf56fb9fb63&amp;oe=5C9C75A4" alt="" class="img" style="width: 718px; height: 354px;">
Điền thông tin đầy đủ vào form tạo mới kho hàng và click **"Tạo mới"**

**2.2. Danh sách kho hàng**

<img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/49038964_604450513344840_4980305825739309056_n.png?_nc_cat=101&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=a9d1fa50b7b5710e4223c23b9125e6a1&amp;oe=5C8CFCCF" alt="" class="img" style="width: 718px; height: 366px;">
Ở đây chúng ta có thể tìm kiếm thông tin của kho hàng theo tên kho hàng hoặc mã kho hàng.

- Tìm kiếm kho hàng theo tên kho hàng:
<img src="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.15752-9/48428154_593547384391823_932949394423021568_n.png?_nc_cat=110&amp;_nc_ht=scontent.fsgn2-3.fna&amp;oh=b4d97676bc646eaf4d5e6e1666cc2ff7&amp;oe=5C8CE3F9" alt="" class="img" style="width: 718px; height: 366px;">

- Tìm kiếm kho hàng theo mã kho hàng:
<img src="https://scontent.fsgn2-1.fna.fbcdn.net/v/t1.15752-9/48926400_588755881570439_7327703618499379200_n.png?_nc_cat=111&amp;_nc_ht=scontent.fsgn2-1.fna&amp;oh=94210edf4da92c2cd1bba135a793bec6&amp;oe=5C92DBBB" alt="" class="img" style="width: 718px; height: 366px;">

- Thông tin cơ bản của kho hàng

Click **"Xem chi tiết"** sau đó vào giao diện click **"Thông tin cơ bản"**
<img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/48935108_465582820635468_3498015352355291136_n.png?_nc_cat=102&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=699fdb899f1ec8ab74994bcbbbb3cf7e&amp;oe=5CD93F72" alt="" class="img" style="width: 718px; height: 366px;">

Ở đây chúng ta có thể thay đổi thông tin về địa chỉ, số điện thoại của kho hàng và click **"Cập nhật"**.
- Tình trạng kho hàng

    - Click **"Tình trạng kho hàng"** để xem thông tin chi tiết các mặt hàng có trong kho và có thể thực hiện chức năng **"Chuyển kho"**.
<img src="https://scontent.fsgn2-1.fna.fbcdn.net/v/t1.15752-9/48421341_344717236310225_8703990278928728064_n.png?_nc_cat=105&amp;_nc_ht=scontent.fsgn2-1.fna&amp;oh=454cbdb9e89411874973cd86809cb3fe&amp;oe=5C90038F" alt="" class="img" style="width: 718px; height: 365px;">

        Ở đây chúng ta có thể tìm kiếm các mặt hàng thông qua tên hàng hóa và mã hàng hóa hoặc thực hiện chức năng **"Chuyển kho"**.
        
    - Click **"Chuyển kho"** để sang giao diện **Lưu chuyển hàng hóa**.
    
        <img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/48366073_2203615666632711_8481425370002751488_n.png?_nc_cat=101&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=256df63eaedb7e5fef4a4155c13dd1ed&amp;oe=5C8E4872" alt="" class="img" style="width: 718px; height: 363px;">
    
        <img src="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.15752-9/48422144_1882714578494294_5246069906570477568_n.png?_nc_cat=100&amp;_nc_ht=scontent.fsgn2-2.fna&amp;oh=16acf7ac1117a2013e4f3a4b49717d32&amp;oe=5C990CD6" alt="" class="img" style="width: 718px; height: 365px;">
        
- Lịch sử kho hàng

    Click **"Lịch sử kho hàng"** để xem thông tin về lịch sử chuyển kho của kho hàng.
<img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.15752-9/48424980_2179785839002820_4028604582627115008_n.png?_nc_cat=109&amp;_nc_ht=scontent.fsgn2-4.fna&amp;oh=f4e5b7183e1a32d717f04c3a7ba41359&amp;oe=5C90BCB4" alt="" class="img" style="width: 718px; height: 366px;">

Ở đây chúng ta cũng có thể tìm kiếm thông tin các mặt hàng thông qua tên hàng hóa, mã hàng hóa bằng cách nhập thông tin cần tìm kiếm vào các thanh tìm kiếm và nhấn **"Tìm kiếm"**.







    
    

