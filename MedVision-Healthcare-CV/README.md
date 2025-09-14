# MedVision - Healthcare & Wellness (Computer Vision in Medical Imaging)

## Overview
MedVision is a computer vision project aimed at applying deep learning techniques to **medical imaging, diagnostics, and patient care**. 
The project demonstrates how AI can assist in early disease detection, anomaly localization, and patient monitoring.

## Features
- Image classification for disease diagnosis (e.g., X-ray, CT scans)
- Segmentation of abnormal regions (tumors, infections)
- Explainable AI with Grad-CAM heatmaps
- Patient monitoring using webcam (pose/facial analysis)
- Prototype dashboard for healthcare professionals

## Tech Stack
- Python, TensorFlow / PyTorch
- OpenCV for image preprocessing
- Flask/Streamlit for prototype demo
- Jupyter for experimentation

## Repository Structure
- `data/` : Dataset references and small samples
- `notebooks/` : Prototyping and model training notebooks
- `src/` : Core source code (training, inference, preprocessing)
- `models/` : Saved models
- `docs/` : Documentation and PPT

## How to Run
1. Clone the repo
```bash
git clone <repo-link>
cd MedVision-Healthcare-CV
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run demo (example with Streamlit)
```bash
streamlit run src/app.py
```

## Dataset References
- [Chest X-ray Pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

## Future Work
- Integrate multimodal data (text + image)
- Enhance explainability
- Deploy as mobile app for rural healthcare

---
**Team MedVision | INSIGHT 2.0 Hackathon**
