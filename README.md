Here's a fully **corrected and properly formatted `README.md` file** for your project using standard Markdown:

---

````markdown
# 📧 Smart Email Classifier & Rewriter

Gen-AI powered email processing service with classification and tone rewriting capabilities.

---

## 🚀 Features

- ✉️ Email classification (Work / Personal / Finance / Spam)
- ✍️ Email rewriting in specified tones (professional / friendly / concise)
- ⚡ FastAPI-based REST API
- 🐳 Docker container support

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nlakade/email-ai-service.git
cd email-ai-service
````

### 2. Set Environment Variables

Copy the example `.env` file and add your OpenAI API key:

```bash
cp .env .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Dependencies

Make sure Python 3.8+ is installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Run the Service

```bash
uvicorn app.main:app --reload
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Using Docker

Build and run the container:

```bash
docker build -t email-ai .
docker run -p 8000:8000 --env-file .env email-ai
```

---

## 📡 API Endpoints

### 🔹 POST `/classify_email`

Classifies the email into categories like `Work`, `Personal`, `Finance`, or `Spam`.

**Request:**

```json
{
  "email_content": "Your email text here..."
}
```

**Sample curl:**

```bash
curl -X POST "http://localhost:8000/classify_email" \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Meeting rescheduled to Wednesday 3 PM"}'
```

**Response:**

```json
{
  "category": "Work"
}
```

---

### 🔹 POST `/rewrite_email`

Rewrites the email in a given tone (e.g., `professional`, `friendly`, `concise`).

**Request:**

```json
{
  "email_content": "Your email text here...",
  "tone": "professional"
}
```

**Sample curl:**

```bash
curl -X POST "http://localhost:8000/rewrite_email" \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Hey, can we push our meeting?", "tone": "professional"}'
```

**Response:**

```json
{
  "rewritten_email": "Dear colleague, would it be possible to reschedule our meeting..."
}
```

---

## 🧪 Postman Testing Guide

### Endpoint: `POST http://localhost:8000/classify_email`

**Headers:**

```json
{
  "Content-Type": "application/json"
}
```

**Body:**

```json
{
  "email_content": "Team, the project deadline is extended"
}
```

**Output:**

```json
{
  "category": "Work"
}
```

---


---

## 👨‍💻 Author

[Nitesh Lakade](https://github.com/nlakade)


