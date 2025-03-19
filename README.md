# Phishing Detector

## 📌 Project Description

Phishing Detector is a **machine learning-powered phishing detection system** designed to analyze URLs, emails, and websites to identify potential phishing attacks. The project extracts key features like **SSL certificate validity, domain age, URL length, and website content** to train an ML model that distinguishes between legitimate and phishing sites.

The final system will be integrated into a **browser extension** to provide real-time protection against phishing threats.

---

## 📁 Project Structure

```
phishing_detector/
│── data/                # Store phishing datasets
│── models/              # Trained ML models
│── scripts/             # Python scripts for feature extraction & training
│── extensions/          # Browser extension integration (later)
│── api/                 # Flask/Django API for detection (later)
│── notebooks/           # Jupyter notebooks for experimentation
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
```

---

## 🚀 Features

- **URL Analysis**: Checks for suspicious patterns, domain age, and SSL certificates.
- **Email Analysis**: Detects phishing attempts using NLP-based classifiers.
- **Website Content Analysis**: Extracts and evaluates text for phishing indicators.
- **Machine Learning Models**: Uses Decision Trees, Random Forest, or Deep Learning models for classification.
- **Real-Time Protection**: Planned integration with a **browser extension**.
- **API for Detection**: (Future) Flask/Django-based API to scan URLs/emails in real-time.

---

## 🔧 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mahingaRodin/Phishing-Detector.git
cd Phishing-Detector
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Feature Extraction & Model Training

```bash
python scripts/data_loader.py   # Collects phishing data & extracts features
python scripts/train_model.py   # Trains the phishing detection model
```

### 5️⃣ Test the Model

```bash
python scripts/test_model.py    # Evaluates model accuracy
```

---

## 📌 Future Enhancements

✔️ Implement real-time URL scanning via API.\
✔️ Deploy a **browser extension** for on-the-fly phishing detection.\
✔️ Improve NLP models for better email phishing detection.\
✔️ Add **adversarial attack resistance** to prevent phishing evasion techniques.

---

## 🤝 Contributing

Feel free to contribute by opening issues or submitting pull requests!

---

## 🛡️ License

This project is licensed under the **MIT License**.

---

🚀 **Stay Safe from Phishing Attacks!** 🔐
