# E-Commerce Testing Project - Sauce Demo

Bộ test script tự động kiểm thử các tính năng chính của website https://www.saucedemo.com/

## Cấu Trúc Dự Án

```
ecommerce_project/
├── conftest.py                 # Pytest configuration & fixtures
├── requirements.txt            # Python dependencies
├── pages/
│   ├── base_page.py           # Base class cho Page Objects
│   ├── login_page.py          # Login page object
│   ├── inventory_page.py      # Products/Inventory page object
│   ├── cart_page.py           # Shopping cart page object
│   └── checkout_page.py       # Checkout page object
├── tests/
│   ├── test_login.py          # Login functionality tests
│   ├── test_cart.py           # Add/Remove from cart tests
│   ├── test_sorting.py        # Product sorting tests
│   └── test_checkout.py       # Checkout process tests
└── utils/
    └── credentials.py          # Test credentials
```

## Các Tính Năng Được Kiểm Thử

### 1. Kiểm thử Đăng nhập (test_login.py)
- ✅ Đăng nhập thành công với thông tin hợp lệ
- ✅ Đăng nhập thất bại với password sai
- ✅ Đăng nhập thất bại với username sai
- ✅ Đăng nhập thất bại với cả hai thông tin sai
- ✅ Để trống các trường thông tin

**Test cases:** 5
- `test_login_success` - Đăng nhập thành công
- `test_login_fail_wrong_password` - Password sai
- `test_login_fail_wrong_username` - Username sai
- `test_login_fail_both_wrong` - Cả hai sai
- `test_login_empty_fields` - Trường trống

### 2. Kiểm thử Thêm sản phẩm vào Giỏ hàng (test_cart.py - Add to Cart)
- ✅ Thêm một sản phẩm vào giỏ hàng
- ✅ Xác minh số lượng sản phẩm trên biểu tượng giỏ hàng
- ✅ Kiểm tra sản phẩm hiển thị trong trang giỏ hàng
- ✅ Thêm nhiều sản phẩm khác nhau

**Test cases:** 4
- `test_add_single_product_to_cart` - Thêm 1 sản phẩm
- `test_add_multiple_products_to_cart` - Thêm 3 sản phẩm
- `test_product_appears_in_cart_page` - Sản phẩm xuất hiện trong trang giỏ hàng
- `test_add_multiple_different_products_verify_in_cart` - Thêm nhiều & xác minh

### 3. Kiểm thử Xóa sản phẩm khỏi Giỏ hàng (test_cart.py - Remove from Cart)
- ✅ Xóa sản phẩm từ trang giỏ hàng
- ✅ Xóa sản phẩm từ trang danh mục (nút Remove)
- ✅ Xóa một trong nhiều sản phẩm
- ✅ Xác minh giỏ hàng cập nhật sau khi xóa

**Test cases:** 4
- `test_remove_product_from_cart_page` - Xóa từ trang giỏ hàng
- `test_remove_product_from_inventory_page` - Xóa từ trang danh mục
- `test_remove_one_of_multiple_products` - Xóa một trong nhiều
- `test_cart_updates_reflect_on_badge` - Badge cập nhật sau xóa

### 4. Kiểm thử Sắp xếp Sản phẩm (test_sorting.py)
- ✅ Sắp xếp theo tên A-Z
- ✅ Sắp xếp theo tên Z-A
- ✅ Sắp xếp theo giá Thấp-Cao
- ✅ Sắp xếp theo giá Cao-Thấp
- ✅ Chuyển giữa các tùy chọn sắp xếp

**Test cases:** 6
- `test_sort_by_name_a_to_z` - Sắp xếp A-Z
- `test_sort_by_name_z_to_a` - Sắp xếp Z-A
- `test_sort_by_price_low_to_high` - Sắp xếp giá thấp-cao
- `test_sort_by_price_high_to_low` - Sắp xếp giá cao-thấp
- `test_sort_maintains_product_information` - Sắp xếp giữ nguyên thông tin
- `test_switch_between_sort_options` - Chuyển giữa tùy chọn

### 5. Kiểm thử Quy trình Thanh toán (test_checkout.py)
- ✅ Thanh toán hoàn chỉnh với thông tin hợp lệ
- ✅ Thanh toán với 1 sản phẩm
- ✅ Thanh toán với nhiều sản phẩm
- ✅ Xác minh thông tin đơn hàng trên trang Overview
- ✅ Xác minh thông báo đặt hàng thành công
- ✅ Xác minh các trường không hợp lệ

**Test cases: Checkout Success (4)**
- `test_complete_checkout_with_valid_info` - Thanh toán hoàn chỉnh
- `test_checkout_with_single_product` - Thanh toán 1 sản phẩm
- `test_checkout_with_multiple_products` - Thanh toán nhiều sản phẩm
- `test_checkout_verify_order_details_on_overview` - Xác minh chi tiết đơn hàng

**Test cases: Checkout Validation (6)**
- `test_checkout_missing_first_name` - Thiếu tên
- `test_checkout_missing_last_name` - Thiếu họ
- `test_checkout_missing_zip_code` - Thiếu mã bưu điện
- `test_checkout_all_fields_empty` - Trường trống
- `test_checkout_with_special_characters_in_name` - Ký tự đặc biệt
- `test_checkout_correct_info_after_error` - Nhập đúng sau lỗi

