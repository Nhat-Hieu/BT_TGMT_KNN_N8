# 📘 Git Workflow Guide (Làm việc với nhánh riêng)

## 0. Thiết Lập Ban Đầu

### 0.1. Clone repo gốc (Nhat-Hieu)
```bash
git clone https://github.com/Nhat-Hieu/BT_TGMT_KNN_N8.git
cd BT_TGMT_KNN_N8
```

### 0.2. Thêm remote cho repo cá nhân
```bash
git remote rename origin Nhat-Hieu
git remote add origin https://github.com/MinhKhanh-EternAI/rps-opencv-knn.git
```

Kiểm tra lại remote:
```bash
git remote -v
```
👉 Kết quả mong đợi:
```
origin    https://github.com/MinhKhanh-EternAI/rps-opencv-knn.git (fetch)
origin    https://github.com/MinhKhanh-EternAI/rps-opencv-knn.git (push)
Nhat-Hieu https://github.com/Nhat-Hieu/BT_TGMT_KNN_N8.git (fetch)
Nhat-Hieu https://github.com/Nhat-Hieu/BT_TGMT_KNN_N8.git (push)
```

---

## 1. Chuyển Nhánh (Switch Branches)

Liệt kê tất cả nhánh local:
```bash
git branch
```

Chuyển sang một nhánh có sẵn:
```bash
git checkout ten-nhanh
```

Tạo và chuyển sang nhánh mới từ `main`:
```bash
git checkout -b khanhnvm main
```

Tạo và chuyển sang nhánh mới từ `Nhat-Hieu/main`:
```bash
git checkout -b khanhnvm Nhat-Hieu/main
```

---

## 2. Push Code

Push code lên repo cá nhân (origin):
```bash
git push origin khanhnvm
```

Push code lên repo gốc (Nhat-Hieu):
```bash
git push Nhat-Hieu khanhnvm
```

Thiết lập tracking khi push lần đầu:
```bash
git push -u origin khanhnvm
```

---

## 3. Pull Code

Cập nhật code từ repo gốc (`main`):
```bash
git pull Nhat-Hieu main
```

Cập nhật code từ repo cá nhân (`main`):
```bash
git pull origin main
```

---

## 4. Merge Trên GitHub

Sau khi đã push nhánh (ví dụ: `khanhnvm`) lên GitHub:

1. Mở GitHub trong trình duyệt.  
2. Tạo **Pull Request (PR)** từ nhánh `khanhnvm` vào `main`.  
3. Review thay đổi, xử lý conflict nếu có.  
4. Merge PR.  

👉 Vì bạn có quyền collaborator trên repo `Nhat-Hieu`, bạn có thể mở PR trực tiếp và merge vào `main` của repo đó.

---

## 5. Các Lệnh Git Hữu Ích Khác

- **Xem trạng thái**
  ```bash
  git status
  ```
- **Xem log commit**
  ```bash
  git log --oneline --graph --all
  ```
- **Chuyển đổi branch**
  ```bash
  git checkout branch-name
  ```
- **Tạo branch mới từ branch hiện tại**
  ```bash
  git checkout -b new-feature
  ```
- **Xóa branch**
  ```bash
  git branch -d branch-name       # xóa local
  git push origin --delete branch-name   # xóa trên remote
  ```
- **Hủy thay đổi chưa commit**
  ```bash
  git restore file.txt
  ```
- **Sửa commit gần nhất (chưa push)**
  ```bash
  git commit --amend -m "message mới"
  ```
- **Khôi phục file từ branch khác**
  ```bash
  git checkout main -- path/to/file.py
  ```

---

## 6. Workflow Tóm Tắt

1. `git clone https://github.com/Nhat-Hieu/BT_TGMT_KNN_N8.git`  
2. `git remote rename origin Nhat-Hieu`  
3. `git remote add origin https://github.com/MinhKhanh-EternAI/rps-opencv-knn.git`  
4. `git checkout main`  
5. `git pull Nhat-Hieu main`  
6. `git checkout -b khanhnvm main`  
7. Code → `git add .` → `git commit -m "..."`  
8. `git push origin khanhnvm`  
9. Mở PR trên GitHub và merge.  
