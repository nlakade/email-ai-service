# Smart Email Classifier & Rewriter

Gen-AI powered email processing service with classification and tone rewriting capabilities.

## Features
- Email classification (Work/Personal/Finance/Spam)
- Email rewriting in specified tones (professional/friendly/concise)
- FastAPI REST endpoints
- Docker container support

## Setup Instructions

1. **Clone repository**
   ```bash
   https://github.com/nlakade/email-ai-service

Set environment variables

bash
cp .env.example .env
# Add your OpenAI API key to .env
Install dependencies

bash
pip install -r requirements.txt
Run service

bash
uvicorn app.main:app --reload
Using Docker
bash
docker build -t email-ai .
docker run -p 8000:8000 --env-file .env email-ai
API Documentation
Access interactive docs at http://localhost:8000/docs

Endpoints
POST /classify_email

json
{
  "email_content": "Your email text here..."
}
POST /rewrite_email

json
{
  "email_content": "Your email text here...",
  "tone": "professional"
}
Sample Requests
bash
# Classification
curl -X POST "http://localhost:8000/classify_email" \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Meeting rescheduled to Wednesday 3 PM"}'

# Rewriting
curl -X POST "http://localhost:8000/rewrite_email" \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Hey, can we push our meeting?", "tone": "professional"}'
Sample Responses
Classification

json
{"category": "Work"}
Rewriting

json
{"rewritten_email": "Dear colleague, would it be possible to reschedule our meeting..."}




Postman Testing Guide
use:

URL: POST http://localhost:8000/classify_email

Headers:

json
{
  "Content-Type": "application/json"
}


Body:

json
{
  "email_content": "Team, the project deadline is extended"
}

Output:


json
{"category": "Work"}