## Cài đặt

### 1. Yêu cầu hệ thống
- Python 3.8 trở lên
- Google Chrome (cập nhật mới nhất)
- pip (trình quản lý package Python)

### 2. Cài đặt thư viện

```bash
# Cài đặt tất cả dependencies
pip install -r requirements.txt

# Hoặc cài đặt riêng lẻ
pip install selenium webdriver-manager pytest
```

## Chạy Tests

### Chạy tất cả tests
```bash
pytest
```

### Chạy tests với output chi tiết
```bash
pytest -v
```

### Chạy tests với output chi tiết + print statements
```bash
pytest -v -s
```

### Chạy test file cụ thể
```bash
pytest tests/test_login.py
pytest tests/test_cart.py
pytest tests/test_sorting.py
pytest tests/test_checkout.py
```

### Chạy test class cụ thể
```bash
pytest tests/test_cart.py::TestAddToCart
pytest tests/test_cart.py::TestRemoveFromCart
pytest tests/test_checkout.py::TestCheckoutValidation
```

### Chạy test function cụ thể
```bash
pytest tests/test_login.py::test_login_success
pytest tests/test_cart.py::TestAddToCart::test_add_single_product_to_cart
```

### Chạy tests với báo cáo coverage (nếu cài pytest-cov)
```bash
pip install pytest-cov
pytest --cov=pages --cov=tests --cov-report=html
```

### Chạy tests ở chế độ headless (không hiển thị trình duyệt)
Mở file `conftest.py` và bỏ comment dòng:
```python
# options.add_argument("--headless=new")
```

## Page Object Model (POM) Architecture

Dự án sử dụng Page Object Model pattern:

- **BasePage** (`pages/base_page.py`) - Lớp base cung cấp các phương thức chung:
  - `find()` - Tìm element với wait
  - `click()` - Click element
  - `type()` - Nhập text
  - `get_text()` - Lấy text
  - `find_all()` - Tìm nhiều elements

- **LoginPage** - Đóng gói logic đăng nhập
- **InventoryPage** - Quản lý trang danh sách sản phẩm
- **CartPage** - Quản lý trang giỏ hàng
- **CheckoutPage** - Quản lý quy trình thanh toán

## Credentials

Thông tin đăng nhập (được định nghĩa trong `utils/credentials.py`):

```python
# Thông tin hợp lệ
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

# Thông tin không hợp lệ
INVALID_USERNAME = "abcxyz"
INVALID_PASSWORD = "123456"
```

## Cấu hình WebDriver

File `conftest.py` cấu hình:
- Tự động tải ChromeDriver phù hợp (webdriver-manager)
- Tối đa hóa cửa sổ Chrome
- Điều hướng đến https://www.saucedemo.com/
- Cleanup sau mỗi test (quit driver)

## Các Tùy chọn Chrome (Options)

Có thể thêm các tùy chọn khác trong `conftest.py`:
```python
# Chạy ở chế độ headless (không hiển thị trình duyệt)
options.add_argument("--headless=new")

# Tắt thông báo
options.add_argument("--disable-notifications")

# Chế độ incognito
options.add_argument("--incognito")
```

## Xử lý Lỗi Thường Gặp

### 1. ChromeDriver không tương thích
```bash
pip install --upgrade webdriver-manager
# Cập nhật Google Chrome lên phiên bản mới nhất
```

### 2. Permission denied / Access denied
Chạy PowerShell với quyền Administrator

### 3. Element not found
- Tăng wait time trong `BasePage.__init__` (hiện tại là 10s)
- Kiểm tra locators có đúng không
- Xem website có thay đổi UI không

### 4. Tests chạy quá chậm
- Bật chế độ headless trong `conftest.py`
- Giảm wait time (chỉ nếu website ổn định)

## Báo cáo Test

Sau khi chạy tests:
- Pytest sẽ hiển thị summary:
  - ✅ Passed - Tests thành công
  - ❌ Failed - Tests thất bại
  - ⚠️ Skipped - Tests bị bỏ qua
  - ⏺️ Errors - Lỗi không mong muốn

## Mở Rộng

Để thêm tests mới:
1. Tạo file test mới trong thư mục `tests/`
2. Tạo Page Objects mới trong thư mục `pages/` nếu cần
3. Đặt tên test functions bắt đầu bằng `test_`
4. Sử dụng `driver` fixture từ `conftest.py`

## Tài Liệu Tham Khảo

- [Selenium Documentation](https://selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Sauce Demo](https://www.saucedemo.com/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## Ghi Chú

- Các tests được thiết kế độc lập - có thể chạy theo bất kỳ thứ tự nào
- Mỗi test sẽ tự đăng nhập - không phụ thuộc vào test trước
- Browser sẽ tự đóng sau mỗi test
- Có thể chạy parallel với pytest-xdist: `pytest -n auto`

## Tác Giả

Tạo cho yêu cầu kiểm thử E-Commerce Website

## License

MIT
