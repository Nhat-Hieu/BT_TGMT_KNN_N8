import cv2
import joblib
from skimage.feature import hog
from skimage import color

# --- Load lại pipeline đã lưu ---
knn_final = joblib.load("model/knn_model.pkl")
scaler = joblib.load("model/scaler.pkl")
pca = joblib.load("model/pca.pkl")
le = joblib.load("model/label_encoder.pkl")

# --- Hàm dự đoán từ 1 frame ---
def predict_from_frame(frame, img_size=(64, 64)):
    # Resize về cùng kích thước
    img_resized = cv2.resize(frame, img_size)

    # Chuyển grayscale + HOG
    gray = color.rgb2gray(img_resized)
    hog_feat = hog(
        gray,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        feature_vector=True
    )

    # Chuẩn hóa + PCA
    hog_feat = scaler.transform([hog_feat])
    hog_feat = pca.transform(hog_feat)

    # Dự đoán bằng KNN
    pred = knn_final.predict(hog_feat)[0]
    return le.inverse_transform([pred])[0]


# --- Mở webcam ---
cap = cv2.VideoCapture(1)   # đổi 0 hoặc 1 tùy máy
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # --- Vẽ khung xanh ở giữa ---
    margin_x = w // 3
    margin_y = h // 3
    x1, y1 = margin_x, margin_y
    x2, y2 = w - margin_x, h - margin_y
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # --- Vẽ đoạn màu đỏ bên phải ---
    red_x = x2
    red_y1 = y1 + (y2 - y1) // 3
    red_y2 = y2 - (y2 - y1) // 3
    cv2.line(frame, (red_x, red_y1), (red_x, red_y2), (0, 0, 255), 2)

    # --- Lấy ROI & dự đoán ---
    roi = frame[y1:y2, x1:x2]
    if roi.size > 0:
        label = predict_from_frame(roi)
        cv2.putText(frame, f"Prediction: {label}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    # --- Hiển thị ---
    cv2.imshow("Rock-Paper-Scissors (KNN Webcam)", frame)

    # Thoát bằng phím q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Thoát bằng nút X của cửa sổ
    if cv2.getWindowProperty("Rock-Paper-Scissors (KNN Webcam)", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
