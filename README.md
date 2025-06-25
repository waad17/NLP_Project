# NLP_Project

Incident Classification and Response Generation System using NLP 🚨

This project is an end-to-end NLP application that classifies Arabic emergency incident descriptions into relevant response teams (e.g., Police, Fire, Ambulance) and automatically generates a suitable response message. Built with deep learning and deployed through an interactive web interface using Flask.

---

## 🔍 Project Overview

This application uses a multi-label classification model trained on Arabic emergency report descriptions. It detects the type(s) of incident and recommends which teams should be dispatched. The model is based on TensorFlow and trained using preprocessed tokenized text data.

Users interact through a modern, styled web interface where they can describe an incident and immediately receive predictions and an automated response message.

---

## 🎯 Project Objectives

- Perform multi-label classification on Arabic incident reports.
- Automatically generate natural response messages based on predicted labels.
- Design a lightweight Flask web application to interact with the model.
- Use expressive UI components with real-time prediction display.
- Provide clean UX with background animation and clear feedback messages.

---

## 📊 Dataset Description

- **Source**: Synthetic and real emergency incident reports in Arabic.
- **Type**: Multi-label text classification.
- **Labels**: `['fire', 'police', 'ambulance', 'civil defense', 'unknown']`
- **Format**: Arabic text description with one or more corresponding response labels.
- **Tokenization**: Handled using Keras Tokenizer and pickled for reuse.

---

## 🧠 Model Architecture

- **Framework**: TensorFlow / Keras
- **Input**: Cleaned, tokenized, and padded Arabic incident text
- **Model Type**: Custom Sequential or Functional model with sigmoid activation for multi-label output
- **Output**: Probability vector for each label
- **Threshold**: 0.3 for multi-label prediction
- **Postprocessing**: `MultiLabelBinarizer` used to decode predictions

---

## 💻 Technologies Used

- Python
- TensorFlow
- Flask
- HTML5 + CSS3
- Vanta.js (for background animation)
- Google Fonts (Space Grotesk)
- Pickle (for loading tokenizer and label encoder)

---

## 📂 Project Structure
├── app.py # Flask backend
├── index.html # Main form UI
├── result.html # Response display page
├── tokenizer_desc.pkl # Tokenizer for Arabic descriptions
├── tokenizer_action.pkl # Optional: Tokenizer for action text
├── mlb.pkl # MultiLabelBinarizer for label decoding
├── incident_response_model.keras # Trained TensorFlow model
├── static/
│ └── twiq-logo.png # Tuwaiq logo used in UI



