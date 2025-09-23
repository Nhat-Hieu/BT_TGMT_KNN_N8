# Hướng Dẫn Làm Việc Với Hai Repo

Tài liệu này hướng dẫn cách làm việc với hai repository:

- Repo gốc (upstream): **Nhat-Hieu/BT_TGMT_KNN_N8**
- Repo cá nhân (origin): **MinhKhanh-EternAI/rps-opencv-knn**

Bạn đã được thêm quyền *collaborator* trên repo gốc, vì vậy có thể push và tạo nhánh trực tiếp.

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
