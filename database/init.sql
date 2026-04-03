-- database/init.sql

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- (Tùy chọn) Thêm sẵn một vài dữ liệu mẫu để test
INSERT INTO users (name) VALUES 
('Đức Anh'),
('Giàng A Lử')
ON CONFLICT DO NOTHING;