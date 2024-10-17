use master
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'fci_project')
BEGIN
    DROP DATABASE fci_project;
END

create database fci_project;

use  fci_project;

IF OBJECT_ID('Products', 'U') IS NOT NULL
    DROP TABLE Products;

CREATE TABLE Products (
    id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,  
    name NVARCHAR(1000),                         
    quota INT,                                  
    price INT,                                  
    image NVARCHAR(1000),                        
    category NVARCHAR(1000)                      
);

INSERT INTO Products (name, quota, price, image, category)
VALUES 
(N'Dép nữ trung niên da xoắn cho mẹ - Dép cho mẹ cho bà cao 5cm - Bao êm, nhẹ, dễ đi', 100, 99000, 'https://down-vn.img.susercontent.com/file/829ca1339ee63c5591a73ea937e66bf6.webp', N'Giầy cao gót'),
(N'GIÀY CAO GÓT MÃ TLC93 CAO 8P CÓ 2 MÀU ĐEN DA LỘN, KEM DA TRƠN THỜI TRANG 2023', 150, 72000, 'https://down-vn.img.susercontent.com/file/vn-11134201-7qukw-leuyk4ce8sjue2.webp', N'Giầy cao gót'),
(N'Giày cao gót nữ đế nhọn thắt nơ 7 phân, giày sandal 7 phân quai ngọc hottrend', 200, 25000, 'https://down-vn.img.susercontent.com/file/5003776fbabc84fdaccb8a247e1331dd.webp', N'Giầy cao gót'),
(N'Giày Sandal Cao Gót Nữ SIZE 35-43 GNC72 Đế Vuông 7P hai màu đen, kem sang trọng quý phái', 50, 85000, 'https://down-vn.img.susercontent.com/file/vn-11134207-23030-wjadqms3wmov10.webp', N'Giầy cao gót'),
(N'Giày Mũi Nhọn Mã C4 Phối Dây Hở Gót Cao 5cm (BÍT HẬU)', 120, 95000, 'https://down-vn.img.susercontent.com/file/f9aacaec37844dcfa9e106cf35bddde3.webp', N'Giầy cao gót'),
(N'Giày nam sneakers thể thao phong cách Hàn Quốc', 80, 100000, 'https://down-vn.img.susercontent.com/file/vn-11134201-7r98o-lrzxvn7yi6ska1.webp', N'Giầy thể thao'),
(N'Giày thể thao Chzk TYT051 thời trang năng động cho nữ', 130, 85000, 'https://down-vn.img.susercontent.com/file/36091aad175c5d95dbff0b4806b24ed1.webp', N'Giầy thể thao'),
(N'Giày Thể Thao Nam Tăng Chiều Cao Thoáng Khí Phong Cách Hàn Quốc Giày Nam', 60, 136000, 'https://down-vn.img.susercontent.com/file/cn-11134207-7r98o-lkyqq8di3b8t74.webp', N'Giầy thể thao'),
(N'Giày Thể Thao Trắng Phối Lưới Thoáng Khí Thời Trang Cho Nữ', 90, 123000, 'https://down-vn.img.susercontent.com/file/cn-11134207-7qukw-lgt0h6bs9fxb4d.webp', N'Giầy thể thao'),
(N'Giày Sneaker Nam Cổ Lỡ WATAHH Dây Viền Hottrend', 110, 162000, 'https://down-vn.img.susercontent.com/file/0e734daf5bf7249fcc63b8bf7016575d.webp', N'Giầy thể thao'),
(N'Giày búp bê da mũi tròn phong cách Mary Jane dễ thương', 80, 55000, 'https://down-vn.img.susercontent.com/file/sg-11134201-7qvd1-lgyqaa027wfu63.webp', N'Giầy búp bê'),
(N'BIKENIKE Giày búp bê giày nữ 2023', 130, 72000, 'https://down-vn.img.susercontent.com/file/sg-11134201-7rbm9-lpc8jzmfltmu27.webp', N'Giầy búp bê'),
(N'Giày Búp Bê Đế Dày Phong Cách Lolita Thời Trang Cho Nữ', 60, 48000, 'https://down-vn.img.susercontent.com/file/sg-11134201-7rcd4-lqyj6a9e38l428.webp', N'Giầy búp bê'),
(N'BINQIAO giày búp bê nữ 2024NEW Giày búp bê Lolita cá tính dễ thương đơn giản da FLF2490MW0 38Z240919', 90, 67000, 'https://down-vn.img.susercontent.com/file/cn-11134211-7ras8-m0fpuec3mkef03.webp', N'Giầy búp bê'),
(N'Giày Búp Bê Lolita 2 Quai Ngang Chéo Da Bóng Phong Cách Dễ Thương Thời Trang', 110, 82000, 'https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lvsnhec5tke170.webp', N'Giầy búp bê'),
(N'Bộ phụ kiện bảo vệ cáp và củ sạc PD 18/20W bằng silicon hoạt hình dễ thương', 40, 90000, 'https://down-vn.img.susercontent.com/file/vn-11134201-7r98o-lnibi0x49mnh7a.webp', N'Phụ kiện'),
(N'Bộ phụ kiện bảo vệ củ sạc và cáp sạc PD18/20W bằng silicon cao cấp', 70, 62000, 'https://down-vn.img.susercontent.com/file/vn-11134201-7r98o-lxawb4ebmn6j72.webp', N'Phụ kiện'),
(N'CHERRYKOKO Kẹp tóc phủ lông nhung cỡ lớn phong cách Hàn Quốc', 150, 56000, 'https://down-vn.img.susercontent.com/file/vn-11134201-7r98o-lt5106ky68fi42.webp', N'Phụ kiện'),
(N'Dây chuyền ngọc trai nhân tạo Doudou Vòng cổ choker đính đá đi tiệc Phụ kiện Dây chuyền nữ cá tính đẹp Hàn Quốc XL012', 100, 98000, 'https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lqcvtkm1rs9e22.webp', N'Phụ kiện'),
(N'Dây chuyền nam mạ vàng Bracelet sang trọng', 80, 61000, 'https://down-vn.img.susercontent.com/file/d6dd224adf2fb0fee8c1e09abbaac82b.webp', N'Phụ kiện')


SELECT * FROM Products;
