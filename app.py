from flask import Flask, render_template, request
import cv2
import easyocr
import numpy as np
import re
import base64
import os

app = Flask(__name__)

reader = easyocr.Reader(['en'])


def extract_lat_long_from_memory(file_bytes):
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    h, w = img.shape[:2]

    crop = img[0:int(h*0.18), 0:int(w*0.45)]

    results = reader.readtext(crop, detail=0)
    text = " ".join(results)

    print("\n🔍 OCR TEXT:\n", text)

    lat_match = re.search(r'[Ll][a4t][:\s]*([0-9]+\.[0-9]+)', text)
    lon_match = re.search(r'[Ll][o0][nmgq9][g]?\s*[:\-]?\s*([0-9]+\.[0-9]+)', text)

    numbers = re.findall(r'\d+\.\d+', text)
    numbers = list(dict.fromkeys(numbers))

    latitude = "Not found"
    longitude = "Not found"

    if lat_match:
        latitude = lat_match.group(1)

    if lon_match:
        longitude = lon_match.group(1)

    for num in numbers:
        value = float(num)

        if value < 20:
            continue

        if latitude == "Not found" and 20 <= value <= 40:
            latitude = num

        elif longitude == "Not found" and 60 <= value <= 100:
            longitude = num

    return latitude, longitude


@app.route("/", methods=["GET", "POST"])
def index():
    lat, lon = None, None
    image_data = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            # 🔥 read file into memory
            file_bytes = np.frombuffer(file.read(), np.uint8)

            # OCR processing
            lat, lon = extract_lat_long_from_memory(file_bytes)

            # 🔥 convert to base64 for preview
            image_data = base64.b64encode(file_bytes).decode('utf-8')

    return render_template("index.html", lat=lat, lon=lon, image_data=image_data)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)