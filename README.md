# Nhận diện Kéo-Búa-Bao bằng thuật toán KNN

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)

## Giới thiệu
Mô hình K-Nearest Neighbors phân loại cử chỉ tay Kéo-Búa-Bao theo thời gian thực, sử dụng đặc trưng HOG và giảm chiều PCA.

## Dữ liệu
[Rock Paper Scissors Dataset](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors) từ Kaggle
- 2,520 ảnh huấn luyện (840 ảnh mỗi lớp)
- 372 ảnh kiểm tra (124 ảnh mỗi lớp)
- Ảnh RGB 300x200 pixel

## Hướng dẫn sử dụng

### Cài đặt
```bash
git clone <repo-url>
cd rock-paper-scissors-knn
pip install numpy opencv-python scikit-learn matplotlib seaborn scikit-image joblib
```

### Tải dữ liệu
Tải từ Kaggle và giải nén vào thư mục `dataset/` theo cấu trúc:
```
dataset/
├── train/
├── test/
└── validation/
```

### Sử dụng
1. **Huấn luyện mô hình**: Chạy notebook `KNN.ipynb`
2. **Dự đoán ảnh đơn**: 
   ```python
   predict_single("check/anh.jpg")
   ```
3. **Demo webcam**: 
   ```bash
   python run.py
   ```

## Hiệu suất mô hình
- **Độ chính xác**: 95.2%
- **Đặc trưng**: HOG + PCA
- **K tối ưu**: 5 (cross-validation)
- **Thời gian thực**: 30+ FPS

## Tính năng chính
- Trích xuất đặc trưng HOG để nhận diện cử chỉ chính xác
- Giảm chiều PCA tối ưu hiệu suất
- Dự đoán webcam theo thời gian thực
- Đánh giá mô hình toàn diện

---
**Nguồn dữ liệu**: [Kaggle - Rock Paper Scissors Dataset](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)