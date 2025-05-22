
# Smart Trash Classifier API 🗑️🤖

A simple REST API for classifying trash images into categories: **paper**, **cardboard**, **glass**, **metal**, and **plastic**.

This API uses a TensorFlow Lite model trained with data from the **[TrashNet dataset](https://www.kaggle.com/datasets/feyzazkefe/trashnet)**, designed to be used with devices like an **ESP32-CAM**, or for web and mobile integrations.

---

## 🚀 Live Demo

API is live at:

```
https://smart-trash-api-rd11.onrender.com
```

---

## 🧠 API Endpoints

### 🔍 `POST /classify`

- **Description:** Classifies an image into one of the five trash categories.

#### 🔧 Request:
- `multipart/form-data`
- Key: `image`
- Value: image file (`.jpg`, `.png`, etc.)

#### 📦 Example using `curl`:

```bash
curl -X POST -F image=@test.jpg https://smart-trash-api-rd11.onrender.com/classify
```

#### ✅ Response:

```json
{
  "prediction": "paper"
}
```

---

## 💻 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/wander-junior/smart-trash-api.git
cd smart-trash-api
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run locally

```bash
python app.py
```

Server will run at:

```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

This API is deployed on **Render** using:

- A production WSGI server (`gunicorn`) with:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

---

## 🗂️ Project Structure

```
.
├── app.py             # Main Flask API
├── model.tflite       # TensorFlow Lite model
├── labels.txt         # Labels file
├── requirements.txt   # Python dependencies
├── .gitignore         # Files to ignore in Git
└── README.md          # Project documentation
```

---

## 🔥 Notes

- This is a **proof of concept**, designed for educational use.
- The model was trained using the **[TrashNet dataset](https://www.kaggle.com/datasets/garythung/trashnet)** available on Kaggle.
- The AI model was created and exported with **Teachable Machine**, using the **Floating Point** TensorFlow Lite format.
- TensorFlow Lite runs on CPU; GPU drivers are not needed.

---

## 👨‍💻 Authors

- Wander Junior - [GitHub](https://github.com/wander-junior)
