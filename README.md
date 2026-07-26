# ☁️ BÁO CÁO ĐỒ ÁN MÔN ĐIỆN TOÁN ĐÁM MÂY (CLOUD COMPUTING)
> **Học phần**: Điện toán đám mây (Cloud Computing)  
> **Chủ đề**: AWS Bảo mật & Chứng thực người dùng  
> **Sinh viên thực hiện**: Trần Lộc  
> **Repository**: [Tranloc12/CloudComputing](https://github.com/Tranloc12/CloudComputing)  
---
![AWS](https://img.shields.io/badge/Cloud-AWS-orange.svg?style=flat&logo=amazon-aws)
![Cognito](https://img.shields.io/badge/Security-Cognito-red.svg?style=flat&logo=amazon-aws)
![IAM](https://img.shields.io/badge/Identity-IAM-blue.svg?style=flat&logo=amazon-aws)
![S3](https://img.shields.io/badge/Storage-S3-green.svg?style=flat&logo=amazon-s3)
---
## 📌 MỤC LỤC
1. [📖 Giới Thiệu Đề Tài](#1-giới-thiệu-đề-tài)
2. [🏛️ Dịch Vụ AWS Sử Dụng](#2-dịch-vụ-aws-sử-dụng)
3. [📁 Cấu Trúc Thư Mục](#3-cấu-trúc-thư-mục)
4. [🔐 Quy Trình Xác Thực](#4-quy-trình-xác-thực)
5. [📊 Kịch Bản Kiểm Thử](#5-kịch-bản-kiểm-thử)
6. [🛠️ Hướng Dẫn Cài Đặt](#6-hướng-dẫn-cài-đặt)
7. [👨‍💻 Thông Tin Sinh Viên](#7-thông-tin-sinh-viên)
---
## 1. 📖 GIỚI THIỆU ĐỀ TÀI
Đề tài **AWS Bảo Mật & Chứng Thực Người Dùng** xây dựng giải pháp quản lý danh tính, xác thực (Authentication) và phân quyền (Authorization) người dùng an toàn trên hạ tầng đám mây AWS.
### 🎯 Mục tiêu trọng tâm:
* Quản lý tài khoản với **Amazon Cognito User Pools**.
* Cấp quyền truy cập dựa trên JWT token bằng **Cognito Identity Pools** & **AWS IAM**.
* Phân quyền tối thiểu (Least Privilege) với **IAM Policies**.
* Mã hóa dữ liệu & hỗ trợ xác thực hai yếu tố (**MFA**).
---
## 2. 🏛️ DỊCH VỤ AWS SỬ DỤNG
- 🔐 **Amazon Cognito User Pool**: Quản lý đăng ký, đăng nhập, OTP Email & phát hành JWT Tokens.
- 🛡️ **Amazon Cognito Identity Pool**: Cấp AWS Temporary Credentials từ JWT Token.
- 📜 **AWS IAM**: Định nghĩa Roles & Policies phân quyền chi tiết cho Admin/User.
- 🗄️ **AWS S3**: Lưu trữ dữ liệu an toàn dựa trên Bucket Policy.
- 📈 **AWS CloudWatch**: Ghi log và cảnh báo truy cập bất thường.
---
## 3. 📁 CẤU TRÚC THƯ MỤC
```text
CloudComputing/
├── README.md
├── Docs/
│   ├── BaoCao_CloudComputing.docx
│   └── Architecture_Diagram.png
├── Configurations/
│   ├── cognito-user-pool.json
│   └── s3-bucket-policy.json
└── Src/
    ├── auth-service.js
    └── aws-config.js
```
---
## 4. 🔐 QUY TRÌNH XÁC THỰC
1. 📝 **Đăng ký & OTP**: User đăng ký ➔ Cognito gửi OTP xác thực Email.
2. 🔑 **Đăng nhập & Token**: Trả về `ID Token`, `Access Token`, `Refresh Token`.
3. 🛡️ **Đổi Credentials**: Đổi Token tại Identity Pool lấy AWS Credentials tạm thời.
4. 🗄️ **Truy cập S3**: IAM cấp quyền đọc/ghi dữ liệu trên S3 Bucket.
---
## 5. 📊 KỊCH BẢN KIỂM THỬ
* **TC01**: Đăng ký tài khoản ➔ Tạo User thành công (`PASS`)
* **TC02**: Xác thực OTP Email ➔ Kích hoạt User (`PASS`)
* **TC03**: Đăng nhập ➔ Trả về JWT Token (`PASS`)
* **TC04**: Sai mật khẩu 5 lần ➔ Tự động khóa tài khoản (`PASS`)
* **TC05**: Token hết hạn ➔ Lỗi `403 Access Denied` (`PASS`)
---
## 6. 🛠️ HƯỚNG DẪN CÀI ĐẶT
### 🔹 Bước 1: Cấu hình AWS CLI
```bash
aws configure
```
### 🔹 Bước 2: Tạo Cognito User Pool
1. Vào AWS Console ➔ Chọn **Amazon Cognito**.
2. Chọn **Create user pool** ➔ Chọn Sign-in bằng `Email`.
### 🔹 Bước 3: Áp dụng S3 Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```
---
## 👨‍💻 THÔNG TIN SINH VIÊN
* **Họ và tên**: Trần Lộc
* **Môn học**: Điện toán đám mây (Cloud Computing)
* **GitHub**: [@Tranloc12](https://github.com/Tranloc12)
