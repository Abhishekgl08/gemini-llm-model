# Gemini LLM & Vision Streamlit Application

> **Interactive text Q&A and image understanding web applications powered by Google Gemini Pro & Gemini Pro Vision.**

---

## 🛠️ Features
- **Text Q&A (`app.py`)**: Ask general questions and receive streaming generative responses using Gemini Pro.
- **Multimodal Image Intelligence (`vision.py`)**: Upload any image (`.jpg`, `.jpeg`, `.png`) and ask questions directly about its visual content.

---

## 🚀 Setup & Execution

### 1. Set Up Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Key
Copy the template and enter your Gemini API key:
```bash
cp .env.example .env
```
In `.env`:
```text
GOOGLE_API_KEY=your_actual_gemini_api_key
```

### 3. Run the Applications
* **Text Q&A App**:
  ```bash
  streamlit run app.py
  ```
* **Image Vision App**:
  ```bash
  streamlit run vision.py
  ```
