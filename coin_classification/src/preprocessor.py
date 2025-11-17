
import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "train")
OUT_DIR = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(OUT_DIR, exist_ok=True)

def preprocess_images():
    print("🔧 Starting preprocessing...")

    for file in os.listdir(RAW_DIR):
        if file.endswith(".png"):
            img_path = os.path.join(RAW_DIR, file)

            img = cv2.imread(img_path)
            if img is None:
                print(f"⚠️ Cannot read {file}, skipping.")
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, (128, 128))

            cv2.imwrite(os.path.join(OUT_DIR, file), resized)

    print("✅ Preprocessing completed! Files saved to data/processed/")

if __name__ == "__main__":
    preprocess_images()
