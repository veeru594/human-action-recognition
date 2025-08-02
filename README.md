
# 🧠 Human Action Recognition (HAR) using Lightweight Deep Learning Models (Django-Based)

This project presents a **light-weight deep learning framework** for Human Action Recognition (HAR) in videos and image sequences. The system is implemented using the **Django web framework** and is designed for both high accuracy and efficient performance, suitable for real-time applications like smart surveillance, healthcare monitoring, and home automation.

---

## 📁 Project Structure

```
main/
│
├── Code/
│   └── HumanAction/
│       ├── manage.py              # Django project launcher
│       ├── human_app/             # Django app for UI & logic
│       │   ├── views.py           # Handles video upload & prediction
│       │   ├── urls.py            # URL routing
│       │   ├── templates/         # HTML UI templates
│       │   └── static/            # CSS, JS, media
│       ├── model_loader.py        # Loads ONNX models
│       ├── predict.py             # Core action recognition logic
│       ├── resnet-34_kinetics.onnx # Pretrained model (External)
│       └── media/
│           ├── videos/            # Sample inputs
│           └── icons/             # UI images
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project overview
```

---

## ⚙️ Features

- 🎥 Real-time human action recognition in videos
- ⚡ Lightweight CNNs: ResNet-34, VGG19, DenseNet, EfficientNet
- 🌐 Web interface built with **Django**
- 📦 Model inference using ONNX Runtime
- 📊 Evaluation with Precision, Recall, F1-Score, AUC

---

## 🧠 Deep Learning Models

This project uses **pre-trained models with transfer learning**:

| Model        | Key Strengths                              | Accuracy (UCF50) |
|--------------|---------------------------------------------|------------------|
| VGG19        | Deep CNN, small filters, batch norm         | 90.11%           |
| DenseNet     | Feature reuse, vanishing gradient handling  | 92.57%           |
| EfficientNet | Scalable, parameter-efficient, high accuracy| 94.25% ✅         |
| ResNet-34    | ONNX inference model used in app            | 91.7% (approx)   |

---

## 📊 Dataset

**UCF50 Human Action Dataset**
- 50 diverse human action categories
- Used to evaluate model performance

---

## 📈 Evaluation Metrics

- ✅ Precision
- 🔁 Recall
- 📊 F1-Score
- 📉 AUC Score

---

## 🔧 System Requirements

### 🖥️ Hardware:
- **Processor:** Intel i7
- **RAM:** 8 GB
- **Disk:** 1 TB
- **GPU:** Optional for training

### 💻 Software:
- **OS:** Windows 10
- **Language:** Python 3.8+
- **Frameworks:** Django, ONNX Runtime
- **Database:** SQLite (default)

---

## 🚀 How to Run the Django App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/veeru594/human-action-recognition.git
   cd human-action-recognition/main/Code/HumanAction
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the model and video manually:**

| File Name               | Description                       | Access Link        |
|------------------------|-----------------------------------|--------------------|
| `resnet-34_kinetics.onnx` | Pretrained model                 | 🔗 [Google Drive Link] |
| `example_activities.mp4`  | Sample input video               | 🔗 [Google Drive Link] |

> 📥 Place both files in `media/` directory.

4. **Run migrations and start server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Visit the app in your browser:**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🔬 Algorithms Used

- CNNs: VGG19, DenseNet, EfficientNet, ResNet34
- SoftMax classifier
- 3D CNNs and Autoencoders (research-oriented)
- ONNX Runtime for model inference

---

## ✅ Key Advantages

- ⚡ Lightweight and efficient
- 🎯 High Accuracy on UCF50
- 🔁 Fast inference via ONNX
- 🔄 Robust to variations (lighting, occlusion, background)
- 🛠️ Transfer Learning enabled

---

## ❗ Known Limitations

- GPU preferred for retraining
- Generalization to other datasets may require fine-tuning
- Manual download of ONNX model required

---
links

GitHub: [veeru594](https://github.com/veeru594)  
LinkedIn: [Profile](https://www.linkedin.com/in/veerendra-kumar-7615b2347/)

---

## 📌 Applications

- 🏥 Health & Fall Monitoring  
- 🏡 Home Automation  
- 🎥 Surveillance Systems  
- 🎮 Gesture-based Interfaces

---

> This Django-based HAR system proves that you can combine deep learning with real-time, efficient web deployment for impactful, real-world applications.
