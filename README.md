# ☁️ BÁO CÁO ĐỒ ÁN MÔN ĐIỆN TOÁN ĐÁM MÂY (CLOUD COMPUTING)
> **Học phần**: Điện toán đám mây (Cloud Computing)  
> **Chủ đề**: AWS Bảo mật & Chứng thực người dùng (AWS Security & User Authentication)  
> **Sinh viên thực hiện**: Trần Lộc  
> **Repository**: [Tranloc12/CloudComputing](https://github.com/Tranloc12/CloudComputing)  
---
![AWS](https://img.shields.io/badge/Cloud-AWS-orange.svg?style=for-the-badge&logo=amazon-aws)
![Cognito](https://img.shields.io/badge/Security-Amazon_Cognito-red.svg?style=for-the-badge&logo=amazon-aws)
![IAM](https://img.shields.io/badge/Identity-AWS_IAM-blue.svg?style=for-the-badge&logo=amazon-aws)
![S3](https://img.shields.io/badge/Storage-AWS_S3-green.svg?style=for-the-badge&logo=amazon-s3)
![JSON](https://img.shields.io/badge/Policy-JSON-yellow.svg?style=for-the-badge)
---
## 📌 MỤC LỤC
1. [📖 Giới Thiệu Đề Tài](#1-giới-thiệu-đề-tài)
2. [🏛️ Kiến Trúc & Dịch Vụ AWS Sử Dụng](#2-kiến-trúc--dịch-vụ-aws-sử-dụng)
3. [📁 Cấu Trúc Thư Mục Dự Án](#3-cấu-trúc-thư-mục-dự-án)
4. [🔐 Quy Trình Xác Thực & Phân Quyền (Auth Flow)](#4-quy-trình-xác-thực--phân-quyền-auth-flow)
5. [📊 Bảng Kịch Bản Kiểm Thử Bảo Mật Mẫu](#5-bảng-kịch-bản-kiểm-thử-bảo-mật-mẫu)
6. [🛠️ Hướng Dẫn Triển Khai & Cấu HÌnh](#6-hướng-dẫn-triển-khai--cấu-hình)
7. [👨‍💻 Thông Tin Sinh Viên](#7-thông-tin-sinh-viên)
---
## 1. 📖 GIỚI THIỆU ĐỀ TÀI
Đề tài **AWS Bảo Mật & Chứng Thực Người Dùng** thuộc môn học **Điện toán đám mây (Cloud Computing)**. Mục tiêu của dự án là thiết kế và triển khai một giải pháp quản lý danh tính, xác thực (Authentication) và phân quyền (Authorization) người dùng an toàn trên nền tảng điện toán đám mây Amazon Web Services (AWS).
### 🎯 Mục tiêu trọng tâm:
* Quản lý tập trung tài khoản người dùng với **Amazon Cognito User Pools**.
* Cấp quyền truy cập tài nguyên điện toán an toàn dựa trên token bằng **Identity Pools** và **AWS IAM**.
* Áp dụng nguyên tắc bảo mật tối thiểu (Principle of Least Privilege) bằng **IAM Policies & Roles**.
* Hỗ trợ xác thực hai yếu tố (**MFA**) và mã hóa dữ liệu trên đường truyền (HTTPS/TLS) & lưu trữ.
---
## 2. 🏛️ KIẾN TRÚC & DỊCH VỤ AWS SỬ DỤNG
|
 Dịch Vụ AWS 
|
 Vai Trò & Chức Năng Trong Hệ Thống 
|
|
:---
|
:---
|
|
**
Amazon Cognito User Pool
**
|
 Quản lý đăng ký, đăng nhập, quên mật khẩu, gửi email xác thực và phát hành các JWT Tokens (
`ID Token`
, 
`Access Token`
, 
`Refresh Token`
). 
|
|
**
Amazon Cognito Identity Pool
**
|
 Đổi JWT Token lấy thông tin xác thực AWS tạm thời (
`AccessKeyId`
, 
`SecretAccessKey`
, 
`SessionToken`
). 
|
|
**
AWS IAM (Identity & Access Management)
**
|
 Định nghĩa IAM Roles, IAM Policies để phân quyền chi tiết cho từng nhóm người dùng (Admin, User, Guest). 
|
|
**
AWS S3 (Simple Storage Service)
**
|
 Lưu trữ dữ liệu và tài nguyên người dùng với chính sách bảo mật (Bucket Policy) nghiêm ngặt. 
|
|
**
AWS CloudWatch
**
|
 Ghi log và giám sát các sự kiện đăng nhập, cảnh báo các truy cập bất thường. 
|
---
## 3. 📁 CẤU TRÚC THƯ MỤC DỰ ÁN
```text
CloudComputing/
├── README.md                           # Tài liệu hướng dẫn đồ án
├── Docs/                               # Tài liệu thiết kế & Báo cáo đồ án
│   ├── BaoCao_CloudComputing.docx      # File Báo cáo môn học Word
│   └── Architecture_Diagram.png        # Sơ đồ kiến trúc bảo mật AWS
├── Configurations/                     # File cấu hình AWS IAM Policies & JSON
│   ├── cognito-user-pool-config.json   # Thiết lập thuộc tính User Pool
│   └── s3-bucket-policy.json           # Chính sách truy cập S3 Bucket
└── Src/                                # Mã nguồn tích hợp xác thực
    ├── auth-service.js                 # Xử lý Sign Up / Sign In SDK AWS
    └── aws-config.js                   # Khởi tạo vùng AWS Region & Client ID
```
---
## 4. 🔐 QUY TRÌNH XÁC THỰC & PHÂN QUYỀN (AUTH FLOW)
```text
[Người Dùng] ──(1) Đăng ký / Đăng nhập──► [Amazon Cognito User Pool]
                                                    │
                                           (2) Trả về JWT Token
                                                    │
                                                    ▼
[Tài Nguyên AWS S3] ◄──(4) Truy cập được cấp── [AWS IAM Role / Policy]
                                                    ▲
                                                    │
                                           (3) Cấp Temporary AWS Credentials
                                                    │
[Người Dùng] ──(Đổi Token lấy Credential)──► [Cognito Identity Pool]
```
1. **Đăng ký & Xác thực Email**: Người dùng nhập Email/Password ➔ Cognito gửi mã OTP xác nhận về Email ➔ Kích hoạt tài khoản.
2. **Đăng nhập & Cấp Token**: Đăng nhập thành công trả về bộ 3 Token JSON Web Token (JWT):
   - `ID Token`: Chứa thông tin hồ sơ người dùng.
   - `Access Token`: Chứa thông tin nhóm và quyền hạn.
   - `Refresh Token`: Dùng để cấp lại Token mới khi hết hạn.
3. **Phân quyền tài nguyên (Authorization)**: Dựa trên nhóm (User Group), AWS IAM gắn Policy cho phép/từ chối thao tác trên AWS S3 Bucket.
---
## 5. 📊 BẢNG KỊCH BẢN KIỂM THỬ BẢO MẬT MẪU
|
 Test Case ID 
|
 Chức Năng Kiểm Thử 
|
 Dữ Liệu Đầu Vào 
|
 Kết Quả Mong Đợi 
|
 Kết Quả 
|
|
:---
|
:---
|
:---
|
:---
|
:---:
|
|
**
TC_SEC_01
**
|
 Đăng ký tài khoản mới 
|
 Email hợp lệ, Password mạnh 
|
 Tạo User thành công, trạng thái 
`UNCONFIRMED`
|
`PASS`
|
|
**
TC_SEC_02
**
|
 Nhập OTP xác thực Email 
|
 Nhập mã OTP gồm 6 chữ số 
|
 Tài khoản chuyển sang trạng thái 
`CONFIRMED`
|
`PASS`
|
|
**
TC_SEC_03
**
|
 Đăng nhập tài khoản 
|
 Đúng Username & Password 
|
 Trả về 
`AccessToken`
 và 
`IdToken`
 hợp lệ 
|
`PASS`
|
|
**
TC_SEC_04
**
|
 Đăng nhập sai mật khẩu 
|
 Nhập sai Password 5 lần 
|
 Khóa tài khoản tạm thời (Prevent Brute-force) 
|
`PASS`
|
|
**
TC_SEC_05
**
|
 Truy cập S3 bị cấm 
|
 Token hết hạn / Không đủ quyền 
|
 Trả về lỗi 
`403 Access Denied`
|
`PASS`
|
---
## 6. 🛠️ HƯỚNG DẪN TRIỂN KHAI & CẤU HÌNH
### 🔹 Bước 1: Cấu hình AWS CLI
```bash
aws configure
# Nhập AWS Access Key ID, Secret Access Key, Default region (vd: ap-southeast-1)
```
### 🔹 Bước 2: Tạo Amazon Cognito User Pool
1. Truy cập AWS Management Console ➔ Chọn dịch vụ **Amazon Cognito**.
2. Chọn **Create user pool**:
   - Sign-in options: `Email`
   - Password policy: Tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và ký tự đặc biệt.
   - Multi-factor authentication (MFA): `Optional` hoặc `Required`.
### 🔹 Bước 3: Áp dụng Policy cho S3 Bucket
Dán file cấu hình `s3-bucket-policy.json` vào phần Bucket Policy trên AWS S3:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCognitoAuthenticatedUsersOnly",
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
