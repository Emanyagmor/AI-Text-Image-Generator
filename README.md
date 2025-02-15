pip install openai flask requests
curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json" -d '{"prompt": "Write a short story", "mode": "text"}'
