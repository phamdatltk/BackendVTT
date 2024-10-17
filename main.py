from fastapi import FastAPI, Query
import pyodbc

app = FastAPI()

# Hàm kiểm tra kết nối với SQL Server
def test_sql_connection():
    try:
        # Chuỗi kết nối đến SQL Server
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=master;"  # Database mặc định để kiểm tra kết nối
            "UID=trin;"         # Tên user
            "PWD=123;"          # Mật khẩu
        )
        # Kết nối tới SQL Server
        conn = pyodbc.connect(conn_str)
        conn.close()  # Đóng kết nối nếu thành công
        return True
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return False

# Định nghĩa endpoint /TestConnect
@app.get("/TestConnect")
def test_connect():
    if test_sql_connection():
        return {"message": "Success"}
    else:
        return {"message": "Failed to connect to SQL Server"}


# Định nghĩa endpoint / trả về "Hello, World!"
@app.get("/")
def read_root():
    return {"message": "Hello, World"}


# Hàm kết nối đến SQL Server
def get_db_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=fci_project;"   # Tên cơ sở dữ liệu
        "UID=trin;"               # Tên user
        "PWD=123;"                # Mật khẩu
    )
    return pyodbc.connect(conn_str)

# API để lấy danh sách sản phẩm dựa theo category
@app.get("/products")
def get_products(category: str = Query(...)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if category == 'caogot':
        category = 'Giầy cao gót'
    if category == 'sport':
        category = 'Giầy thể thao'
    if category == 'baby':
        category = 'Giầy búp bê'
    if category == 'phukien':
        category = 'Phụ kiện'
        
    
    # SQL để lấy tất cả bản ghi
    if category == None or category == "all":
        cursor.execute("SELECT * FROM Products")
    else:
        cursor.execute("SELECT * FROM Products WHERE category = ?", category)
    
    # Lấy tất cả các bản ghi
    products = cursor.fetchall()
    
    # Đóng kết nối
    conn.close()

    # Chuyển đổi kết quả thành danh sách dict
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "quota": product.quota,
            "price": product.price,
            "image": product.image,
            "category": product.category
        })
    
    return {"products": result}