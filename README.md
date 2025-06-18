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
