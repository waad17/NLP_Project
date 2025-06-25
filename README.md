# NLP_Project

# NLP_Project

Multi-Task NLP System for Emergency Incident Reports 🚨

This project implements a multi-task Natural Language Processing (NLP) system that processes synthetic emergency incident reports to classify incident types, summarize the report, generate appropriate emergency actions, and construct automated responses. The system supports real-time predictions through a web interface using Flask.

---

## 🧠 Project Objectives

- Perform multi-label classification of emergency incidents (e.g., fire, ambulance, police)
- Generate concise summaries from report descriptions
- Recommend appropriate emergency actions
- Construct natural response messages to confirm dispatch
- Provide a user-friendly web interface for input and output display

---

## 📦 Dataset Description

- **Source**: Synthetic dataset generated for simulation
- **Records**: 50,000 incident reports
- **Language**: English
- **Fields**:
  - `description`: Raw incident report text
  - `summary`: Generated summary
  - `label`: Incident type(s) (multi-label)
  - `action`: Suggested operational response
  - `response`: Generated user-facing reply message

---

## 🛠️ Technologies Used

- Python, Flask
- TensorFlow / Keras
- Scikit-learn (MultiLabelBinarizer)
- Pickle (for tokenizer/model saving)
- HTML/CSS (for UI)
- Vanta.js (animated background)

---

## 🖥️ Web App Features

- Elegant home page with animated background and input form
- Result page displays:
  - Colored incident types (e.g., fire = red, police = blue)
  - Auto-generated dispatch message
  - A "New Report" button to submit again

---

## 🧩 Future Improvements

- Add Arabic language support for multilingual incident handling
- Train the model on real-world datasets (e.g., 911 call transcripts)
- Deploy on cloud for public access with GPU acceleration
- Integrate with live map services for location-based dispatching
- Enhance UI with icons and voice input

---

## 👩‍💻 Author

**Waad Alqahtani**  
AI Diploma Student, Tuwaiq Academy  
Date: **June 25, 2025**

---

## 🏫 Developed As Part of

**AI Diploma Program – Tuwaiq Academy**  
Cohort 2024–2025 – Final Project (NLP Track)
