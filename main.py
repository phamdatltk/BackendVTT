from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import pyodbc
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Thêm middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bạn có thể thay đổi thành danh sách các origin được phép
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các phương thức (GET, POST, PUT, DELETE, ...)
    allow_headers=["*"],  # Cho phép tất cả các header
)

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

# API để xóa sản phẩm theo ID
@app.delete("/products/{id}")
def delete_product(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Kiểm tra xem sản phẩm có tồn tại không
    cursor.execute("SELECT * FROM Products WHERE id = ?", id)
    product = cursor.fetchone()
    
    if not product:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")

    # Xóa sản phẩm
    cursor.execute("DELETE FROM Products WHERE id = ?", id)
    conn.commit()  # Lưu thay đổi
    conn.close()
    
    return {"message": "Product deleted successfully"}

# Định nghĩa model cho sản phẩm
class Product(BaseModel):
    name: str
    quota: int
    price: float
    image: str
    category: str
    
# API để thêm sản phẩm mới
@app.post("/products")
def create_product(product: Product):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Thêm sản phẩm vào cơ sở dữ liệu
    cursor.execute(
        "INSERT INTO Products (name, quota, price, image, category) VALUES (?, ?, ?, ?, ?)",
        product.name,
        product.quota,
        product.price,
        product.image,
        product.category
    )
    conn.commit()  # Lưu thay đổi
    conn.close()

    return {"message": "Product created successfully", "product": product}

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Kiểm tra xem sản phẩm có tồn tại không
    cursor.execute("SELECT * FROM Products WHERE id = ?", id)
    existing_product = cursor.fetchone()
    
    if not existing_product:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")

    # Cập nhật thông tin sản phẩm
    cursor.execute(
        "UPDATE Products SET name = ?, quota = ?, price = ?, image = ?, category = ? WHERE id = ?",
        product.name,
        product.quota,
        product.price,
        product.image,
        product.category,
        id
    )
    conn.commit()  # Lưu thay đổi
    conn.close()
    
    return {"message": "Product updated successfully", "product": product}