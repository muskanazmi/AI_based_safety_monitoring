# 🛡️ AI-Based Safety Monitoring System

Welcome to the future of safety!  
This project uses AI to **detect violence in real-time** using deep learning and computer vision — because everyone deserves to feel safe. 🧠📹

---

## 🚨 Demo

🎥 Here’s how our model watches over public safety like a superhero in disguise:

![Demo](demo/video-SqtunTxx-online-video-cutt.gif)

---

## 🔍 What It Does

✅ Detects violence in surveillance footage  
✅ Triggers alerts if violence is detected  
✅ Lightweight and mobile-friendly using MobileNetV2  
✅ Sends snapshot of the violent activity along with the location via a Telegram bot API  
✅ Suitable for schools, stations, and public places  

---

## 🧠 Tech Stack

- 🔍 **Model**: MobileNetV2 + Attention Layer  
- 📦 **Frameworks**: TensorFlow / Keras  
- 💡 **Languages**: Python  
- 🎞️ **Dataset**: AIRTLAB dataset

---
## 🛠️ Hardware Setup & Integration

This AI-based safety monitoring system is designed to run on affordable, accessible hardware, making it deployable in real-world environments such as schools, stations, and public places.

### 🔧 Hardware Components Used
- **Raspberry Pi 4**: Runs the fine-tuned MobileNetV2 model with attention mechanism.
- **Smartphone (DroidCam)**: Acts as a real-time camera for video input.
- **Breadboard + Buzzer**: Buzzer connected to GPIO pins for physical alerts.
- **Wiring & Connectors**: To integrate Raspberry Pi with breadboard and buzzer.
- **Wi-Fi Network**: Connects the Pi, camera, and display device.

### ⚙️ System Integration Workflow
1. 📷 **Live Video Feed**: A DroidCam-enabled smartphone streams real-time video over Wi-Fi to the Raspberry Pi.
2. 🧠 **On-Device Inference**: The fine-tuned MobileNetV2 model (with attention layer) is flashed and executed on the Raspberry Pi for local processing.
3. 🚨 **Violence Detection & Alerting**:
   - When violence is detected:
     - A **snapshot** of the violent frame is captured.
     - Snapshot and location data are sent to a **Telegram channel** using Telegram Bot API.
     - A **buzzer** connected via breadboard is triggered to raise an on-site alert.
4. 💻 **Display Output**: The inference output is displayed on the laptop screen connected over the same Wi-Fi network.

This setup enables real-time violence detection with automatic alerting, all from a compact, portable, and cost-effective device configuration.

## 🚀 How to Run

```bash
# Clone this repo
git clone https://github.com/muskanazmi/AI_based_safety_monitoring.git

# Navigate into the folder
cd AI_based_safety_monitoring

# Install dependencies
pip install -r requirements.txt

# Run the model
python violence_detection.py
```
## ❓ Questions

Have questions about the model architecture or fine-tuning process?

Feel free to reach out:

📧 **Email**: [muskan685amu@gmail.com](mailto:muskan685amu@gmail.com)  
🐙 **GitHub Issues**: You can also [open an issue](https://github.com/muskanazmi/AI_based_safety_monitoring/issues) on this repository.

