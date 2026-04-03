<img width="983" height="730" alt="image" src="https://github.com/user-attachments/assets/9be28069-69b0-46c7-9e68-e745cd7589cd" />DEVOPS MINI PROJECT

MỤC TIÊU
 Làm việc với project thực tế từ GitHub
 Áp dụng DevOps cơ bản: Git, Environment Variables, Docker, Docker Compose
 Triển khai hệ thống gồm Backend + Frontend + Database
YÊU CẦU CHUNG
 Làm cá nhân (mỗi sinh viên 1 bài)
1. TẠO PROJECT
Cách 1: Clone từ GitHub
 Repository public
 Có Backend + Frontend + Database
<img width="333" height="119" alt="image" src="https://github.com/user-attachments/assets/517a465a-939b-4f92-8fae-3dd9b9e33ac3" />

Cách 2: Tự xây dựng
Backend:
 Ít nhất 2 API (GET + POST/PUT)
<img width="261" height="115" alt="image" src="https://github.com/user-attachments/assets/e2c960f1-72da-4122-b359-7c6788d84bcf" />

Frontend:
 Hiển thị dữ liệu từ backend
 Có tương tác (form/button)
<img width="215" height="85" alt="image" src="https://github.com/user-attachments/assets/6016d2f3-3720-46b6-b93d-3ccc894152d6" />

Database:
 Lưu trữ dữ liệu thực
 Không được dùng dữ liệu hard-code
<img width="1919" height="1018" alt="image" src="https://github.com/user-attachments/assets/c4c68d58-8b0c-4940-9a7b-a01cde47e221" />

3. GIT
 Tạo repository riêng
 Có ít nhất 5 commit, message rõ ràng
 Có 3 branch: main/master, develop, feature
//git hub
ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (main)
$ git init
Initialized empty Git repository in D:/Anh_Python/DevOff/Tran_Duc_Anh_2251220096/.git/

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (master)
$ git remote add origin https://github.com/Anhcoder46/Anh_Python.git

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (master)
$ git add docker-compose.yml .env database/

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (master)
$ git commit -m "Init project with docker-compose and database config"
[master (root-commit) 1b4038b] Init project with docker-compose and database config
 3 files changed, 55 insertions(+)
 create mode 100644 .env
 create mode 100644 database/init.sql
 create mode 100644 docker-compose.yml

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (master)
$ git branch -M main

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (main)
$ git checkout -b develop
Switched to a new branch 'develop'

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git add backend/

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git commit -m "Add backend setup with Flask and API routes"
[develop 5f42fbe] Add backend setup with Flask and API routes
 3 files changed, 78 insertions(+)
 create mode 100644 backend/Dockerfile
 create mode 100644 backend/app.py
 create mode 100644 backend/requirements.txt

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git checkout -b feature
Switched to a new branch 'feature'

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (feature)
$ git add frontend/index.html

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (feature)
$ git commit -m "Create frontend layout and fetch API"
[feature f32acda] Create frontend layout and fetch API
 1 file changed, 61 insertions(+)
 create mode 100644 frontend/index.html

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (feature)
$ git add frontend/Dockerfile

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (feature)
$ git commit -m "Add Dockerfile for frontend Nginx"
[feature 52fbe84] Add Dockerfile for frontend Nginx
 1 file changed, 4 insertions(+)
 create mode 100644 frontend/Dockerfile

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (feature)
$ git checkout develop
Switched to branch 'develop'

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git merge feature
Updating 5f42fbe..52fbe84
Fast-forward
 frontend/Dockerfile |  4 ++++
 frontend/index.html | 61 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 65 insertions(+)
 create mode 100644 frontend/Dockerfile
 create mode 100644 frontend/index.html

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git commit -m "Merge feature branch to develop"
On branch develop
nothing to commit, working tree clean

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git push -u origin develop
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 20 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), 4.23 KiB | 1.41 MiB/s, done.
Total 20 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
remote:
remote: Create a pull request for 'develop' on GitHub by visiting:
remote:      https://github.com/Anhcoder46/Anh_Python/pull/new/develop
remote:
To https://github.com/Anhcoder46/Anh_Python.git
 * [new branch]      develop -> develop
