# 📍 Lat-Long Extractor using OCR (EasyOCR + Flask)

## 🧠 Project Overview
This project is a web-based application that extracts **Latitude and Longitude** from an image using **OCR (Optical Character Recognition)**.

The system uses **EasyOCR** to read text from images and then processes that text to identify coordinate values.

---

## 🚀 Features

- 📸 Upload image from browser
- 🔍 Extract text using EasyOCR
- 📍 Automatically detect Latitude & Longitude
- 🧠 Smart filtering (removes incorrect values like time)
- 🔒 No image storage (processed in memory)

---

## 🧰 Technologies Used

- Python
- Flask
- EasyOCR
- OpenCV
- NumPy
- HTML, CSS, JavaScript

---

## ⚙️ How It Works

1. User uploads an image
2. Image is processed in memory (not saved)
3. OpenCV processes the image (crop top area)
4. EasyOCR extracts text
5. Regex finds latitude and longitude
6. Smart filtering removes wrong values
7. Output is displayed on the web page

---

## 📁 Project Structure
# 📍 Lat-Long Extractor using OCR (EasyOCR + Flask)

## 🧠 Project Overview
This project is a web-based application that extracts **Latitude and Longitude** from an image using **OCR (Optical Character Recognition)**.

The system uses **EasyOCR** to read text from images and then processes that text to identify coordinate values.

---

## 🚀 Features

- 📸 Upload image from browser
- 🔍 Extract text using EasyOCR
- 📍 Automatically detect Latitude & Longitude
- 🧠 Smart filtering (removes incorrect values like time)
- 🔒 No image storage (processed in memory)

---

## 🧰 Technologies Used

- Python
- Flask
- EasyOCR
- OpenCV
- NumPy
- HTML, CSS, JavaScript

---

## ⚙️ How It Works

1. User uploads an image
2. Image is processed in memory (not saved)
3. OpenCV processes the image (crop top area)
4. EasyOCR extracts text
5. Regex finds latitude and longitude
6. Smart filtering removes wrong values
7. Output is displayed on the web page

---

## 📁 Project Structure
.
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css

---

## 🧪 How to Run

### 1. Install Dependencies


pip install flask easyocr opencv-python numpy


---

### 2. Run the App


python app.py


---

### 3. Open in Browser


http://127.0.0.1:5000


---

## 💡 Advantages

- Fast processing
- No manual typing needed
- Secure (no image storage)
- Easy to use

---

## ⚠️ Limitations

- Accuracy depends on image quality
- May fail on blurry images

---

## ❤️ Made With

Made with ❤️ using Python & OCR

---

## 👨‍💻 Author

Prithu Maheshwari