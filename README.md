# Human Action Recognition 

This project presents a lightweight deep learning model for **Human Action Recognition** using CNN-based architecture. The system can recognize actions from video sequences or image frames and is designed for performance and efficiency.

##  Project Structure

main/
│
├── Code/
│ └── HumanAction/
│ ├── app.py # Streamlit Web App
│ ├── predict.py # Prediction logic
│ ├── utils.py # Utility functions
│ ├── model_loader.py # Loads pretrained ONNX model
│ ├── resnet-34_kinetics.onnx # Pre-trained model (LFS-hosted)
│ └── media/
│ ├── videos/ # Example videos
│ └── icons/ # UI icons/images
│
├── requirements.txt # Python dependencies
└── README.md # Project overview


## ⚙️ Features

- Recognizes human actions in videos/images 
- Lightweight and optimized ResNet-34 ONNX model 
- Built with **Streamlit** for an interactive web app 🖥
- Clean UI and real-time classification 

##  Model

We use the **ResNet-34 trained on Kinetics dataset**, exported as an ONNX model for efficient inference.

##  How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/veeru594/human-action-recognition.git
   cd human-action-recognition/main/Code/HumanAction

🔗 Large Files
Due to GitHub limitations, the following large files were removed from the repository:

File Name	Description	Access
resnet-34_kinetics.onnx	Pretrained action recognition model	🔗 Download Link (Google Drive)
example_activities.mp4	Sample input video	🔗 Download Link (Google Drive)

Place them manually in main/Code/HumanAction/media/ after download.

 Author
Veerendra Kumar,  B.Tech Student graduate (2025)
GitHub: veeru594