branch 'develop' set up to track 'origin/develop'.

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git push -u origin feature
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feature' on GitHub by visiting:
remote:      https://github.com/Anhcoder46/Anh_Python/pull/new/feature
remote:
To https://github.com/Anhcoder46/Anh_Python.git
 * [new branch]      feature -> feature
branch 'feature' set up to track 'origin/feature'.

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (develop)
$ git checkout main
Switched to branch 'main'

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (main)
$ git push -f origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Anhcoder46/Anh_Python.git
 + 5d8e82b...1b4038b main -> main (forced update)

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (main)
$ git checkout main
Already on 'main'

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (main)
$ git merge develop
Updating 1b4038b..52fbe84
Fast-forward
 backend/Dockerfile       |  7 +++++
 backend/app.py           | 67 ++++++++++++++++++++++++++++++++++++++++++++++++
 backend/requirements.txt |  4 +++
 frontend/Dockerfile      |  4 +++
 frontend/index.html      | 61 +++++++++++++++++++++++++++++++++++++++++++
 5 files changed, 143 insertions(+)
 create mode 100644 backend/Dockerfile
 create mode 100644 backend/app.py
 create mode 100644 backend/requirements.txt
 create mode 100644 frontend/Dockerfile
 create mode 100644 frontend/index.html

ACER@AnhTapCode MINGW64 /d/Anh_Python/DevOff/Tran_Duc_Anh_2251220096 (main)
$ git push origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Anhcoder46/Anh_Python.git
   1b4038b..52fbe84  main -> main

5. TÍNH NĂNG ỨNG DỤNG
Trang thông tin cá nhân (/about):
 Họ tên sinh viên
 Mã số sinh viên
 Lớp
<img width="983" height="730" alt="image" src="https://github.com/user-attachments/assets/0c63416e-0404-4276-a36a-2806b518395e" />

Health Check (/health):
 { "status": "ok" }
<img width="1044" height="691" alt="image" src="https://github.com/user-attachments/assets/04220539-2ab8-4eee-a0b8-ae192442311f" />

Environment Variables:
 PORT
 DB_HOST / DB_URL
 APP_NAME

4. DATABASE
 Sử dụng MySQL / PostgreSQL / MongoDB / ...
 Không dùng dữ liệu hard-code

6. DOCKER
 Dockerfile cho Backend
<img width="1486" height="729" alt="image" src="https://github.com/user-attachments/assets/c52f3fe6-ff86-4bb2-b090-12fcd17a9ac7" />

 Dockerfile cho Frontend
<img width="1481" height="741" alt="image" src="https://github.com/user-attachments/assets/012bd791-a306-4089-97ab-a4ef8d2484ce" />

 Database chạy container riêng
<img width="1482" height="718" alt="image" src="https://github.com/user-attachments/assets/b280e616-1713-489c-8cd4-456f5405be7c" />

8. DOCKER COMPOSE
 Có docker-compose.yml
 Chạy được Backend + Frontend + Database
<img width="1432" height="661" alt="image" src="https://github.com/user-attachments/assets/150f4558-124d-42bb-8fd6-b313385072b8" />

9. DOCKER HUB
 Build image Backend + Frontend
 Push lên Docker Hub
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/b33a2d66-0db1-401a-a340-9b1518b7c296" />

10. SẢN PHẨM NỘP
Phần A: Thông tin chung
 Thông tin sinh viên
 Giới thiệu ứng dụng
 Tính năng
 Use cases
Phần B: Minh chứng

 Link GitHub
 Link Docker Hub
 Ảnh VSCode (commit)
 Ảnh GitHub (branch)
 Ảnh Docker running
 Trang /about
 Endpoint /health
CHECKLIST
 Có commit history
 Có BE + FE + DB
 Có /about
 Có /health
 Có .env
 Có Dockerfile
 Có docker-compose
 Push Docker Hub
