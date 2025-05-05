Thiết lập môi trường để chạy test
Cài selenium : ```pip install selenium```
Cài thư viện : ```pip install -r requirements.txt```
Chạy từng test case : ```pytest tests/test_create_order.py -k "tên test case" ```
Chạy toàn bộ test : ```pytest```
Chạy test kèm report : ```pytest --html=report.html --maxfail=1 --disable-warnings```

Cấu trúc project
1. venv: cài môi trường chạy python, kích hoạt để dùng 
``` python -m venv .venv```
```.\.venv\Scripts\activate ```
2. config : cấu hình dự án, connect db, mở trình duyệt ...
3. pages: chứa các phần tử và các thao tác của trang
4. tests: chưa test case
